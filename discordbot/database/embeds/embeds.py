import json


class PleaseWait:
    config = json.load(
        open("discordbot/database/embeds/embeds.json", "r", encoding="utf-8"))

    TITLE = config["PleaseWait"]["TITLE"]
    DESCRIPTION = config["PleaseWait"]["DESCRIPTION"]
    FOOTER = config["PleaseWait"]["FOOTER"]
    THUMBNAIL = config["PleaseWait"]["THUMBNAIL"]
    AUTHOR_LINK = config["PleaseWait"]["AUTHOR_LINK"]
    AUTHOR_NAME = config["PleaseWait"]["AUTHOR_NAME"]
