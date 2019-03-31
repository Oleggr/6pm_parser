import config
import os
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
from parser import *

# import telebot
# from telebot import types


TOKEN = config.token
MONITORING_TOKEN = config.monitoring_bot_token
MY_ID = config.oleggr_id


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    try:
        keyboard = [["/get"]]

        rep_mark = ReplyKeyboardMarkup(keyboard, resize_keyboard = True)

        bot.sendMessage(update.message.chat.id, 'Hi!', reply_markup = rep_mark)

        #update.message.reply_text('Please choose:', reply_markup=reply_markup)

        command = 'curl -s -X POST ' \
                + 'https://api.telegram.org/bot' \
                + MONITORING_TOKEN \
                + '/sendMessage -d chat_id=' \
                + MY_ID \
                + ' -d text=\"'+ str(update.message.chat.id) + ' started sales bot\"'

        os.system(command)

    except Exception as e:

        #string_to_send = 'Problem%20in%20start%20command'
        command = 'curl -s -X POST ' \
                + 'https://api.telegram.org/bot' \
                + MONITORING_TOKEN \
                + '/sendMessage -d chat_id=' \
                + MY_ID \
                + ' -d text=\"'+ str(update.message.chat.id) + ' failed in starting sales bot\"'

        os.system(command)

        #print('EXCEPTION 1: ', e)

def get(bot, update):
    try:
        replyes = parse(get_html(URL))
        message = '*Here is what I found:*\n\n#'

        for replye in replyes:
            #print(replye)
            message += replye

    #for reply in replyes:
    #    message =+ reply + '\n'
    #print(update.message.chat.id)
    #update.message.reply_text(message)
        bot.sendMessage(update.message.chat.id, message, parse_mode="markdown")

    except Exception as e:

        #string_to_send = 'Problem%20in%20getting%20data%20or%20in%20sending%20message'

        #monitoring_url = 'https://api.telegram.org/bot' \
         #       + MONITORING_TOKEN \
          #      + '/sendMessage?chat_id=' \
           #     + MY_ID \
            #    + '&text=' \
             #   + string_to_send

        command = 'curl -s -X POST ' \
                + 'https://api.telegram.org/bot' \
                + MONITORING_TOKEN \
                + '/sendMessage -d chat_id=' \
                + MY_ID \
                + ' -d text=\"FAIL: Getting info for '+ str(update.message.chat.id) + '\'s request failed\"'

        os.system(command)

        bot.sendMessage(update.message.chat.id, 
                        '*Error*\nGathering information gone wrong, try again later',
                        parse_mode="markdown")

        #TODO add logging

        print('EXCEPTION 2: ', e)

def main():
    """Run bot."""
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get", get))

    try:
        # Start the Bot
        updater.start_polling()
    except Exception as e:

        command = 'curl -s -X POST ' \
                + 'https://api.telegram.org/bot' \
                + MONITORING_TOKEN \
                + '/sendMessage -d chat_id=' \
                + MY_ID \
                + ' -d text=\"Polling of @DiscountNotificator_bot fucked up\"'


        os.system(command)

        #print('EXCEPTION 3: ', e)

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
