import discord
from discord.ext import commands
import asyncio
import os

token = os.environ.get('AuthToken')

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
@commands.has_role('jokr')
async def scrim(ctx, arg1, arg2):
    await client.get_channel(615938985914662922).send(f"@everyone Scrim Scheduled for: **{arg1.capitalize()}, {arg2.capitalize()}**")


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.author.id == 372522812403089409:
        await message.delete()


client.run(token)