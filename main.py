# Work with Python 3.7.4
import random
import asyncio
import aiohttp
import json
import discord
from discord import *
from discord.ext import commands
from discord.ext.commands import *
import time
import random
import math

BOT_PREFIX = ("w:")
TOKEN = 'NjY5NTcwOTYyOTkxMjE4NzM0.Xihzwg.NLsikuOQKMKriQmPCJlACqI6YyE'
#the token you need for the bot to work



client = Bot(command_prefix=BOT_PREFIX)
bot = commands.Bot(command_prefix='!')


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


#Works
@client.command(
    name="Bitcoin",
    description="Shows the current Bitcoin Price",
    brief="p:bitcoin",
    aliases=['bitcoin'],
    pass_context=True)
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" +
                          response['bpi']['USD']['rate'])

@client.command(
    name='info',
    description='Shows information',
    brief='Shows info',
    aliases=['information'],
    pass_context=True)
async def info(ctx):
    await ctx.send("**Here is some information about this Discord Bot**")
    time.sleep(1)
    await ctx.send(
        "```\nCreated by:\nRiley Richard, Joystick#7300\nSamuel Nalini, RescueTwo#9584\n------------------------\nCreated On: 1/22/2020\nUpdated On: 1/22/2020```"
    )



word = {

      '@everyone YOU NEED TO BE WORKING OUT!!!',
      '@everyone I HEARD MARINE RECRUITERS ARE LOOKING FOR PEOPLE JUST LIKE YOU, 1.5GPA AND 300LBS',
      '@everyone THOSE JELLY ROLLS ARE LOOKING TASTY, BETTER MOVE BEFORE I CATCH YOU!!!!',
      '@everyone DO YOU WANT TO BE LAZY FOR THE REST OF YOUR LIFE!?!?!?!?!?!?!?',
      '@everyone THAT GUY IS MERGING ONTO YOUR LANE!!! WALK IT OFF NOWW. 300 MILE SPRINT ON THE DOUBLE!!!!!',
      '@everyone MOVEEEEEE NOWWWWW!!!',
      "@everyone CMON PRIVATE PYLE GET THOSE LEGS MOVIN\'",
      '@everyone THOSE DONUTS AREN\'T GOING TO BURN THEMSELVES OFF!',
      '@everyone DO 500 JUMPING JACKS THIS INSTANT!!!',
      '@everyone GET MOVING NOW!!!',


}



@client.command(
    name='exercise',
    description='Shows information',
    brief='Shows info',
    aliases=[],
    pass_context=True)
async def check(ctx):

  start, finish = random.choice(list(word.items()))


  if ctx.message.content.startswith('message'):
      channel = ctx.channelTest
      await channel.send('Knock Knock')


      def check(m):
        return m.content == 'who\'s there?', "Who's there?", "whos there?", "who's there", "whos there", "Who's There?", "Who's There", "who is there?", "Who is there?" and m.channel == channel

        msg = client.wait_for('message', check=check)
        return m.content == start.format(msg) + " who?", start.format(msg) + " who" and m.channel == channel

        
        channelTest = client.get_channel(557646913583710208)
        await channelTest.send('Initialize Exercise Robot "Wayze"')
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)
        msg = await client.wait_for('message', check=check)
        await channelTest.send(start.format(msg))
        time.sleep(25)

        channelTestSecond = client.get_channel(669609923524689972)
        await channelTestSecond.send("w:exercise")






@client.command(
    name="exercise",
    description="no",
    brief="f",
    aliases=[],
    pass_context=True)
async def knock(ctx):
    start, finish = random.choice(list(word.items()))

    if ctx.message.content.startswith('message'):
        channel = ctx.channel
        await channel.send("Initializing Wayze Exercise Bot.")

        def check(m):
            return m.content == 'who\'s there?', "Who's there?", "whos there?", "who's there", "whos there", "Who's There?", "Who's There", "who is there?", "Who is there?" and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(start.format(msg))
        def firstResponse(m):
            return m.content == ((list(word.items))) and m.channel == channel


        def secondResponse(m):
            return m.content == start.format(msg) + " who?", start.format(msg) + " who" and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(finish.format(msg))
        def thirdResponse(m):
            return m.content == ((list(word.items))) and m.channel == channel



client.loop.create_task(list_servers())
client.run(TOKEN)