import os

import discord
from discord.ext import commands

import discordbot.database.main.main as main_settings
import discordbot.web.web_server as web_server

# Defining the bot
client = commands.Bot(command_prefix=str(main_settings.PREFIX))

# Loading all the cogs
for filename in os.listdir('./discordbot/cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'discordbot.cogs.{filename[:-3]}')
        print(f"+ Loaded discordbot.cogs.{filename[:-3]}")

# Running the web server
if main_settings.START_WEB_SERVER == True:
    web_server.keep_alive()

# Running the bot
client.run(str(main_settings.BOT_TOKEN), reconnect=True)
