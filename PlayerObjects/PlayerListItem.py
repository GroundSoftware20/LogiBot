class PlayerItem:
    
    def __init__(self, name, cost, numNeeded):
        
    
    def addToNumNeeded(self, num):

        if(self.numNeeded == -1):
            return

        self.numNeeded += num
        self.numRemaining += num

    def signup(self, num):
            
        print("here")
        self.numSignedUp += num

        if self.numNeeded == -1:
            self.numRemaining += num
            
            if self.numRemaining > self.numNeeded:
                self.numRemaining = self.numNeeded
        else:
            self.numRemaining -= num

            if self.numRemaining < 0:
                self.numRemaining = 0
        
    def unsignup(self, num):
        self.numSignedUp -= num

        if self.numSignedUp < 0:
            self.numSignedUp = 0

        if self.numNeeded != -1:
             self.numRemaining += num

             if self.numRemaining > self.numNeeded:
                self.numRemaining = self.numNeeded
        else:
            self.numRemaining -= num

            if self.numRemaining < 0:
                self.numRemaining = 0

    def complete(self, num):
        self.numCompleted += num
        
        if self.numNeeded == -1:
            self.numRemaining -= num

            if self.numRemaining < 0:
                self.numRemaining = 0

        else:
            self.numSignedUp -= num

            if(self.numSignedUp < 0):
                self.numSignedUp = 0

    def uncomplete(self, num):
        self.numCompleted -= num
        self.numRemaining += numd
        self.numCompleted = 0





        
        