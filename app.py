import asyncio
import logging
import os
import random
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
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
from data import MOVIES, is_valid_movie

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

games = {}

# --- HELPER FUNCTIONS ---

def get_game(chat_id):
    return games.get(chat_id)

def clean_string(text):
    import re
    return re.sub(r'[^a-zA-Z]', '', text).lower()

def get_last_letter(movie_name):
    cleaned = clean_string(movie_name)
    if not cleaned:
        return None
    return cleaned[-1].upper()

async def next_turn(chat_id):
    game = get_game(chat_id)
    if not game or not game['is_active']:
        return

    if len(game['players']) == 1:
        winner = game['players'][0]
        await bot.send_message(chat_id, f"🏆 <b>GAME OVER!</b>\n\n👑 Winner: {winner.mention_html()}\n\nCongratulations!")
        del games[chat_id]
        return

    game['current_idx'] = (game['current_idx'] + 1) % len(game['players'])
    current_player = game['players'][game['current_idx']]

    game['current_letter'] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') if game['current_letter'] == '' else game['current_letter']
    
    msg = f"🎬 <b>{current_player.full_name}'s Turn!</b>\n"
    msg += f"🔤 Send a movie starting with: <b>'{game['current_letter']}'</b>"
    
    await bot.send_message(chat_id, msg)

    if game['timer_task']:
        game['timer_task'].cancel()
    
    game['timer_task'] = asyncio.create_task(check_timeout(chat_id, game['current_idx'], 35))


async def check_timeout(chat_id, expected_player_idx, timeout_seconds):
    await asyncio.sleep(timeout_seconds)
    
    game = get_game(chat_id)
    if game and game['is_active'] and game['current_idx'] == expected_player_idx:
        eliminated_player = game['players'].pop(expected_player_idx)
        await bot.send_message(chat_id, f"⏱️ <b>Time's Up!</b>\n😢 {eliminated_player.mention_html()} eliminated!")
        
        game['current_idx'] = expected_player_idx - 1 
        await next_turn(chat_id)

# --- HANDLERS ---

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "🎬 <b>Movie Word Chain Game</b>\n\n"
        "📜 <b>Rules:</b>\n"
        "1. Join with /join\n"
        "2. Start game with /playgame\n"
        "3. Send a movie name starting with the last letter of the previous movie.\n"
        "4. Valid movies only.\n"
        "5. 35 seconds per turn.\n\n"
        "Commands:\n"
        "/join - Join game\n"
        "/leave - Leave game\n"
        "/players - See players\n"
        "/playgame - Start\n"
        "/stopgame - Stop"
    )
    await message.answer(text)

@dp.message(Command("join"))
async def cmd_join(message: types.Message):
    chat_id = message.chat.id
    user = message.from_user

    if chat_id not in games:
        games[chat_id] = {
            'players': [],
            'used_movies': [],
            'current_letter': '',
            'is_active': False,
            'timer_task': None,
            'current_idx': 0
        }
    
    game = games[chat_id]

    for p in game['players']:
        if p.id == user.id:
            await message.answer("⚠️ Already joined!")
            return

    game['players'].append(user)
    await message.answer(f"✅ {user.full_name} joined!")

@dp.message(Command("leave"))
async def cmd_leave(message: types.Message):
    chat_id = message.chat.id
    user = message.from_user
    
    game = get_game(chat_id)
    if not game:
        return

    for i, p in enumerate(game['players']):
        if p.id == user.id:
            game['players'].pop(i)
            await message.answer(f"👋 {user.full_name} left.")
            
            if game['is_active'] and game['current_idx'] == i:
                 game['current_idx'] = i - 1
                 await next_turn(chat_id)
            elif game['is_active'] and game['current_idx'] > i:
                 game['current_idx'] -= 1
            
            if game['is_active'] and len(game['players']) < 2:
                await bot.send_message(chat_id, "Not enough players. Game stopped.")
                game['is_active'] = False
            return

@dp.message(Command("players"))
async def cmd_players(message: types.Message):
    game = get_game(message.chat.id)
    if not game or not game['players']:
        await message.answer("No players.")
        return
    
    names = "\n".join([f"{i+1}. {p.full_name}" for i, p in enumerate(game['players'])])
    await message.answer(f"👥 Players:\n\n{names}")

@dp.message(Command("playgame"))
async def cmd_playgame(message: types.Message):
    chat_id = message.chat.id
    game = get_game(chat_id)
    
    if not game or len(game['players']) < 2:
        await message.answer("❌ Need 2+ players!")
        return
    
    if game['is_active']:
        await message.answer("Already running!")
        return

    game['is_active'] = True
    game['used_movies'] = []
    game['current_letter'] = ''
    
    await message.answer("🎲 Game Started!")
    
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

# --- GAMEPLAY ---

@dp.message()
async def handle_game_input(message: types.Message):
    chat_id = message.chat.id
    user = message.from_user
    text = message.text

    game = get_game(chat_id)
    
    if not game or not game['is_active']:
        return

    current_player = game['players'][game['current_idx']]
    if user.id != current_player.id:
        return

    cleaned_name = text.strip()
    normalized_name = cleaned_name.lower()

    if not is_valid_movie(normalized_name):
        await message.reply("❌ Invalid movie.")
        return

    if normalized_name in game['used_movies']:
        await message.reply("🔄 Already used!")
        return

    if game['current_letter']:
        if cleaned_name[0].upper() != game['current_letter']:
            await message.reply(f"🔤 Must start with '{game['current_letter']}'")
            return

    if game['timer_task']:
        game['timer_task'].cancel()

    game['used_movies'].append(normalized_name)
    last_char = get_last_letter(cleaned_name)
    game['current_letter'] = last_char

    await message.reply(f"✅ {cleaned_name}\nNext: '{last_char}'")

    await next_turn(chat_id)

# --- MAIN ---

async def main():
    import threading
    t = threading.Thread(target=run_flask)
    t.start()

    print("Bot running...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
