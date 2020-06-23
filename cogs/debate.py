import discord
import random
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # flips a coin
    @commands.command()
    async def flip(self, ctx):
        sides = ['heads', 'tails']
        await ctx.send(f'{random.choice(sides)}')

    # chooses debate round side and order
    @commands.command()
    async def decide(self, ctx):
        sides = ['aff', 'neg']
        order = ['1st', '2nd']
        decision = [random.choice(sides), random.choice(order)]
        decision2 = []
        if decision[0] == 'aff':
            if decision[1] == '1st':
                decision2 = ['neg', '2nd']
            elif decision[1] == '2nd':
                decision2 = ['neg', '1st']
        elif decision[0] == 'neg':
            if decision[1] == '1st':
                decision2 = ['aff', '2nd']
            elif decision[1] == '2nd':
                decision2 = ['aff', '1st']
        await ctx.send(
            f'You will be {decision[0]} {decision[1]}, and your opponent will be {decision2[0]} {decision2[1]}')


def setup(client):
    client.add_cog(Example(client))
