import telebot
from _config import *



# Replace with your bot token
BOT_TOKEN = tg_bot_token

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: message.forward_from_chat is not None)
def handle_forwarded_message(message):
    forward_chat = message.forward_from_chat
    if forward_chat:
        chat_type = "Channel" if forward_chat.type == "channel" else "Group"
        chat_id = forward_chat.id
        bot.reply_to(
            message,
            f"The forwarded message is from a {chat_type}.\nChat ID: `{chat_id}`",
            parse_mode="Markdown"
        )
    else:
        bot.reply_to(message, "Could not identify the source of the forwarded message.")

# Start the bot
print("Bot is running...")
bot.infinity_polling()