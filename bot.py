import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 OpenRouter API Key
OPENROUTER_API_KEY = "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"
MODEL = "qwen/qwq-32b:free"  # বা অন্য যেকোনো মডেল

# 🤖 Telegram Bot Token
TELEGRAM_TOKEN = "7681539419:AAFzrTrwWW9Zqf11Am_NWXJqwueewR8a16Y"

logging.basicConfig(level=logging.INFO)

# 🌐 AI Request Function
def query_openrouter(user_prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://tasnimgpt.com",
        "X-Title": "Tohina AI",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response_json = res.json()
        return response_json['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 📥 Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # 🤖 পরিচয় দিলে উত্তর দিবে আলাদা
    if any(x in user_message.lower() for x in ["what's your name", "তোমার নাম", "who made you"]):
        response = "🤖 My name is Tohina AI. I was created by Ahmed Shariar."
    else:
        response = query_openrouter(user_message)

    await update.message.reply_text(response)

# ▶️ Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm Tohina AI. Ask me anything!")

# 🚀 Main Bot Runner
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()
