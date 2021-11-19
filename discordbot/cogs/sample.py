import os
import platform

import discord
from discord.ext import commands

import discordbot.database.main.main as main_settings


class OnReady(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def say(self, ctx, text=None):
        await ctx.send(f"**{ctx.author.name}** - {text}")


def setup(client: commands.Bot):
    client.add_cog(OnReady(client))
