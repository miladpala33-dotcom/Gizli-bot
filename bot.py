import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# این تابع جدید و امن تر برای دستور /start هست
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """وقتی کاربر دستور /start رو میزنه، این پیام رو براش میفرسته"""
    # این روش امن تری برای گرفتن اسم کاربره
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"سلام {user_name}!\n\nبه کافه دیجیتال Gizli خوش اومدی. من آماده‌ام تا سریع‌ترین اتصال رو برات فراهم کنم."
    )

def main() -> None:
    """ربات رو اجرا میکنه"""
    TOKEN = os.environ.get("BOT_TOKEN")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
