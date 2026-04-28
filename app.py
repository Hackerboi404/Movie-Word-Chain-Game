import os
import random
import logging
import threading
import json
from flask import Flask, jsonify, request, abort
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, CallbackContext, Filters
from telegram.ext import Application

# --- CONFIGURATION ---
TOKEN = os.environ.get("TOKEN", "YOUR_BOT_TOKEN_HERE")  # Render env var prefer karega

app = Flask(__name__)

# --- SETUP TELEGRAM APPLICATION (v20+) ---
# V20 mein Application hi base hota hai
application = Application.builder().token(TOKEN).build()

# Dispatcher access (v20 style)
dispatcher = application.dispatcher

# --- GAME STATE ---
# Structure: { chat_id: { 'is_active': bool, 'round': int, 'current_q': (dialogue, movie), 'scores': {user_id: {'name': str, 'points': int}}, 'timer_lock': bool } }
game_state = {}

# --- IMPORT DIALOGUES ---
try:
    from dialogues import DIALOGUES
except ImportError:
    print("dialogues.py not found! Using dummy data.")
    DIALOGUES = [("Test dialogue", "Test Movie")]

# --- HELPER FUNCTIONS ---

def get_leaderboard_text(chat_id):
    if chat_id not in game_state:
        return "No game played yet."
    
    state = game_state[chat_id]
    scores = state['scores']
    
    if not scores:
        return "No scores yet!"

    # Sort users by score (descending)
    # scores dict: { user_id: {'name': 'Name', 'points': 10} }
    sorted_scores = sorted(scores.values(), key=lambda x: x['points'], reverse=True)
    
    text = "🏆 <b>FINAL LEADERBOARD</b> 🏆\n\n"
    rank = 1
    for user_data in sorted_scores:
        name = user_data['name']
        pts = user_data['points']
        text += f"{rank}. {name} - {pts} pts\n"
        rank += 1
        
    return text

def end_game(chat_id):
    if chat_id not in game_state:
        return

    # Mark game as inactive
    game_state[chat_id]['is_active'] = False
    
    # Send Leaderboard
    lb_text = get_leaderboard_text(chat_id)
    application.bot.send_message(chat_id=chat_id, text=lb_text, parse_mode='HTML')
    
    # Clean up memory
    del game_state[chat_id]

def send_next_question(chat_id):
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
    
    application.bot.send_message(chat_id=chat_id, text=msg, parse_mode='HTML')

    # Start Timer for this round (30 seconds)
    # Hum timer function ke andar check karenge ki kya answer mil gaya hai ya nahi
    # Agar round number badh gaya ho, matlab answer mil gaya tha.
    
    def timeout_handler():
        # Check if game is still active and round hasn't changed (meaning answer wasn't given)
        if chat_id in game_state and \
           game_state[chat_id]['is_active'] and \
           game_state[chat_id]['round'] == current_round:
            
            application.bot.send_message(chat_id=chat_id, text="⏰ Time's up! No one guessed it.\nNext round...")
            
            # Move to next round
            game_state[chat_id]['round'] += 1
            send_next_question(chat_id)

    # Schedule the timeout (30.0 seconds)
    t = threading.Timer(30.0, timeout_handler)
    t.start()


# --- COMMAND HANDLERS ---

def start_game(update: Update, context: CallbackContext):
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
        'scores': {} 
    }
    
    # Start First Question
    send_next_question(chat_id)

def help_cmd(update: Update, context: CallbackContext):
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

def handle_guess(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user = update.effective_user
    
    # Check if game is active in this chat
    if chat_id not in game_state or not game_state[chat_id]['is_active']:
        return

    guess = update.message.text.strip().lower()
    state = game_state[chat_id]
    correct_movie = state['current_q'][1].lower()

    # Logic: Agar guess correct movie mein hai ya correct movie guess mein hai
    if guess in correct_movie or correct_movie in guess:
        
        # Correct Answer!
        
        # 1. Update Round (This stops the timer automatically)
        state['round'] += 1
        
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
        send_next_question(chat_id)
    else:
        # Wrong answer, ignore (spam prevention)
        pass


# --- ERROR HANDLING ---
def error(update: Update, context: CallbackContext):
    logger = logging.getLogger(__name__)
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# --- ROUTES ---

@app.route('/')
def index():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string, application.bot)
        dispatcher.process_update(update)
        return jsonify({"status": "ok"})
    else:
        abort(403)

# --- SETUP ---
dispatcher.add_handler(CommandHandler("start", help_cmd))
dispatcher.add_handler(CommandHandler("playgame", start_game))
dispatcher.add_handler(CommandHandler("help", help_cmd))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_guess))

dispatcher.add_error_handler(error)

if __name__ == '__main__':
    # Run the app
    # Note: v20 doesn't use start_polling here, webhook is handled by route
    # Hum logging bhi on kar sakte hain
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
