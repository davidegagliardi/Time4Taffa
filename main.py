#!/usr/bin/env python

import logging
import time

from database import loadDB, checkUser, updateLanguage, getLanguage, delUser
from menu import generate_message
from daily import dailyMenu
import os
import schedule
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text("Hey! I'm TimeforTaffa, I'm gonna send you daily menu from Taffa restaurant")
    chat_id = update.message.chat_id
    print(chat_id)
    checkUser(update, chat_id)

def en(update, context):
    update.message.reply_text("Language switched to english 🇬🇧")
    chat_id = update.message.chat_id
    updateLanguage(update, chat_id, "en")
def fi(update, context):
    update.message.reply_text("Kieli vaihdettu suomeksi 🇫🇮")
    chat_id = update.message.chat_id
    updateLanguage(update, chat_id, "fi")
def sv(update, context):
    update.message.reply_text("Språket bytte till svenska 🇸🇪")
    chat_id = update.message.chat_id
    updateLanguage(update, chat_id, "sv")

def today(update, context):
    chat_id = update.message.chat_id
    update.message.reply_text(generate_message(chat_id))

def stop(update, context):
    chat_id = update.message.chat_id
    delUser(update, chat_id)
    update.message.reply_text('So long and thanks for all the fish!')

def about(update, context):
    update.message.reply_text('TimeForTaffa is a bot that allows you to receive daily update about Taffa\'s menu. It\'s developed by @davidegagliardi')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
def test():
    print("Qui")
def main():
    updater = Updater(os.environ['TOKEN'], use_context=True)
    # while True:
    #     HOUR = datetime.datetime.now().hour
    #     MINUTE = datetime.datetime.now().minute
    #     if HOUR == 18 and MINUTE == 34:
    #         dailyMenu()
    #     time.sleep(60)

    dp = updater.dispatcher

    #Commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("en", en))
    dp.add_handler(CommandHandler("fi", fi))
    dp.add_handler(CommandHandler("sv", sv))
    dp.add_handler(CommandHandler("today", today))
    dp.add_handler(CommandHandler("about", about))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    loadDB()
    main()