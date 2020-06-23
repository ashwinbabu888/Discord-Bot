import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!")


# load cogs command
@client.command()
async def load(ctx, extension):
    await ctx.send(f'Loaded {extension}.py cog.')
    client.load_extension(f'cogs.{extension}')


# unload cogs command
@client.command()
async def unload(ctx, extension):
    await ctx.send(f'Unloaded {extension}.py cog.')
    client.unload_extension(f'cogs.{extension}')


# reload cogs command
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}.py cog.')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# clear function
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


# returns the user's ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency * 1000)}ms')


# flips a coin
@client.command()
async def flip(ctx):
    sides = ['heads', 'tails']
    await ctx.send(f'{random.choice(sides)}')


# chooses debate round side and order
@client.command()
async def decide(ctx):
    sides = ['aff', 'neg']
    order = ['1st', '2nd']
    decision = [random.choice(sides), random.choice(order)]
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
    await ctx.send(f'You will be {decision[0]} {decision[1]}, and your opponent will be {decision2[0]} {decision2[1]}')


# 8 ball feature which responds to a question
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
                 "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                 "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                 "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
                 "Outlook not so good.", "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


# echoes the given message and deletes the command
@client.command(aliases=['copy'])
async def echo(ctx, *, message):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{message}')


# kick member function
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked!')


# ban member function
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned!')


# unban member function
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} has been unbanned!')
            break


# runs the client using its Discord API Token
client.run('NzIyNTc0NzU4MTc2MjI3Mzk5.XulEXw.0sGoOSHo-KyT-Kzalw31pX94FO4')
