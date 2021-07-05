import os
from pyrogram import Client, filters

Motechyt = Client(
            "MT ID BOT",
            bot_token = os.environ["BOT_TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"]
)

@Motechyt.on_message(filters.private & filters.command("start"))
async def start(bot, update):  
    text = f"""
<b> 👋Hello {update.from_user.mention}</b>
<b>I CAN GET ANY PUBLIC AND PRIVATE CHANNEL ID
FORWARD A MESSAGE FROM YOUR CHANNEL TO GET YOUR CHANNEL ID.
CLICK /ID GET YOUR ID
CLICK /INFO GET YOUR TELEGRAM INFO </b>
"""
    await update.reply_text(
        text=text,
        disable_web_page_preview=True
  )

@Motechyt.on_message(filters.text & filters.group & ~filters.bot)
async def add_group(bot, update):
      text = """Hi"""
      await update.reply_text(        
        text=text,
        disable_web_page_preview=True
    )

Motechyt.run()
