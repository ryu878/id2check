import telebot
from _config import *



# Replace with your bot token
BOT_TOKEN = tg_bot_token

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Hello! 👋 I'm here to help you identify the source of forwarded messages.\n\n"
        "Here's how to use me:\n"
        "1. Forward any message to this bot.\n"
        "2. I will tell you whether it was forwarded from a user, group, or channel.\n"
        "3. I will also provide the ID and other details of the source.\n\n"
        "Try forwarding a message now!"
    )

# Handle forwarded messages
@bot.message_handler(func=lambda message: message.forward_from or message.forward_from_chat)
def handle_forwarded_message(message):
    if message.forward_from:
        # If the message is forwarded from a user
        user_id = message.forward_from.id
        username = message.forward_from.username or "No username"
        bot.reply_to(
            message,
            f"The forwarded message is from a user.\n"
            f"User ID: `{user_id}`\n"
            f"Username: `{username}`",
            parse_mode="Markdown"
        )
    elif message.forward_from_chat:
        # If the message is forwarded from a group or channel
        forward_chat = message.forward_from_chat
        chat_type = "Channel" if forward_chat.type == "channel" else "Group"
        chat_id = forward_chat.id
        chat_title = forward_chat.title or "No title"
        bot.reply_to(
            message,
            f"The forwarded message is from a {chat_type}.\n"
            f"Chat ID: `{chat_id}`\n"
            f"Title: `{chat_title}`",
            parse_mode="Markdown"
        )
    else:
        bot.reply_to(message, "Could not identify the source of the forwarded message.")

# Start the bot
print("Bot is running...")
bot.infinity_polling()