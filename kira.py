import discord

client = discord.Client()
token = 'NTQ3OTY3MjU1OTg0NjAzMTM2.D0-jRA.ENOZ0BLgASrMTdvRhTbWjgSKSPE'
version = 'v0'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #dont let the bot reply to itself
    if message.author == client.user:
        return
    
    if message.content.startswith('kpy!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Hey guys! Kira starting up!')
    print('My name is: ' + client.user.name)
    print('And my user id is: ' + client.user.id)
    print('-------------------------------------------')

client.run(token)