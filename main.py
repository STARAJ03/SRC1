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

# Flask App Setup
flask_app = Flask(__name__)
app = flask_app  # For Gunicorn

# Initialize Telegram Client (MOVE THIS TO shared_client.py if needed)
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
client = TelegramClient('bot_session', api_id, api_hash)

@flask_app.route("/")
def welcome():
    return redirect("https://t.me/Shivaay20005", code=302)

async def start_client():
    try:
        await client.start()
    except FloodWaitError as e:
        print(f'Waiting {e.seconds} seconds due to flood wait')
        time.sleep(e.seconds)
        await start_client()

async def load_and_run_plugins():
    await start_client()
    plugin_dir = "plugins"
    plugins = [f[:-3] for f in os.listdir(plugin_dir) 
               if f.endswith(".py") and f != "__init__.py"]

    for plugin in plugins:
        try:
            module = importlib.import_module(f"plugins.{plugin}")
            if hasattr(module, f"run_{plugin}_plugin"):
                print(f"Running {plugin} plugin...")
                await getattr(module, f"run_{plugin}_plugin")()
        except Exception as e:
            print(f"Failed to load plugin {plugin}: {str(e)}")

async def bot_main():
    print("Starting Telegram bot...")
    await load_and_run_plugins()
    while True:
        await asyncio.sleep(1)

def run_web():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    if os.environ.get("WORKER_MODE"):
        try:
            asyncio.run(bot_main())
        except KeyboardInterrupt:
            print("Bot shutdown complete")
        except Exception as e:
            print(f"Bot error: {str(e)}")
            sys.exit(1)
    else:
        run_web()