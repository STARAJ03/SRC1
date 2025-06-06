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
import logging
from config import API_ID, API_HASH, BOT_TOKEN, STRING
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize clients
client = TelegramClient("telethonbot", API_ID, API_HASH)
app = Client("pyrogrambot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
userbot = Client("4gbbot", api_id=API_ID, api_hash=API_HASH, session_string=STRING)

async def start_client():
    """Initialize and start all clients"""
    try:
        # Start Telethon client
        if not client.is_connected():
            await client.start(bot_token=BOT_TOKEN)
            print("✅ Telethon client started")
    except Exception as e:
        print(f"❌ Failed to start Telethon client: {e}")
        sys.exit(1)

    try:
        # Start Pyrogram bot
        await app.start()
        print("✅ Pyrogram bot started")
    except Exception as e:
        print(f"❌ Failed to start Pyrogram bot: {e}")
        sys.exit(1)

    try:
        # Start Userbot
        await userbot.start()
        print("✅ Userbot started")
    except Exception as e:
        print(f"❌ Failed to start userbot: {e}")
        sys.exit(1)

    return client, app, userbot

async def stop_client():
    """Stop all clients gracefully"""
    try:
        await client.disconnect()
        await app.stop()
        await userbot.stop()
        logger.info("✅ All clients stopped successfully")
    except Exception as e:
        logger.error(f"❌ Error stopping clients: {e}")
        raise
