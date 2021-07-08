from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
import os

Token =os.environ.get("MT_BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

START_MESSAGE = """Hi {}, {}"""

HELP_TEXT = "HI"

def start(updater,context):
 first_name = update.effective_user.first_name
     if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_STRINGS)

            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, False)
                else:
                    send_settings(match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name
            update.effective_message.reply_photo(DEVIL_IMG,PM_START_TEXT.format(escape_markdown(first_name), escape_markdown(bot.first_name), OWNER_NAME, OWNER_USERNAME ),reply_markup=InlineKeyboardMarkup(
                                                [[InlineKeyboardButton(text=" 👥 channel.",url="https://telegram.dog/Mai_bOTs")],  
                                                [InlineKeyboardButton(text="Creater",url="https://t.me/No_OnE_Kn0wS_Me"),InlineKeyboardButton(text="Mai Source",url="https://github.com/No-OnE-Kn0wS-Me/Filterbot")]]),disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)
    else:

def help(updater,context):
 updater.message.reply_text(
                            "{}".format(HELP_TEXT),
                            reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton(text="How To Own", url="https://t.me/Mrk_yt")], [InlineKeyboardButton(text="Join", url="t.me/PR0FESS0R_99")]]),
                            disable_web_page_preview=True,
                            parse_mode=ParseMode.MARKDOWN)
                           
 

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
