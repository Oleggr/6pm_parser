import config

from telegram.ext import Updater, CommandHandler
from parser import *

# import telebot
# from telebot import types


TOKEN = config.token


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):

    replye = parse(get_html_from_file())

    message = 'Hi, here is what I found:\n{}'.format(replye)    
    
    #for reply in replyes:
    #    message =+ reply + '\n'

    update.message.reply_text(message)        


def main():
    """Run bot."""
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
