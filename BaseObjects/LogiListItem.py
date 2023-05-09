from .ListType import ListType
class LogiListItem:

    def __init__(self, name, cost, numNeeded):
        self.name = name
        self.cost = cost
        
        self.lists = {}
        self.lists[ListType.numNeeded] = numNeeded
        self.lists[ListType.numSignedUp] = 0
        self.lists[ListType.numCompleted] = 0
        self.lists[ListType.numRemaining] = numNeeded
    
    #Helper Functions
    def calcNumRemaining(self):
        self.lists[ListType.numRemaining] = self.lists[ListType.numNeeded] - self.lists[ListType.numSignedUp] - self.lists[ListType.numCompleted]

        self.lists[ListType.numRemaining] = max(self.lists[ListType.numRemaining], 0)


    #Public Functions

    #Mutators

    def modifyList(self, listIndex, num):
        self.lists[listIndex] += num

        self.lists[listIndex] = max(self.lists[listIndex], 0)
        self.calcNumRemaining()

    def addToNumNeeded(self, num):
        self.modifyList(ListType.numNeeded, num)

    def signup(self, num):
        self.modifyList(ListType.numSignedUp, num)
        
    def unsignup(self, num):
        self.modifyList(ListType.numSignedUp, -num)

    def complete(self, num):
        self.modifyList(ListType.numCompleted, num)

    def uncomplete(self, num):
        self.modifyList(ListType.numCompleted, -num)
    
    #Accessors
    def getNumNeeded(self):
        return self.lists[ListType.numNeeded]
    
    def getNumSignedUp(self):
        return self.lists[ListType.numSignedUp]
    
    def getNumCompleted(self):
        return self.lists[ListType.numCompleted]
    
    def getNumRemaining(self):
        return self.lists[ListType.numRemaining]