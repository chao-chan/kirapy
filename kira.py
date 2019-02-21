import discord
import random
import asyncio
import aiohttp
import json
from discord.ext.commands import Bot

token = 'NTQ3OTY3MjU1OTg0NjAzMTM2.D1B6nw.YhDSdqyTVP_VjvrMKy5kZixv9ZA'
version = 'v0'
bot_prefix = ("?", "!")
client = Bot(command_prefix=bot_prefix)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #dont let the bot reply to itself
    if message.author == client.user:
        return
    
@client.command(name='hello',
                description="Simple Hello Command",
                brief="Hello!",
                pass_context=True)
async def hello():
    await client.say("Hello!!")

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    if not context.message.channel.is_private and context.message.channel.name != client.designated_channel_name:
        return
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    #debug
    print("Used 8ball Command")


@client.event
async def on_ready():
    print('Hey guys! Kira starting up!')
    print('My name is: ' + client.user.name)
    print('And my user id is: ' + client.user.id)
    print('-------------------------------------------')

client.run(token)