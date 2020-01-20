import discord
from discord.ext import commands
import asyncio
import os

token = os.environ.get('AuthToken')

client = commands.Bot(command_prefix = '.')


@client.command()
@commands.has_role('jokr')
async def scrim(ctx, message, arg1, arg2):
    await client.get_channel(615938985914662922).send(f"@everyone Scrim Scheduled for: **{arg1.capitalize()}, {arg2.capitalize()}**")
    await ctx.message.delete()

@client.command()
@commands.has_role('admin')
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=6)
    await ctx.channel.send("**Succesfully deleted last 5 messages :)**")

@client.command()
async def cmds(ctx):
    await ctx.channel.send("I currently have 3 Working Commands")
    await ctx.channel.send("```.sremind (time) >>> Reminds the team the amount of time before a scrim!```")
    await ctx.channel.send("```.scrim (day), (time) >>> Posts the scrim into the scrim schedule!```")
    await ctx.channel.send("```And the last command is not for you!```")



@client.command()
async def sremind(ctx, arg1, arg2):
    await client.get_channel(631644755083657267).send(f"```Reminder you have a scrim in >>> {arg1} {arg2}```")
    await ctx.message.delete()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)