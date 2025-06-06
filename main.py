# Copyright (c) 2025 devgagan : https://github.com/Shivaay20005.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import asyncio
import os
import sys
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from config import (
    API_ID, 
    API_HASH, 
    BOT_TOKEN, 
    STRING, 
    LOG_GROUP,
    FORCE_SUB,
    FREEMIUM_LIMIT,
    PREMIUM_LIMIT
)
from utils.func import is_premium_user, get_user_data, save_user_data

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Initialize user client
user = Client(
    "user",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING
)

# Start command
@bot.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    try:
        user_id = message.from_user.id
        user_data = await get_user_data(user_id)
        
        if not user_data:
            await save_user_data(user_id, {
                "first_name": message.from_user.first_name,
                "username": message.from_user.username,
                "join_date": message.date
            })
        
        welcome_text = (
            f"👋 Hello {message.from_user.mention}!\n\n"
            "I'm a powerful downloader bot that can help you download:\n"
            "• YouTube videos\n"
            "• Instagram posts\n"
            "• And more!\n\n"
            "Use /help to see all available commands."
        )
        
        await message.reply_text(welcome_text)
        
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        await message.reply_text("❌ An error occurred. Please try again later.")

# Help command
@bot.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    help_text = (
        "📚 **Available Commands:**\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/ytdl <url> - Download YouTube video\n"
        "/batch - Start batch download\n"
        "/login - Login to account\n"
        "/premium - Check premium status\n\n"
        "For more help, contact @Shivaay20005"
    )
    await message.reply_text(help_text)

# Premium check command
@bot.on_message(filters.command("premium"))
async def premium_command(client: Client, message: Message):
    try:
        user_id = message.from_user.id
        is_premium = await is_premium_user(user_id)
        
        if is_premium:
            await message.reply_text(
                "🌟 You are a premium user!\n"
                f"Your download limit is {PREMIUM_LIMIT} files per day."
            )
        else:
            await message.reply_text(
                "📌 You are using the free version.\n"
                f"Your download limit is {FREEMIUM_LIMIT} files per day.\n\n"
                "Upgrade to premium for more features!"
            )
            
    except Exception as e:
        logger.error(f"Error in premium command: {e}")
        await message.reply_text("❌ An error occurred. Please try again later.")

async def main():
    try:
        # Start both clients
        await bot.start()
        await user.start()
        
        logger.info("✅ Bot started successfully!")
        
        # Send startup message to log group
        if LOG_GROUP:
            try:
                await bot.send_message(
                    LOG_GROUP,
                    "🚀 Bot started successfully!"
                )
            except Exception as e:
                logger.error(f"Error sending startup message: {e}")
        
        # Keep the bot running
        await bot.idle()
        
    except Exception as e:
        logger.error(f"❌ Error starting bot: {e}")
    finally:
        # Stop both clients
        await bot.stop()
        await user.stop()
        logger.info("🛑 Bot stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot shutdown complete.")
    except Exception as e:
        logger.error(f"🔥 Bot error: {str(e)}")
        sys.exit(1)
