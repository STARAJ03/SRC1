# # Copyright (c) 2025 devgagan : https://github.com/Shivaay20005.  
# # Licensed under the GNU General Public License v3.0.  
# # See LICENSE file in the repository root for full license text.

# from telethon import TelegramClient
# from config import API_ID, API_HASH, BOT_TOKEN, STRING
# from pyrogram import Client
# import sys

# client = TelegramClient("telethonbot", API_ID, API_HASH)
# app = Client("pyrogrambot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
# userbot = Client("4gbbot", api_id=API_ID, api_hash=API_HASH, session_string=STRING)

# async def start_client():
#     if not client.is_connected():
#         await client.start(bot_token=BOT_TOKEN)
#         print("Shivaay_ started...")
#     if STRING:
#         try:
#             await userbot.start()
#             print("Userbot started...")
#         except Exception as e:
#             print(f"Hey honey!! check your premium string session, it may be invalid of expire {e}")
#             sys.exit(1)
#     await app.start()
#     print("Pyro App Started...")
#     return client, app, userbot















# shared_client.py

from telethon import TelegramClient
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, STRING
import sys

# Initialize clients globally to reuse across your app
client = TelegramClient("telethonbot", API_ID, API_HASH)
app = Client("pyrogrambot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
userbot = Client("4gbbot", api_id=API_ID, api_hash=API_HASH, session_string=STRING) if STRING else None

async def start_client():
    try:
        # Start Telethon bot client
        await client.start(bot_token=BOT_TOKEN)
        print("Shivaay_ Telethon client started...")
    except Exception as e:
        print(f"Error starting Telethon client: {e}")
        sys.exit(1)

    if userbot:
        try:
            await userbot.start()
            print("Userbot started...")
        except Exception as e:
            print(f"Invalid or expired userbot string session: {e}")
            sys.exit(1)

    try:
        await app.start()
        print("Pyrogram bot started...")
    except Exception as e:
        print(f"Error starting Pyrogram bot: {e}")
        sys.exit(1)

    return client, app, userbot
