import json

config = json.load(
    open("discordbot/database/main/main.json", "r", encoding="utf-8"))

BOT_TOKEN = config["TOKEN"]
PRESENCE = config["PRESENCE"]
PREFIX = config["PREFIX"]
START_WEB_SERVER = config["START_WEB_SERVER"]
