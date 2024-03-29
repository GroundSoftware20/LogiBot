import re

class Message:
    '''
        This class contains all the information from the user that the bot needs to know in order to response.
        This includes:
            author: The discord user who sent the message
            channel: The discord channel the message was sent in

            isPrivate: Whether or not to send the message privately or publically
            shouldRespond:  Whether or not a response should be sent
                            ex. If the user's message was not a command, the bot should not respond

            command: The commmand that the discord user wants to invoke
            arguments: any other arguments needs to be included; the format changes based on the command

    '''
    def __init__(self, messageObject):
        
        #set up the variable you know about
        self.channel = messageObject.channel
        self.isPrivate = self.channel == "Direct Message with Unknown User"
        self.author = messageObject.author


        #separate the input message into the command and arguments
        inputMessage = messageObject.content
        parser = re.compile("^(?P<command>/\w+)(?P<arguments>\s*.*)$", re.DOTALL)
        matches = parser.match(inputMessage)
        
        #If the message was not the correct format, don't send a response
        if(matches == None):
            self.shouldRespond = False
            return

        #Otherwise, we should process the arguments and send a response
        self.shouldRespond = True
        self.command = matches.group("command")


        self.rawArguments = matches.group("arguments")
        '''
            In this case, we want to pair up integers and item names

            Examples that work:
                1)
                    grenade 20 gun 30 bandage 4

                2)
                    20 uniforms 5 mortars 3 tanks

                3)
                    20 first aid kits 40 fragmentation grenades 10 bandages

                4)
                    20 bandages
                    50 grenade launchers 80 tripods
                    machine guns 40

            Examples that don't work
                1)
                    grenade 20 30 guns
        '''
        self.arguments = {}
        nonDigitWord= "(?:[a-z\d]*[a-z][a-z\d]*)"
        nameMatch = "(?:(" + nonDigitWord + " *)*" + nonDigitWord + ")"
        parser = re.compile("((?P<item1>" + nameMatch +") +(?P<amount1>\d+))|((?P<amount2>/d+)(?P<item2> " + nameMatch + "))")

        for m in parser.finditer(self.rawArguments):
            
            itemName = ""
            amount = ""

            if m.group("item1"):
                itemName = m.group("item1")
                amount = m.group("amount1")
            
            elif m.group("item2"):
                itemName = m.group("item2")
                amount = m.group("amount2")
            
            self.arguments[itemName] = int(amount)