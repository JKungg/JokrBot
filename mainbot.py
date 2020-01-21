import discord
from discord.ext import commands
import asyncio
import os
import random
import time

token = os.environ.get('AuthToken')

client = commands.Bot(command_prefix = '.')


@client.command()
@commands.has_role('jokr')
async def scrim(ctx, arg1, arg2):
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
    await ctx.channel.send("```.sremind (time) >>> Reminds the team the amount of time before a scrim!\n.scrim (day), (time) >>> Posts the scrim into the scrim schedule!\n.rpc (rock, paper or scissors) >>> Simple game of Rock Paper Scissors!\nAnd the last command is not for you!```")


@client.command()
async def sremind(ctx, arg1, arg2):
    await client.get_channel(631644755083657267).send(f"```Reminder you have a scrim in >>> {arg1} {arg2}```")
    await ctx.message.delete()

@client.command()
async def rpc(ctx, int1):
    aiPick = random.randint(1,3)
    if int1 == 'rock':
        await ctx.channel.send("Hmm what should I pick?")
        time.sleep(1)
        if aiPick == 1:
            await ctx.channel.send("Whoops, we both picked **Rock**!")
        elif aiPick == 2:
            await ctx.channel.send("My **paper** beat your **rock**!")
        elif aiPick == 3:
            await ctx.channel.send("Your **rock** destroyed my **scissors**!")
    elif int1 == 'paper':
        await ctx.channel.send("Hmm what should I pick?")
        time.sleep(1)
        if aiPick == 1:
            await ctx.channel.send("Your **paper** beat my **rock**! :(")
        elif aiPick == 2:
            await ctx.channel.send("We both chose **paper** it's a tie!")
        elif aiPick == 3:
            await ctx.channel.send("My **scissors** destroyed your **paper**!")
    elif int1 == 'scissors':
        await ctx.channel.send("Hmm what should I pick?")
        time.sleep(1)
        if aiPick == 1:
            await ctx.channel.send("My **Rock** beat your **scissors**")
        elif aiPick == 2:
            await ctx.channel.send("Your **scissors** destroyed my **paper**!")
        elif aiPick == 3:
            await ctx.channel.send("We both chose **scissors** it's a draw!")
    else:
        await ctx.channel.send("Error! 404")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)
