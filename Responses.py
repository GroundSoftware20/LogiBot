from HandleData import *

def parseItems():

    str_list = str.split()


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
    
    