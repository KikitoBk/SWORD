from Action import Action

class Agent : 
    def __init__(self,id) :
        self.id = id
    
    def getAction(self) :
        return Action(self.id,'UP'),False