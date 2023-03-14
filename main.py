import pyrogram
import config
from pyrogram import filters

# ini buat namanin app nya
app = pyrogram.Client(
    ":kim:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

# ini buat start nya

@app.on_message(filters.command("mulai"))
async start chat_actions(_, message):
    await app.send_message(message.chat.id, "halo bang, makasih udah start bot ini awoakwoak")

print('dah jalan')
app.run()
