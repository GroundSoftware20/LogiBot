import Responses
import discord
import HandleData
from Message import Message
async def send_message(messageObject):
    try:

        #Handle Private Requests here
        if messageObject.isPrivate:
            #Need to add different behavior for this
            response = Responses.handle_response(messageObject)
            await messageObject.author.send(response)            

        else:
            response = Responses.handle_response(messageObject)
            await messageObject.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA5NTc2NzI2MjMzOTgwOTMzMg.GT7S8H.9RrLztmaECZvxSrCPzuZT4VG-ZhIqqaD1bf3EM'

    intents = discord.Intents.default()
    intents.message_content = True

    HandleData.loadItemInfo()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        input = Message(message)
        if input.shouldRespond == True:
            await send_message(input)

    client.run(TOKEN)




