
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN, ADMIN_ID, BOT_NAME
from database import setup, add_user, count_users
from datetime import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id, user.username or "")

    await update.message.reply_text(
        f"سڵاو {user.first_name}!\n"
        f"بەخێربێیت بۆ {BOT_NAME} 🔥\n\n"
        "/help - یارمەتی\n"
        "/id - ناسنامە\n"
        "/info - زانیاری\n"
        "/time - کات"
    )

async def help_command(update: Update, context):
    await update.message.reply_text(
        "فەرمانەکانی بۆت:\n"
        "/start\n/help\n/id\n/info\n/time"
    )

async def get_id(update: Update, context):
    await update.message.reply_text(
        f"ناسنامەی تۆ: {update.effective_user.id}"
    )

async def info(update: Update, context):
    await update.message.reply_text(
        f"ناو: {BOT_NAME}\n"
        "وەشان: 1.0\n"
        "زمان: Python"
    )

async def get_time(update: Update, context):
    await update.message.reply_text(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

async def admin(update: Update, context):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("ڕێگەپێدراو نیت!")
        return

    await update.message.reply_text(
        f"بەخێربێیت ئەدمین!\n"
        f"ژمارەی بەکارهێنەران: {count_users()}"
    )

async def echo(update: Update, context):
    await update.message.reply_text(
        f"تۆ نووسیت: {update.message.text}"
    )

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    setup()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", get_id))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("time", get_time))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, echo
    ))

    print("SHBLOOD BOT IS RUNNING!")
    app.run_polling()

if __name__ == "__main__":
    main()
