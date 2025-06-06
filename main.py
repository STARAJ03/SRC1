# # Copyright (c) 2025 devgagan : https://github.com/Shivaay20005.  
# # Licensed under the GNU General Public License v3.0.  
# # See LICENSE file in the repository root for full license text.

# import asyncio
# from shared_client import start_client
# import importlib
# import os
# import sys

# async def load_and_run_plugins():
#     await start_client()
#     plugin_dir = "plugins"
#     plugins = [f[:-3] for f in os.listdir(plugin_dir) if f.endswith(".py") and f != "__init__.py"]

#     for plugin in plugins:
#         module = importlib.import_module(f"plugins.{plugin}")
#         if hasattr(module, f"run_{plugin}_plugin"):
#             print(f"Running {plugin} plugin...")
#             await getattr(module, f"run_{plugin}_plugin")()  

# async def main():
#     await load_and_run_plugins()
#     while True:
#         await asyncio.sleep(1)  

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     print("Starting clients ...")
#     try:
#         loop.run_until_complete(main())
#     except KeyboardInterrupt:
#         print("Shutting down...")
#     except Exception as e:
#         print(e)
#         sys.exit(1)
#     finally:
#         try:
#             loop.close()
#         except Exception:
#             pass


import os
import asyncio
import importlib
import sys
import time
from flask import Flask, redirect
from telethon import TelegramClient
from telethon.errors import FloodWaitError
from telethon.sessions import StringSession

# ─────────────────────────────────────────────
# Flask App Setup
# ─────────────────────────────────────────────
flask_app = Flask(__name__)
app = flask_app  # For gunicorn compatibility

@flask_app.route("/")
def welcome():
    return redirect("https://t.me/Shivaay20005", code=302)

# ─────────────────────────────────────────────
# Telegram Client Initialization
# ─────────────────────────────────────────────
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
session_string = os.getenv('STRING')  # use STRING from Heroku env
client = TelegramClient(StringSession(session_string), api_id, api_hash)

# ─────────────────────────────────────────────
# Telegram Bot Start Function
# ─────────────────────────────────────────────
async def start_client():
    try:
        await client.start(bot_token=bot_token)
        print("✅ Bot started successfully.")
        print("🔐 Session string (backup):", client.session.save())
    except FloodWaitError as e:
        print(f"⚠️ Flood wait triggered: sleeping for {e.seconds} seconds...")
        time.sleep(e.seconds)
        await start_client()
    except Exception as e:
        print(f"❌ Failed to start client: {str(e)}")
        sys.exit(1)

# ─────────────────────────────────────────────
# Plugin Loader
# ─────────────────────────────────────────────
async def load_and_run_plugins():
    try:
        plugin_dir = "plugins"
        if not os.path.exists(plugin_dir):
            os.makedirs(plugin_dir)

        plugins = [f[:-3] for f in os.listdir(plugin_dir)
                   if f.endswith(".py") and f != "__init__.py"]

        for plugin in plugins:
            try:
                module = importlib.import_module(f"plugins.{plugin}")
                if hasattr(module, f"run_{plugin}_plugin"):
                    print(f"🔌 Running {plugin} plugin...")
                    await getattr(module, f"run_{plugin}_plugin")()
            except Exception as e:
                print(f"⚠️ Failed to load plugin {plugin}: {str(e)}")
    except Exception as e:
        print(f"❌ Plugin loader error: {str(e)}")

# ─────────────────────────────────────────────
# Bot Main Loop
# ─────────────────────────────────────────────
async def bot_main():
    print("🚀 Starting Telegram bot...")
    await start_client()
    await load_and_run_plugins()
    while True:
        await asyncio.sleep(3600)  # Keep alive

# ─────────────────────────────────────────────
# Web Server Run Function (Gunicorn)
# ─────────────────────────────────────────────
def run_web():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

# ─────────────────────────────────────────────
# Main Execution Logic
# ─────────────────────────────────────────────
if __name__ == "__main__":
    if os.environ.get("WORKER_MODE"):  # worker dyno
        try:
            asyncio.run(bot_main())
        except KeyboardInterrupt:
            print("🛑 Bot shutdown complete.")
        except Exception as e:
            print(f"🔥 Bot error: {str(e)}")
            sys.exit(1)
    else:  # web dyno
        run_web()
