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
        state = self.env.reset()
        while(not(self.env.done)) :
            actions = []
            for agent in self.agents :
                action,isLocal = agent.getAction(state)
                if(isLocal) :
                    self.localToGlobal(action,self.env.getSnake(agent.id))
                actions.append(action)
                # print(agent.getAction().direction)
            state,_,_,_ = self.env.step(actions)
            self.env.render() 
            sleep(self.tickInterval)
        self.env.reset()
        sleep(1)
        self.run()

    def localToGlobal(self,action,snake) :
        leftBinding = {'UP': 'LEFT', 'DOWN': 'RIGHT', 'LEFT': 'DOWN', 'RIGHT': 'UP'}
        rightBinding = {'UP': 'RIGHT', 'DOWN': 'LEFT', 'LEFT': 'UP', 'RIGHT': 'DOWN'}

        #choose to go left
        if action.direction == 'LEFT' :
            action.direction = leftBinding[snake.direction]
        #choose to go forward
        elif action.direction == 'STRAIGHT' :
            action.direction == snake.direction
        #choose to go right
        elif action.direction == 'RIGHT' :
            action.direction = rightBinding[snake.direction]