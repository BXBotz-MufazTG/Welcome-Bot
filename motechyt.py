from telegram import Update
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
import os
import pickledb

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
    send_async(context, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)


def set_welcome(update, context):
    """ Sets custom welcome message """

    chat_id = update.message.chat.id

    # Check admin privilege and group context
    if not check(update, context):
        return

    # Split message into words and remove mentions of the bot
    message = update.message.text.partition(" ")[2]

    # Only continue if there's a message
    if not message:
        send_async(
            context,
            chat_id=chat_id,
            text="You need to send a message, too! For example:\n"
            "<code>/welcome Hello $username, welcome to "
            "$title!</code>",
            parse_mode=ParseMode.HTML,
        )
        return

    # Put message into database
    db.set(str(chat_id), message)

    send_async(context, chat_id=chat_id, text="Got it!")

  
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("welcome", set_welcome))
dp.add_handler(MessageHandler(Filters.status_update, empty_message))
dp.add_error_handler(error)

updater.start_polling()
updater.idle()
