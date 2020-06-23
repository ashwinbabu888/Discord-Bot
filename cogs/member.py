import discord
from discord.ext import commands


class Initialize(commands.Cog):

    def __init__(self, client):
        self.client = client

    # returns the name of who joined the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server!')

    # returns the name of who left the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} left the server.')


def setup(client):
    client.add_cog(Initialize(client))
