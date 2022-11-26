from telethon import TelegramClient, events, sync
api_id = 3595783
api_hash = "13d72cc0cb8f2bf82cceaa205b808360"
client = TelegramClient("w1ke", api_id, api_hash)
@client.on(events.NewMessage(pattern=".help"))
async def _(event):
  await event.edit("AnnotationX userbot help menyusi .ha - ashi .ashi >
@client.on(events.NewMessage(pattern=".ashi"))
async def _(event):
  await event.edit("ha")
@client.on(events.NewMessage(pattern=".ha"))
async def _(event):
  await event.edit("ashi")


client.start()
client.run_until_disconnected()
