class Cost:

    def __init__(self, b, e, he, r):
        self.bmat = b
        self.emat = e
        self.hemat = he
        self.rmat = r

class Item:

    def __init__(self, name, cost, numNeeded):
        self.name = name
        self.cost = cost
        
        self.numNeeded = numNeeded
        self.numSignedUp = 0
        self.numCompleted = 0
        self.numRemaining = numNeeded
    
    def addToNeeded(num):
        numNeeded += num
        numRemaining += num