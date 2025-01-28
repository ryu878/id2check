import telebot
from datetime import datetime, timedelta
import time
from _config import *


name = 'id2check'
ver = '280125'

BOT_TOKEN = tg_bot_token

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Dictionary to store user access timestamps
user_last_access = {}

# Dictionary to store banned users with unban timestamps
banned_users = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Hello! 👋 I'm here to help you identify the source of forwarded messages.\n\n"
        "You can forward any message to me, but please don't spam—requests are limited to one every 5 seconds.\n\n"
        'Try forwarding a message now!'
    )

@bot.message_handler(func=lambda message: True)
def handle_request(message):
    user_id = message.from_user.id
    chat_id = message.chat.id  # This will get the chat ID

    # Check if the user is banned
    if user_id in banned_users:
        unban_time = banned_users[user_id]
        if datetime.now() < unban_time:
            bot.reply_to(message, f'You are banned for exceeding the request limit. Try again later.')
            return
        else:
            # Unban the user after the ban duration has passed
            del banned_users[user_id]

    # Check rate limit
    current_time = time.time()
    if user_id in user_last_access:
        last_access_time = user_last_access[user_id]
        if current_time - last_access_time < RATE_LIMIT_SECONDS:
            # Ban the user
            banned_users[user_id] = datetime.now() + timedelta(hours=BAN_DURATION_HOURS)
            bot.reply_to(
                message,
                f'You exceeded the request rate limit. You are banned for 24 hours.'
            )
            return

    # Update last access time
    user_last_access[user_id] = current_time

    # Handle forwarded messages
    if message.forward_from:
        user_id = message.forward_from.id
        username = message.forward_from.username or 'No username'
        bot.reply_to(
            message,
            f'The forwarded message is from a user.\n'
            f"User ID: `{user_id}`\n"
            f"Username: `{username}`\n"
            f"Message sent from chat ID: `{chat_id}`",
            parse_mode='Markdown'
        )
    elif message.forward_from_chat:
        forward_chat = message.forward_from_chat
        chat_type = 'Channel' if forward_chat.type == 'channel' else 'Group'
        chat_id = forward_chat.id
        chat_title = forward_chat.title or 'No title'
        bot.reply_to(
            message,
            f'The forwarded message is from a {chat_type}.\n'
            f"Chat ID: `{chat_id}`\n"
            f"Title: `{chat_title}`\n"
            f"Message sent from chat ID: `{chat_id}`",
            parse_mode='Markdown'
        )
    else:
        bot.reply_to(message, f'Could not identify the source of the forwarded message.')

# Start the bot
print(f' {name} ver: {ver}\n is running...')
bot.polling()