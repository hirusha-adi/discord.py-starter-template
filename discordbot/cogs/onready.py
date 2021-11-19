import os
import platform

import discord
from discord.ext import commands

import discordbot.database.main.main as main_settings


class OnReady(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"* Logged in as {self.client.user}")
        print(f"* Discord.py API version: {discord.__version__}")
        print(f"* Python version: {platform.python_version()}")
        print(
            f"* Running on: {platform.system()} {platform.release()} ({os.name})")
        await self.client.change_presence(activity=discord.Game(str(main_settings.PRESENCE)))
        print("-"*22)
        print("+ Bot is ready to be used!")


def setup(client: commands.Bot):
    client.add_cog(OnReady(client))
