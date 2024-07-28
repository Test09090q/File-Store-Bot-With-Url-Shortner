import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "9619481"))
  API_HASH = os.environ.get("API_HASH", "10effb30531c66d27b90f1e07f6bd071")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6725760034:AAEHsb0N2E93k8JPlDohvlYJmIEGFIdxCeM")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Kmoviestore_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002011038623"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "ziplinker.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "8ea1e29d79de76acacdae5625f19fe8703c97f68")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6624919731"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://fffworld57:Or97XLuv6P6GvtFZ@cluster0.u34tcer.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002115836678"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent Public file Store bot. 
𝗣𝗹𝗲𝗮𝘀𝗲 𝗗𝗼𝗻'𝘁 𝗨𝗽𝗹𝗼𝗮𝗱 𝟭𝟴+ 𝗩𝗶𝗱𝗲𝗼𝘀 𝗜𝗳 𝘆𝗼𝘂 𝘂𝗽𝗹𝗼𝗮𝗱 𝘁𝗵𝗲𝗻 𝘆𝗼𝘂 𝗯𝗮𝗻𝗻𝗲𝗱 💀.
╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [private Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[  ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [kk](https://telegram.me/9)
 
 I am Super noob Please Support My Hard Work.

[repo](https://t.me/paidby99)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\n
 This is a Permanent Public file Store bot. 
𝗣𝗹𝗲𝗮𝘀𝗲 𝗗𝗼𝗻'𝘁 𝗨𝗽𝗹𝗼𝗮𝗱 𝟭𝟴+ 𝗩𝗶𝗱𝗲𝗼𝘀 𝗜𝗳 𝘆𝗼𝘂 𝘂𝗽𝗹𝗼𝗮𝗱 𝘁𝗵𝗲𝗻 𝘆𝗼𝘂 𝗯𝗮𝗻𝗻𝗲𝗱 💀**About Bot**.
"""
