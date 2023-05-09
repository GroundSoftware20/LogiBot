import json
from BaseObjects import *

itemInfo = {}

def getToken():
    tokenFile = open("Data\discordToken.txt", "r")

    return tokenFile.read()

def getSpaces(numSpaces):
    if numSpaces <= 0:
        return ""
    
    to_return = ""

    for i in range(numSpaces):
        to_return += " "
    
    return to_return


def printItemInfo():
    #10, 18, 21 19
    to_return = "```| Names                            | Basic Materials | Explosive Materials | High Explosive Materials | Refined Materials |\n"

    j = 0
    for i in itemInfo.keys():
        to_return += "| " + i + getSpaces(32 - len(i))
        to_return += " | " + str(itemInfo[i].bmat) + getSpaces(15 - len(str(itemInfo[i].bmat)))
        to_return += " | " + str(itemInfo[i].emat) + getSpaces(19 - len(str(itemInfo[i].emat)))
        to_return += " | " + str(itemInfo[i].hemat) + getSpaces(24 - len(str(itemInfo[i].hemat)))
        to_return += " | " + str(itemInfo[i].rmat) + getSpaces(17 - len(str(itemInfo[i].rmat))) + " |\n"
        j += 1
        if(j > 10):
            break


    to_return += "```"

    return to_return

#Loads the item information from a json file
def loadItemInfo(path="data/items.json"):
    data = json.loads(open(path).read())
    for i in data["items"]:
        resources = {"bmat":0, "emat":0, "hemat":0, "rmat":0}
        cost_field = i["cost"]
        for res in resources.keys():
            if res in cost_field:
                resources[res] = cost_field[res]

        itemInfo[i["itemName"].lower()] = Cost(resources["bmat"], resources["emat"],resources["hemat"],resources["rmat"])

list_directory = {}

#These functions are for changing the LogiList

#Checks if a LogiList needs to be created for a channel. If it does, it creates one
def createLogiListIfNeeded(channel):
    if not channel in list_directory:
        list_directory[channel] = LogiList()

#Sets the description of a LogiList
def setDesciption(messageObject):
    createLogiListIfNeeded(messageObject.channel)

    list_directory[messageObject.channel].description = messageObject.arguments
    return "Description sucessfully changed"

#Helper: Takes an input item name and finds possible matches
def lookupItem(input):

    candidates = []
    for i in itemInfo.keys():
        if input == i.lower():
            candidates.append(i.lower())
            return candidates
        if input in i.lower():
            candidates.append(i.lower())
        
    
    return candidates

#Add items to a LogiList
def addItems(messageObject):
    channel = messageObject.channel
    createLogiListIfNeeded(channel)

    errorItems = []
    successItems = []

    if len(messageObject.arguments) == 0:
        return "Please insert valid items"

    for itemName, quantity in messageObject.arguments.items():
        itemMatches = lookupItem(itemName)
    
        if len(itemMatches) == 0:
            errorItems.append("\n    " + itemName + "\n        Did not find matching item names")

        elif len(itemMatches) == 1:
            formalItemName = itemMatches[0]
            print(formalItemName)

            if formalItemName in list_directory[channel].itemList.keys():
                list_directory[channel].itemList[formalItemName].addToNumNeeded(quantity)
            else:
                cost = itemInfo[formalItemName]
                toAdd = LogiListItem(formalItemName, cost, quantity)
                
                
                list_directory[channel].itemList[formalItemName] = toAdd
                print(list_directory[channel].itemList[formalItemName].name)
            successItems.append("\n    " + itemName + " " + str(quantity))
        
        else:
            errorString = "\n    " + itemName + "  matches with:"

            for item in itemMatches:
                errorString += "\n        " + item
            
            errorItems.append(errorString)
    
    to_return = ""

    if len(successItems) > 0:
        to_return += "The following items were successfully added:"
        for item in successItems:
            to_return += item
    
    if len(errorItems) > 0:
        to_return += "\n\nThe following items could not be added:"
        for item in errorItems:
            to_return += item
    return to_return

def modifyLogiList(messageObject, listToModify):
    channel = messageObject.channel
    
    if not channel in list_directory:
        return "A logi list does not exist for this channel"

    for item, amount in messageObject.arguments.items():
        print(item)
        print(amount)
        itemMatches = lookupItem(item)
        newItem = itemMatches[0]
        if newItem in list_directory[channel].itemList.keys():

            print("present")
            if messageObject.command == "/unsignup" or messageObject.command == "/uncomplete":
                amount *= -1

            list_directory[channel].itemList[newItem].modifyList(listToModify, amount)
        else:
            print("not present")

    return "success"

def signup(messageObject):
    return modifyLogiList(messageObject, ListType.numSignedUp)
    
def complete(messageObject):
    return modifyLogiList(messageObject, ListType.numCompleted)

def unsignup(messageObject):
    return modifyLogiList(messageObject, ListType.numSignedUp)

def uncomplete(messageObject):
    return modifyLogiList(messageObject, ListType.numCompleted)


#These functions are for viewing the LogiList
def viewLogiList(channel):
    
    createLogiListIfNeeded(channel)

    columns = ["          Name          ", "Needed", "Signed Up For", "Completed", "Remaining"]

    to_return = "```"

    #Very top
    for col in columns:
        to_return += "| " + col + " "
    to_return += "|"

    if len(list_directory[channel].itemList) == 0:
        to_return += "\n(No items in the list yet)"
    #Go through LogiList
    for item_instance in list_directory[channel].itemList.keys():
        print(item_instance)
        item = list_directory[channel].itemList[item_instance]
        print(item.name)
        to_return += "\n| " + item.name + getSpaces(len(columns[0]) + 1 - len(item.name))
        to_return += "| " + str(item.getNumNeeded()) + getSpaces(len(columns[1]) + 1 - len(str(item.getNumNeeded())))
        to_return += "| " + str(item.getNumSignedUp()) + getSpaces(len(columns[2]) + 1 - len(str(item.getNumSignedUp())))
        to_return += "| " + str(item.getNumCompleted()) + getSpaces(len(columns[3]) + 1 - len(str(item.getNumCompleted())))
        to_return += "| " + str(item.getNumRemaining()) + getSpaces(len(columns[4]) + 1 - len(str(item.getNumRemaining()))) + '|'
    
    to_return += "```"

    return to_return