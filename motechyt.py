from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
import os

Token =os.environ.get("MT_BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

START_MESSAGE = """Hi"""

HELP_TEXT = "HI"

def start(updater,context):
 updater.message.reply_text(
                            '''{}'''.format(START_MESSAGE),
                           reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton(text=" 👥 channel.",url="https://telegram.dog/Mai_bOTs")],  
                           [InlineKeyboardButton(text="Creater",url="https://t.me/No_OnE_Kn0wS_Me"),InlineKeyboardButton(text="Mai Source",url="https://github.com/No-OnE-Kn0wS-Me/Filterbot")]]),
                            disable_web_page_preview=True,
                            parse_mode=ParseMode.MARKDOWN)
   

def help(updater,context):
 updater.message.reply_text(
                            "{}".format(HELP_TEXT),
                            replay_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton(text="How To Own", url="https://t.me/Mrk_yt")], [InlineKeyboardButton(text="Join", url="t.me/PR0FESS0R_99")]]),
                            disable_web_page_previwe=True,
                            prase_mode=PraseMode.MARKDOWN)
                           
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'👋Hello {member.full_name} , Welcome to ln Support\n\n💖Thank💖You💖For💖Joining💖')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
