from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("MT_BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''👋Hi Bro or Sis Iam Welcome Messanger bot\n\n👤Any Doubt - @Mo_Tech_YT\n🔊Bot Updates - @Mo_Tech_YT\n\n😮More Details Clcik /help Button''')

def help(updater,context):
 updater.message.reply_text("👇English👇\n\n⚕️Add ME TO YOUR GROUP\n⚕️MAKE ME AS ADMIN ON GROUP\n\n👇Malayalam👇\n\n⚕️ആദ്യം എന്നെ നിങ്ങളുടെ ഗ്രൂപ്പിൽ ആഡ് ആകൂ\n⚕️എന്നെ നിങളുടെ ഗ്രൂപ്പിൽ അഡ്മിൻ ആകൂ\n\n🖥️HOW TO OWN🖥️\nhttps://youtu.be/0a5nnEj5BjY")
 

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
