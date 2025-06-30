# Copyright (c) 2025 devgagan : https://github.com/Shivaay20005.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

# API Configuration
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
STRING = os.getenv("STRING")

# Channel Configuration
LOG_GROUP = int(os.getenv("LOG_GROUP", 0))
FORCE_SUB = int(os.getenv("FORCE_SUB", 0))

# Limits Configuration
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", 0))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", 10000))

# Database Configuration
MONGO_DB = os.getenv("MONGO_DB")
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")

# Security Keys
MASTER_KEY = os.getenv("MASTER_KEY")
IV_KEY = os.getenv("IV_KEY")

# Cookie Configuration
YT_COOKIES = os.getenv("YT_COOKIES")
INSTA_COOKIES = os.getenv("INSTA_COOKIES")

# Links Configuration
JOIN_LINK = os.getenv("JOIN_LINK")
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT")

