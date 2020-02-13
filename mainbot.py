import discord, asyncio, os, random, time, json, requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from discord.ext import commands, tasks
from bs4 import BeautifulSoup

token = os.environ.get('AuthToken')

client = commands.Bot(command_prefix = '.')

## Useful Commands, for Jokr.


@client.command()
@commands.has_role(629817762897985576)
async def scrim(ctx, arg1, arg2):
    role = ctx.guild.get_role(629817762897985576)
    await client.get_channel(615938985914662922).send(f"@everyone Scrim Scheduled for: **{arg1.capitalize()} at {arg2.capitalize()}**")
    await ctx.message.delete()

@client.command()
@commands.has_role(629817762897985576)
async def setgame(ctx, arg1, arg2):
    role = ctx.guild.get_role(629817762897985576)
    await client.get_channel(615938985914662922).send(f"@everyone League Match Scheduled for: **{arg1.capitalize()} at {arg2.capitalize()}**")
    await ctx.message.delete()

@client.command()
async def sremind(ctx, arg1, arg2):
    await client.get_channel(631644755083657267).send(f"```Reminder you have a scrim in >>> {arg1} {arg2}```")
    await ctx.message.delete()


# START MATCH GETTER

def getTeams():

    page = requests.get("https://vrmasterleague.com/EchoArena/Matches/")
    soup = BeautifulSoup(page.content, 'html.parser')
    matchNode = soup.find(id='MatchesScheduled_MatchesNode')
    matchesHidden = matchNode.find_all(class_ = 'rows-hider-body rows-hider-hidden')
    orangeCell = matchNode.find_all(class_ = 'home_team_cell')
    blueCell = matchNode.find_all(class_ = 'away_team_cell')

    global oteams
    global bteams
    # Get Teams in LIST \/ \/
    bteams = list()
    for teams in blueCell:
        bteams.append(teams.get_text())

    oteams = list()
    for teams in orangeCell:
        oteams.append(teams.get_text())

    
async def sendScrape():
# 
    await client.wait_until_ready()
    matchchannel = client.get_channel(676243741811671050)

    getTeams()
# 
    counter = 0
    for team  in bteams:
        if team == "Team Jokr":
            orangeTeam = oteams[counter]
            await matchchannel.send(f'@everyone Team Jokr vs {orangeTeam}')
        counter += 1


    counter = 0
    for team in oteams:
        if team == "Team Jokr":
            blueTeam = bteams[counter]
            await matchchannel.send(f'@everyone Team Jokr vs {blueTeam}')
        counter += 1


scheduler = AsyncIOScheduler()
scheduler.add_job(sendScrape, 'cron', day_of_week=0, hour=17, minute=15)
scheduler.start()

# END OF MATCH GETTER

## General Use Commands.


@client.command()
@commands.has_role('admin')
async def clear(ctx, int1):
    await ctx.message.delete()
    await ctx.channel.purge(limit=int(int1))
    confirmation = await ctx.channel.send(f"**Succesfully deleted last {str(int1)} messages :)**")
    time.sleep(3)
    await confirmation.delete() 

@client.command()
async def cmds(ctx):
    await ctx.channel.send("I currently have a few Working Commands")
    await ctx.channel.send("```.sremind (time) >>> Reminds the team the amount of time before a scrim/game!\n.scrim (day) (time) >>> Posts the scrim into the scrim schedule!\n.setgame (day) (time) >>> For settings League Games!\n.rps (rock, paper or scissors) >>> Simple game of Rock Paper Scissors!\n.rpsstats >>> Shows the total amount of server wins, ties and losses for RPS Games.\n.numguess >>> Number Guessing Game.\n.ryan >> Shows a beautiful picture of ryan!\n.clear (amount of lines) >>> Clears the amount of lines given!```")

@client.command()
async def numguess(ctx):
    rnumber = random.randint(1,20)
    guess = 0
    user_guess = 0
    print(rnumber)
    while user_guess != rnumber:
        initmessage = await ctx.send("Keep Guessing! 1 to 20!")
        response = await client.wait_for('message', timeout=30.0)
        user_guess = int(response.content)
        if user_guess > rnumber:
            await initmessage.edit(content="**Too high!**")
            guess += 1
            time.sleep(1)
            continue
        elif user_guess < rnumber:
            await initmessage.edit(content="**Too low!**")
            guess += 1
            time.sleep(1)
            continue
        elif user_guess == rnumber:
            guess += 1
            await ctx.send(f"Good Job! You guessed it in **{str(guess)}** tries")
            break
        else:
            await ctx.send("Error Code 5")

## Fun Commands <3

@client.command()
async def willwewin(ctx):
    answer = random.randint(1,100)
    if answer > 90:
        await ctx.channel.send("You're gonna get destroyed, sorry for breaking the news :)")
    elif answer < 90:
        await ctx.channel.send("You'll probably win! That's a Big Surprise!")
    else:
        await ctx.channel.send("Error Code 3")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#@client.event
#async def on_message(message):
    #print(message)

client.run(token)
