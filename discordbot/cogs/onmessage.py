import os
import platform

import discord
from discord.ext import commands


class OnMessage(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if not message.author.bot:
            await self.client.process_commands(message)


def setup(client: commands.Bot):
    client.add_cog(OnMessage(client))
