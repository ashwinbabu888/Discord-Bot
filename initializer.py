import discord
from discord.ext import commands


class Initialize(commands.Cog):

    def __init__(self, client):
        self.client = client

    # message to confirm initialization
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot has been initialized.')


def setup(client):
    client.add_cog(Initialize(client))
