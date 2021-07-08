from telegram import Update
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, TelegramError, Update
import os
import pickledb
from telegram.ext.dispatcher import run_async
from html import escape

Token =os.environ.get("MT_BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

db = pickledb.load("bot.db", True)

if not db.get("chats"):
    db.set("chats", [])


START_MESSAGE = """Hi"""


def start(updater,context):
 updater.message.reply_text("{}".format(START_MESSAGE))

def welcome(update, context, new_member):
    """ Welcomes a user to the chat """

    message = update.message
    chat_id = message.chat.id
    logger.info(
        "%s joined to chat %d (%s)",
        escape(new_member.first_name),
        chat_id,
        escape(message.chat.title),
    )

    # Pull the custom message for this chat from the database
    text = db.get(str(chat_id))

    # Use default message if there's no custom one set
    if text is None:
        text = "Hello $username! Welcome to $title 😊"

    # Replace placeholders and send message
    text = text.replace("$username", new_member.first_name)
    text = text.replace("$title", message.chat.title)
    


welcome_handle = MessageHandler(Filters.status_update.new_chat_members, welcome)
updater.dispatcher.add_handler(welcome_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',set_welcome))

updater.start_polling()
updater.idle()
