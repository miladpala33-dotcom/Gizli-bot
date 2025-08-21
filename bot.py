
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# این تابع برای دستور /start هست
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """وقتی کاربر دستور /start رو میزنه، این پیام رو براش میفرسته"""
    user = update.effective_user
    await update.message.reply_html(
        f"سلام {user.mention_html()}!\n\nبه کافه دیجیتال Gizli خوش اومدی. من آماده‌ام تا سریع‌ترین اتصال رو برات فراهم کنم.",
    )

def main() -> None:
    """ربات رو اجرا میکنه"""
    # توکن ربات رو از یه جای امن میخونه که بعدا تنظیمش میکنیم
    TOKEN = os.environ.get("BOT_TOKEN")

    # ساخت اپلیکیشن ربات
    application = Application.builder().token(TOKEN).build()

    # ثبت کردن دستور /start
    application.add_handler(CommandHandler("start", start))

    # شروع به کار ربات
    application.run_polling()

if __name__ == "__main__":
    main()
