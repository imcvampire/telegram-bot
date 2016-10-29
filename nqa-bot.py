import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, InlineQueryHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
from emoji import emojize

from config import Config

updater = Updater(token=Config.BOT_TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s \
                    - %(levelname)s - %(message)s', level=logging.INFO)

def hi(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Hi. I\'m a stupid bot. Don\'t talk with me')

def ping(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Pong %s" % emojize(":thumbsup:", use_aliases=True))


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def stfu(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='STFU!!!!!')

def register_handler(command, func):
    dispatcher.add_handler(CommandHandler(command, func))

def main():
    register_handler('hi', hi)
    register_handler('ping', ping)
    register_handler('echo', echo)
    register_handler('stfu', stfu)

    updater.start_polling()

if __name__ == '__main__':
    main()
