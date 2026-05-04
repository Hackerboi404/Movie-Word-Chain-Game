import asyncio
import logging
import os
import random
import re

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Flask imports for Render Web Service
from flask import Flask

# --- CONFIGURATION ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    print("Error: BOT_TOKEN not found in environment variables.")
    exit(1)

# --- DATA IMPORT ---
from data import MOVIE_SET, MOVIES

# --- FLASK APP SETUP (Keep Alive) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, use_reloader=False)

# --- BOT & GAME STATE ---
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# In-memory Game State
games = {}

# --- HELPER FUNCTIONS ---

def get_game(chat_id):
    return games.get(chat_id)

def clean_string(text):
    """Remove spaces and special chars to check letters"""
    return re.sub(r'[^a-zA-Z]', '', text).lower()

def get_last_letter(movie_name):
    cleaned = clean_string(movie_name)
    if not cleaned:
        return None
    return cleaned[-1].upper()

def normalize_movie(name):
    """
    Normalize movie name for comparison.
    1. Strip whitespace.
    2. Convert to Title Case (e.g., golmaal -> Golmaal) - Used for display only.
    """
    return name.strip().title()

async def next_turn(chat_id):
    game = get_game(chat_id)
    if not game or not game['is_active']:
        return

    # Check for winner (only 1 player left)
    if len(game['players']) == 1:
        winner = game['players'][0]
        # Using mention_html for better tagging
        await bot.send_message(chat_id, f"🏆 <b>GAME OVER!</b>\n\n👑 Winner: {winner.mention_html()}\n\nCongratulations!")
        del games[chat_id]
        return

    # Move to next player index (looping)
    game['current_idx'] = (game['current_idx'] + 1) % len(game['players'])
    current_player = game['players'][game['current_idx']]

    # Tag the player and show the letter
    game['current_letter'] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') if game['current_letter'] == '' else game['current_letter']
    
    # IMPROVED TAGGING & SPACING
    msg = f"🎬 <b>{current_player.full_name}'s Turn!</b>\n\n"
    msg += f"🔤 Send a movie starting with: <b>'{game['current_letter']}'</b>"
    
    await bot.send_message(chat_id, msg)

    # Set Timer (35 seconds)
    if game['timer_task']:
        game['timer_task'].cancel()
    
    game['timer_task'] = asyncio.create_task(check_timeout(chat_id, game['current_idx'], 35))

async def check_timeout(chat_id, expected_player_idx, timeout_seconds):
    await asyncio.sleep(timeout_seconds)
    
    game = get_game(chat_id)
    # Validate that game is still running and it's still the same player's turn
    if game and game['is_active'] and game['current_idx'] == expected_player_idx:
        # Time out - Eliminate player
        eliminated_player = game['players'].pop(expected_player_idx)
        # Fixed: Use mention_html for proper tagging in timeout
        await bot.send_message(chat_id, f"⏱️ <b>Time's Up!</b>\n😢 {eliminated_player.mention_html()} eliminated for being too slow!")
        
        # Adjust index so we don't skip the next person after popping
        game['current_idx'] = expected_player_idx - 1 
        await next_turn(chat_id)

# --- HANDLERS ---

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "🎬 <b>Movie Word Chain Game</b>\n\n"
        "📜 <b>Rules:</b>\n"
        "1. Join with /join\n"
        "2. Start game with <b>/playgame</b>\n"
        "3. Send a movie name starting with the last letter of the previous movie.\n"
        "4. Valid movies only (based on database).\n"
        "5. <b>35 seconds</b> per turn.\n\n"
        "Commands:\n"
        "/join - Join game\n"
        "/leave - Leave game\n"
        "/players - See players\n"
        "/playgame - Start Game\n"
        "/stopgame - Stop"
    )
    await message.answer(text)

@dp.message(Command("join"))
async def cmd_join(message: types.Message):
    chat_id = message.chat.id
    user = message.from_user
    user_id = user.id

    if not chat_id in games:
        games[chat_id] = {
            'players': [],
            'used_movies': [], 
            'current_letter': '',
            'is_active': False,
            'timer_task': None,
            'current_idx': 0
        }
    
    game = games[chat_id]

    # Check if already joined
    for p in game['players']:
        if p.id == user_id:
            await message.answer("⚠️ You are already in the game!")
            return

    game['players'].append(user)
    await message.answer(f"✅ {user.full_name} joined the game!")

@dp.message(Command("leave"))
async def cmd_leave(message: types.Message):
    chat_id = message.chat.id
    user = message.from_user
    
    game = get_game(chat_id)
    if not game:
        return

    # Check if user is in the game
    user_in_game = False
    for p in game['players']:
        if p.id == user.id:
            user_in_game = True
            break

    if not user_in_game:
        await message.answer("❌ You are not part of the game.")
        return

    # Remove player
    for i, p in enumerate(game['players']):
        if p.id == user.id:
            game['players'].pop(i)
            await message.answer(f"👋 {user.full_name} left the game.")
            
            # If it was their turn, move to next
            if game['is_active'] and game['current_idx'] == i:
                 game['current_idx'] = i - 1 # Logic adjustment in next_turn
                 await next_turn(chat_id)
            elif game['is_active'] and game['current_idx'] > i:
                 game['current_idx'] -= 1 # Shift index if someone before them left
            
            # Check win condition if empty
            if game['is_active'] and len(game['players']) < 2:
                await bot.send_message(chat_id, "Not enough players. Game stopped.")
                game['is_active'] = False
            return

@dp.message(Command("players"))
async def cmd_players(message: types.Message):
    game = get_game(message.chat.id)
    if not game or not game['players']:
        await message.answer("No players joined yet.")
        return
    
    # Added better formatting with newlines
    names = "\n".join([f"{i+1}. {p.full_name}" for i, p in enumerate(game['players'])])
    await message.answer(f"👥 <b>Current Players ({len(game['players'])}):</b>\n\n{names}")

@dp.message(Command("playgame"))
async def cmd_playgame(message: types.Message):
    chat_id = message.chat.id
    game = get_game(chat_id)
    
    if not game or len(game['players']) < 2:
        await message.answer("❌ Need at least 2 players to start! Use /join")
        return
    
    if game['is_active']:
        await message.answer("Game is already running!")
        return

    game['is_active'] = True
    game['used_movies'] = []
    game['current_letter'] = '' 
    
    await message.answer("🎲 <b>Game Started!</b>\nLet's pick who goes first...")
    
    random.shuffle(game['players'])
    game['current_idx'] = -1 
    
    await next_turn(chat_id)

@dp.message(Command("stopgame"))
async def cmd_stopgame(message: types.Message):
    chat_id = message.chat.id
    if chat_id in games:
        games[chat_id]['is_active'] = False
        if games[chat_id]['timer_task']:
            games[chat_id]['timer_task'].cancel()
        del games[chat_id]
        await message.answer("🛑 Game stopped.")
    else:
        await message.answer("No game running.")

# --- GAMEPLAY LOGIC ---

@dp.message()
async def handle_game_input(message: types.Message):
    chat_id = message.chat.id
    user = message.from_user
    text = message.text

    game = get_game(chat_id)
    
    if not game or not game['is_active']:
        return

    # Check if it is this user's turn
    current_player = game['players'][game['current_idx']]
    if user.id != current_player.id:
        return

    # Normalization logic: "golmaal" becomes "Golmaal" (for display)
    normalized_name = normalize_movie(text)
    
    # 1. Check if it's a valid movie from DB using SET (Case Insensitive)
    if text.strip().lower() not in MOVIE_SET:
        await message.reply("❌ Invalid or unknown movie. Try another.")
        return

    # 2. Check if already used (Compare normalized titles)
    if normalized_name in game['used_movies']:
        await message.reply("🔄 This movie was already used! Pick another.")
        return

    # 3. Check First Letter
    # We compare the first letter of normalized name (Title Case) vs current letter
    if game['current_letter']:
        if normalized_name[0] != game['current_letter']:
            await message.reply(f"🔤 Must start with letter <b>'{game['current_letter']}'</b>!")
            return

    # SUCCESSFUL TURN
    if game['timer_task']:
        game['timer_task'].cancel()

    game['used_movies'].append(normalized_name)
    last_char = get_last_letter(normalized_name)
    game['current_letter'] = last_char

    # Improved spacing for reply
    await message.reply(f"✅ <b>{normalized_name}</b> accepted!\n\nNext letter: <b>'{last_char}'</b>")

    await next_turn(chat_id)

# --- MAIN EXECUTION ---

async def main():
    import threading
    t = threading.Thread(target=run_flask)
    t.start()
    print("Bot started polling with 35s timer...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
