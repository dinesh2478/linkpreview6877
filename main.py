from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = "26758684"
API_HASH = "7296d2b5945a5a8b73555f24bbb1418e"
BOT_TOKEN = "7299358803:AAGOFJgNV05eG5NEIlnzMuFBhE0iEOiA3Hk"

linkpreview6877_bot = Client(
    name="linkpreview6877_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_BUTTONS = [[
    InlinekeyboardButton("JOIN MY CHANNEL", url="https://t.me/myfavideo7")
]]

@linkpreview6877_bot.on_message.(filters.commands("start"))
async def start_cmd(client, message):
    await message.reply_text("hai this is an advanced bot you have join my channel to use me"
    reply_markup=InlinekeyboardMarkup(START_BUTTONS)
    )
    

    
    @linkpreview6877_bot.on_message.(filters.commands("start"))
async def help_cmd(client, message):
    await message.reply_text("all admin permission")

print("Bot was started")

linkpreview6877_bot.run()
