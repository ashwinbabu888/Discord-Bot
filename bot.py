import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!")


# message to confirm initialization
@client.event
async def on_ready():
    print('I am ready!')


# returns the name of who joined the server
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')


# returns the name of who left the server
@client.event
async def on_member_remove(member):
    print(f'Wow. {member} left the server.')


# clear function
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


# returns the user's ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency * 1000)}ms')


# 8 ball feature which responds to a question
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
                 "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                 "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                 "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
                 "Outlook not so good.", "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


# kick member function
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


# ban member function
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


# runs the client using its Discord API Token
client.run('NzIyNTc0NzU4MTc2MjI3Mzk5.XulEXw.0sGoOSHo-KyT-Kzalw31pX94FO4')
