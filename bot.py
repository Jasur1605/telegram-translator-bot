from telethon import TelegramClient, events
from deep_translator import GoogleTranslator

api_id = 34643919
api_hash = "619adcbcff94ed62544183d03827871c"

source_channels = [
    "kunuzofficial",
    "test21212131"
]

target_group = "mygroup12321"

client = TelegramClient("session", api_id, api_hash)

translator = GoogleTranslator(source='auto', target='en')

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):

    print("New message detected")

    text = event.message.text

    if text:
        try:
            translated = translator.translate(text)
        except:
            translated = text
    else:
        translated = ""

if event.message.media:
    await client.send_file(
        target_group,
        event.message.media,
        caption=translated
    )
    
client.start()
client.run_until_disconnected()