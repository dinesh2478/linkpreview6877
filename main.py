from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = "29721671"
API_HASH = "dcff48c9ff5ff7b54990a3fb09499308"
BOT_TOKEN = "7522778102:AAE_H1lfrXglY6_6YpAP2S4L0Ziwztu3W4g"

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

Preview07_bot.run()
