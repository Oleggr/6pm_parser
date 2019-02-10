import config

from telegram.ext import Updater, CommandHandler
from parser import *

# import telebot
# from telebot import types


TOKEN = config.token


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi! Use /get to get info about discount')


def get_discount(bot, update):

    chat_id = update.message.chat_id
    replyes = parse(get_html_from_file())

    update.message.reply_text('We working')
    
    for reply in replyes:

        bot.send_message(
                chat_id, 
                text=reply, 
                parse_mode=telegram.ParseMode.MARKDOWN
                )


def main():
    """Run bot."""
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get", get_discount))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()