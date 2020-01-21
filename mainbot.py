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
    await ctx.channel.send("I currently have a few Working Commands")
    await ctx.channel.send("```.sremind (time) >>> Reminds the team the amount of time before a scrim!\n.scrim (day), (time) >>> Posts the scrim into the scrim schedule!\n.rpc (rock, paper or scissors) >>> Simple game of Rock Paper Scissors!\n.rpcstats >>> Shows the total amount of server wins, ties and losses for RPC Games.\n.ryan >> Shows a beautiful picture of ryan!\nAnd the last command is not for you!```")


@client.command()
async def sremind(ctx, arg1, arg2):
    await client.get_channel(631644755083657267).send(f"```Reminder you have a scrim in >>> {arg1} {arg2}```")
    await ctx.message.delete()

@client.command()
async def rpc(ctx, int1):
    aiPick = random.randint(1,3)
    result = 'None'
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
    if result == 'Win':
        stats = open("rpcjokrstats.txt", "a")
        stats.write("Win ")
        stats.close()
    elif result == 'Tie':
        stats = open("rpcjokrstats.txt", "a")
        stats.write("Tie ")
        stats.close()
    elif result == 'Loss':
        stats = open("rpcjokrstats.txt", "a")
        stats.write("Loss ")
        stats.close()
    else:
        await ctx.channel.send("Error 405!")

@client.command()
async def rpcstats(ctx):
    stats = open("rpcjokrstats.txt", "r")
    rsl = stats.read()
    win = rsl.count('Win ')
    ties = rsl.count('Tie ')
    loss = rsl.count('Loss ')
    stats.close()
    await ctx.channel.send("```Wins = " + str(win) + "\nDraws = " + str(ties) + "\nLosses = " + str(loss) + "```")


@client.command()
async def ryan(ctx):
    await ctx.channel.send("https://static-cdn.jtvnw.net/jtv_user_pictures/f0f76f1e-0ba2-4f3b-927d-c6df70a8022d-profile_image-300x300.png")

@client.command()
async def trenty111222(ctx):
    await ctx.channel.send("https://cdn2-img.pressreader.com/pressdisplay/docserver/getimage.aspx?regionKey=OMvzDX2twTLVQEtqCt%2BWaA%3D%3D")
    await ctx.channel.send("Love you Trent <3")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)