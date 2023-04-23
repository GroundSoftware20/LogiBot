import discord
from Data import *

def handle_response(messageObject)->str:
    command = messageObject.command
    channel = messageObject.channel
    print(command)

    #modify chore list
    if command == "/description":
        return setDesciption(messageObject)
    elif command == "/add":
        return addItems(messageObject)
    elif command == "/remove":
        return "run remove items"
    elif command == "/deletelist":
        return "run delete list"
    
    #signup and completion actions
    elif command == "/signup":
        return "run signup"
    elif command == "/unsignup":
        return "run unsignup"
    elif command == "/complete":
        return "run complete"
    elif command == "/uncomplete":
        return "run uncomplete"
    
    #view information
    elif command == "/view":
        return viewLogiList(channel)
    elif command == "/log":
        return "run log"
    elif command == "/help":
        return "run help"
    elif command == "/iteminfo":
        return printItemInfo()
    
    #save stats
    elif command == "/save":
        return "data not saved"
    elif command == "/load":
        return "data not loaded"
    
    else:
        return "unknown command. Run /help for the command list"

async def send_message(messageObject):
    try:

        #Handle Private Requests here
        if messageObject.isPrivate:
            #Need to add different behavior for this later
            response = handle_response(messageObject)
            await messageObject.author.send(response)            

        else:
            response = handle_response(messageObject)
            await messageObject.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = getToken()

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




