from time import sleep
from PlayerAgent import PlayerAgent
from SnakeEnv import SnakeEnv

class GameManager:
    # TODO init env and snake and agent
    def __init__(self,tickInterval,gridSizeX,gridSizeY,agents,snakes) :
        self.env = SnakeEnv(gridSizeX,gridSizeY,snakes)
        self.agents = agents
        self.tickInterval = tickInterval
    
    def run(self) :
        observations = self.env.reset()
        while(not(self.env.done)) :
            actions = []
            for i,agent in enumerate(self.agents) :
                actions.append(agent.getAction(observations[i]))
                # print(agent.getAction().direction)
            observations,_,_,_ = self.env.step(actions)
            self.env.render() 
            sleep(self.tickInterval)
        self.env.reset()
        sleep(1)
        self.run()

    