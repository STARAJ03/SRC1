# Copyright (c) 2025 devgagan : https://github.com/Shivaay20005.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB = os.getenv("MONGO_DB", "")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", "1BVtsOKEBu6tpuKQA25BrfQ9ZMOqUMkwHawHfokYxhnj_ru3BTLIsJrmH2gYYjtuNsvKnYoZBbp0HqkVpqJkIwzxmxG8SX5OldMajhRFtCIjcpYfwOpMpm5U0chIF7CgdbeiSmY63ekdHyChujzA5ASdV-PdzeFUZxNeUl4GBhMl74dP0R-bnTeb03jlxddzu9ZwaXglqnyIJ1obhn7wYggiUCcKiAOwnfbEkwmheDiBuXoZRPNF7xH4kRIQh6n2KT5PVmVhv76eqFIlwenVLirg6g0p-QKQOuhYpguMl1TSfZVand-Mnl99sLbDDlTpj6zeti2YdOywVzNpNhNCfCvnlJIYWLSw=") # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1001234456")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-10012345567")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/Shivaay20005") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/Shivaay20005")

