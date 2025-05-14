import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    keyboard = [[
        InlineKeyboardButton(
            "🎮 Play Game", 
            web_app=WebAppInfo(url="https://yourusername.neocities.org")
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('গেম খেলতে বাটনে ক্লিক করুন:', reply_markup=reply_markup)

def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
