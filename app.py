import os
import random
import time
import threading
import logging
import json
from flask import Flask, jsonify, request, abort
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, CallbackContext, Filters

# --- CONFIGURATION ---
TOKEN = "8790186660:AAHGbgtQ6biJG7CH3J-dtpcvGgdsuNFOgrw"  # Apna Token yahan daalein
# Note: Render wali setting mein environment variable use karna better hai: os.getenv("TOKEN")
# Local ke liye yahan paste kar sakte hain.

app = Flask(__name__)

# Initialize Bot
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# --- GAME STATE ---
# Structure: { chat_id: { 'is_active': bool, 'round': int, 'current_q': (dialogue, movie), 'timer_thread': None, 'scores': {user_id: int} } }
game_state = {}

# Import Dialogues
try:
    from dialogues import DIALOGUES
except ImportError:
    DIALOGUES = [("Default dialogue", "Default Movie")]
    print("dialogues.py not found!")

# --- HELPER FUNCTIONS ---

def get_leaderboard_text(chat_id):
    if chat_id not in game_state:
        return "No game played yet."
    
    scores = game_state[chat_id]['scores']
    if not scores:
        return "No scores yet!"

    # Sort users by score (descending)
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    
    text = "🏆 <b>FINAL LEADERBOARD</b> 🏆\n\n"
    rank = 1
    for user_id, score in sorted_scores:
        # Fetching username from dictionary if available or simple ID
        # In real app, you might need to fetch user details via API, but for simplicity we use ID
        # Or store user names in state. Let's assume we store names in scores.
        user_name = scores[user_id].get('name', f"User {user_id}") if isinstance(scores[user_id], dict) else f"User {user_id}"
        
        # Fix logic if scores dict stores just ints or dicts
        if isinstance(scores[user_id], dict):
            name = scores[user_id]['name']
            pts = scores[user_id]['points']
        else:
            name = f"User {user_id}"
            pts = score
            
        text += f"{rank}. {name} - {pts} pts\n"
        rank += 1
        
    return text

def end_game(chat_id):
    if chat_id not in game_state:
        return

    # Cancel timer if running
    if game_state[chat_id]['timer_thread'] and game_state[chat_id]['timer_thread'].is_alive():
        # We can't easily kill threads in Python, so we check a flag in the thread function
        game_state[chat_id]['is_active'] = False 
    
    game_state[chat_id]['is_active'] = False
    
    # Send Leaderboard
    lb_text = get_leaderboard_text(chat_id)
    bot.send_message(chat_id=chat_id, text=lb_text, parse_mode='HTML')
    
    # Clear state (optional, kept for history)
    # del game_state[chat_id]

def send_next_question(chat_id, context=None):
    if chat_id not in game_state or not game_state[chat_id]['is_active']:
        return

    state = game_state[chat_id]
    current_round = state['round']

    if current_round > 10:
        end_game(chat_id)
        return

    # Pick a random dialogue
    dialogue, movie = random.choice(DIALOGUES)
    state['current_q'] = (dialogue, movie)
    
    # Send Question
    msg = f"🎬 <b>Round {current_round}/10</b>\n\n"
    msg += f"🗣️ Dialogue: <i>\"{dialogue}\"</i>\n\n"
    msg += "Guess the Movie! 🧐"
    
    bot.send_message(chat_id=chat_id, text=msg, parse_mode='HTML')

    # Start Timer for this round
    # Note: Using a threading.Timer for the 30s check
    def timeout_handler():
        # Check if game is still active
        if chat_id in game_state and game_state[chat_id]['is_active'] and game_state[chat_id]['round'] == current_round:
            bot.send_message(chat_id=chat_id, text="⏰ Time's up! No one guessed it.\nNext round...")
            game_state[chat_id]['round'] += 1
            send_next_question(chat_id)

    # Schedule the timeout
    t = threading.Timer(30.0, timeout_handler)
    t.start()
    state['timer_thread'] = t


# --- COMMAND HANDLERS ---

def start_game(update, context):
    chat_id = update.effective_chat.id
    
    # Check if game is already running
    if chat_id in game_state and game_state[chat_id]['is_active']:
        context.bot.send_message(chat_id=chat_id, text="⚠️ Game is already running! Wait for it to finish.")
        return

    context.bot.send_message(chat_id=chat_id, text="🎮 <b>Bollywood Dialogue Quiz</b> Started!\n\n10 Rounds.\n30 Seconds per round.\nFirst correct answer gets +10 Points.", parse_mode='HTML')
    
    # Initialize Game State
    game_state[chat_id] = {
        'is_active': True,
        'round': 1,
        'current_q': None,
        'timer_thread': None,
        'scores': {} # user_id: {'name': str, 'points': int}
    }
    
    # Start First Question
    send_next_question(chat_id)

def help_cmd(update, context):
    text = (
        "<b>How to Play:</b>\n"
        "1. Type <code>/playgame</code> to start.\n"
        "2. I will send a Bollywood dialogue.\n"
        "3. Reply with the <b>Movie Name</b>.\n"
        "4. First correct answer = +10 Points.\n"
        "5. Game ends after 10 rounds."
    )
    update.message.reply_text(text, parse_mode='HTML')


# --- MESSAGE HANDLERS (GUESSING) ---

def handle_guess(update, context):
    chat_id = update.effective_chat.id
    user = update.effective_user
    
    # Check if game is active in this chat
    if chat_id not in game_state or not game_state[chat_id]['is_active']:
        return

    guess = update.message.text.strip().lower()
    state = game_state[chat_id]
    correct_movie = state['current_q'][1].lower()

    # Logic to check guess (Partial matching allowed, e.g. "dilwale" for "dilwale dulhania")
    # We check if the user's guess is contained in the correct movie name OR vice versa
    if guess in correct_movie or correct_movie in guess:
        
        # Correct Answer!
        
        # 1. Stop the timer for this round (by marking answer given or checking round change)
        # Since threads are hard to kill, we simply check inside the timeout handler if the round changed.
        
        # 2. Award Points
        user_id = user.id
        if user_id not in state['scores']:
            state['scores'][user_id] = {
                'name': user.first_name,
                'points': 0
            }
        
        state['scores'][user_id]['points'] += 10
        
        winner_name = user.first_name
        correct_answer_full = state['current_q'][1]
        
        # 3. Send Success Message
        reply = f"✅ <b>Correct!</b>\nAnswer: {correct_answer_full}\n\n🏆 +10 Points to {winner_name}"
        context.bot.send_message(chat_id=chat_id, text=reply, parse_mode='HTML')
        
        # 4. Move to next round
        state['round'] += 1
        send_next_question(chat_id)

    # else: Wrong answer, ignore to avoid spam


# --- ERROR HANDLING ---
def error(update, context):
    logger = logging.getLogger(__name__)
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# --- ROUTES ---

@app.route('/')
def index():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return jsonify({"status": "ok"})

# --- SETUP ---
dispatcher.add_handler(CommandHandler("start", help_cmd))
dispatcher.add_handler(CommandHandler("playgame", start_game))
dispatcher.add_handler(CommandHandler("help", help_cmd))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_guess))

dispatcher.add_error_handler(error)

if __name__ == '__main__':
    # Run the app
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
