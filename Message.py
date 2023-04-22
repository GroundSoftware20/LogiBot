import re

class Message:

    def __init__(self, messageObject):
        
        #set up the variable you know about
        self.channel = messageObject.channel
        self.isPrivate = self.channel == "Direct Message with Unknown User"
        self.author = messageObject.author
        self.shouldRespond = False

        #separate command an arguments
        inputString = messageObject.content
        parser = re.compile("^(?P<command>/\w+)(?P<arguments>\s*.*)$", re.DOTALL)
        matches = parser.match(inputString)
        
        if(matches == None):
            return

        self.shouldRespond = True
        self.command = matches.group("command")
        argumentsToProcess = matches.group("arguments")


        if self.command == "/argumentsToProcess":
            self.arguments = argumentsToProcess
            return
        
        self.arguments = {}
        parser = re.compile("[\s]+((?P<item>[a-zA-Z][a-zA-Z]+[a-zA-Z])[\t ]+(?P<quantity>\d+))|((?P<quantity2>\d+)[\t ]+(?P<item2>[a-zA-Z][a-zA-Z ]*[a-zA-Z]))")
        for m in parser.finditer(argumentsToProcess):
            
            itemName = ""
            amount = ""

            if m.group("item"):
                itemName = m.group("item")
                amount = m.group("quantity")
            
            elif m.group("item2"):
                itemName = m.group("item2")
                amount = m.group("quantity2")
            
            self.arguments[itemName] = int(amount)