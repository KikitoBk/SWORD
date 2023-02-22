from Environnement.Action import Action

class Agent : 
    counter = 0
    
    def __init__(self,color="green") :
        self.id = str(Agent.counter)
        self.color = color
        Agent.counter+=1
    
    def getAction(self) :
        return Action(self.id,'UP'),False