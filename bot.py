import discord
import os
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


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('for Ashwin'))


# returns the user's ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency * 1000)}ms')


# runs the client using its Discord API Token
client.run('NzIyNTc0NzU4MTc2MjI3Mzk5.XulEXw.0sGoOSHo-KyT-Kzalw31pX94FO4')
