class Item:

    def __init__(self, name, cost, numNeeded):
        self.name = name
        self.cost = cost
        
        self.numNeeded = numNeeded
        self.numSignedUp = 0
        self.numCompleted = 0
        self.numRemaining = numNeeded
    
    def addToNumNeeded(self, num):
        self.numNeeded += num
        self.numRemaining += num