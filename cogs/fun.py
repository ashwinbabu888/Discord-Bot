import discord
import random
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # 8 ball feature that responds to a question
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
                     "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                     "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                     "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
                     "Outlook not so good.", "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    # echoes the given message and deletes the command
    @commands.command(aliases=['copy'])
    async def echo(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{message}')


def setup(client):
    client.add_cog(Fun(client))
