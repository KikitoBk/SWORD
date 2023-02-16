from time import sleep
from PlayerAgent import PlayerAgent
from SnakeEnv import SnakeEnv

class GameManager:
    # TODO init env and snake and agent
    def __init__(self,tickInterval,agents,snakes) :
        self.env = SnakeEnv(20,20,snakes)
        self.agents = agents
        self.tickInterval = tickInterval
    
    def run(self) :
        while(not(self.env.done)) :
            actions = []
            for agent in self.agents :
                actions.append(agent.getAction())
            self.env.step(actions)
            self.env.render() 
            sleep(self.tickInterval)
        self.env.reset()
        self.run()

    