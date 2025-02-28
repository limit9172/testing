import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7843842319:AAHj34cuZ_Z06lX4t-w9IS7XrTxttCnYOmc"  
CHAT_ID_OWNER = 6786210993  
PHISHING_LINK = "https://your-phishing-site.com"  


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

def start(update: Update, context: CallbackContext) -> None:
    """Kirim link phishing hanya ke pemilik bot"""
    if update.message.chat_id == CHAT_ID_OWNER:
        update.message.reply_text(f"Halo bos, ini link lo: {PHISHING_LINK}")
    else:
        update.message.reply_text("⚠️ Maaf, lo gak punya akses ke bot ini.")

def main():
    """Jalankan bot"""
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
