import asyncio
import logging
import os
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from flask import Flask

# --- CONFIGURATION ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    print("Error: BOT_TOKEN not found in environment variables.")
    exit(1)

# --- DATA IMPORT ---
from data import MOVIES, is_valid_movie

# --- FLASK ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, use_reloader=False)

# --- BOT ---
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

games = {}

# --- HELPERS ---
def get_game(chat_id):
    return games.get(chat_id)

def clean_string(text):
    import re
    return re.sub(r'[^a-zA-Z]', '', text).lower()

def get_last_letter(movie_name):
    cleaned = clean_string(movie_name)
    return cleaned[-1].upper() if cleaned else None

# --- GAME LOGIC ---
async def next_turn(chat_id):
    game = get_game(chat_id)
    if not game or not game['is_active']:
        return

    if len(game['players']) == 1:
        winner = game['players'][0]
        await bot.send_message(chat_id, f"🏆 Winner: {winner.mention_html()}")
        del games[chat_id]
        return

    game['current_idx'] = (game['current_idx'] + 1) % len(game['players'])
    player = game['players'][game['current_idx']]

    if game['current_letter'] == '':
        game['current_letter'] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    await bot.send_message(
        chat_id,
        f"🎬 {player.full_name}'s Turn\n🔤 Letter: <b>{game['current_letter']}</b>"
    )

    if game['timer_task']:
        game['timer_task'].cancel()

    game['timer_task'] = asyncio.create_task(check_timeout(chat_id, game['current_idx'], 35))


async def check_timeout(chat_id, idx, time):
    await asyncio.sleep(time)
    game = get_game(chat_id)

    if game and game['is_active'] and game['current_idx'] == idx:
        out = game['players'].pop(idx)
        await bot.send_message(chat_id, f"⏱️ {out.full_name} out!")

        game['current_idx'] = idx - 1
        await next_turn(chat_id)

# --- COMMANDS ---

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer(
        "🎬 Movie Game\n\n"
        "Use:\n"
        "/join\n"
        "/playgame\n"
        "/leave\n"
        "/players\n"
        "/stopgame"
    )

@dp.message(Command("join"))
async def join(msg: types.Message):
    chat = msg.chat.id
    user = msg.from_user

    if chat not in games:
        games[chat] = {
            'players': [],
            'used_movies': [],
            'current_letter': '',
            'is_active': False,
            'timer_task': None,
            'current_idx': 0
        }

    game = games[chat]

    if any(p.id == user.id for p in game['players']):
        await msg.answer("Already joined")
        return

    game['players'].append(user)
    await msg.answer(f"✅ {user.full_name} joined")

# ✅ FIXED PART HERE
@dp.message(Command("playgame"))
async def play(msg: types.Message):
    chat = msg.chat.id
    game = get_game(chat)

    # if no game created yet
    if not game:
        await msg.answer(
            "❌ <b>No players yet!</b>\n\n"
            "👉 Use /join to join the game\n"
            "👥 Minimum players required: 2"
        )
        return

    # if less than 2 players
    if len(game['players']) < 2:
        await msg.answer(
            "❌ <b>Not enough players!</b>\n\n"
            "👉 Ask others to /join\n"
            "👥 Minimum players required: 2"
        )
        return

    if game['is_active']:
        await msg.answer("Game already running")
        return

    game['is_active'] = True
    game['used_movies'] = []
    game['current_letter'] = ''

    random.shuffle(game['players'])
    game['current_idx'] = -1

    await msg.answer("🎲 Game Started!")
    await next_turn(chat)

@dp.message(Command("players"))
async def players(msg: types.Message):
    game = get_game(msg.chat.id)
    if not game or not game['players']:
        await msg.answer("No players")
        return

    text = "\n".join([p.full_name for p in game['players']])
    await msg.answer(text)

@dp.message(Command("leave"))
async def leave(msg: types.Message):
    game = get_game(msg.chat.id)
    if not game:
        return

    game['players'] = [p for p in game['players'] if p.id != msg.from_user.id]
    await msg.answer("Left game")

@dp.message(Command("stopgame"))
async def stop(msg: types.Message):
    if msg.chat.id in games:
        del games[msg.chat.id]
        await msg.answer("Game stopped")

# --- GAME INPUT ---
@dp.message()
async def game(msg: types.Message):
    game = get_game(msg.chat.id)
    if not game or not game['is_active']:
        return

    player = game['players'][game['current_idx']]
    if msg.from_user.id != player.id:
        return

    name = msg.text.strip()
    norm = name.lower()

    if not is_valid_movie(norm):
        await msg.reply("Invalid movie")
        return

    if norm in game['used_movies']:
        await msg.reply("Already used")
        return

    if game['current_letter']:
        if name[0].upper() != game['current_letter']:
            await msg.reply(f"Use letter {game['current_letter']}")
            return

    if game['timer_task']:
        game['timer_task'].cancel()

    game['used_movies'].append(norm)
    last = get_last_letter(name)
    game['current_letter'] = last

    await msg.reply(f"✅ {name}\nNext: {last}")
    await next_turn(msg.chat.id)

# --- MAIN ---
async def main():
    import threading
    threading.Thread(target=run_flask).start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
