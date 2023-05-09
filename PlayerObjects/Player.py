class Player:
    lastActivity = None
    commitmentList = {}
    
    def __init__(self, name):
        self.name = name
        self.playerContributions = LogiList("A list of logi contributions from " + name)
    
    def addActivity(self, newActivity):
        activityLists = nameToList[newActivity.activityName]
        #self.playerContributions.moveLists(newActivity.itemList, activityLists[0], activityLists[1])
        newActivity.lastActivity = self.lastActivity
        self.lastActivity = newActivity
    
    def printActivityList(self):
        currActivity = self.lastActivity
        while currActivity != None:
            print(f"Player {currActivity.activityName} the following items: ")
            for item in currActivity.itemList:
                print(f"{item.name}: {item.amount}")
            print("")
            currActivity = currActivity.lastActivity
        print("")