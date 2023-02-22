from time import sleep
from Environnement.Snake import Snake
from Environnement.SnakeEnv import SnakeEnv

class GameManager:
    def __init__(self,tickInterval,gridSizeX,gridSizeY,agents) :
        
        snakes = [Snake(agent.id,(gridSizeX//(len(agents)+1))*(i+1),gridSizeY//2,3,agent.color) for i,agent in enumerate(agents) ]
        
        self.env = SnakeEnv(gridSizeX,gridSizeY,snakes)
        self.agents = agents
        self.tickInterval = tickInterval
    
    def run(self) :
        while True :
            observations = self.env.reset()
            while(not(self.env.done)) :
                actions = []
                for i,agent in enumerate(self.agents) :
                    action,isLocal = agent.getAction(observations[i])
                    if(isLocal) :
                        action.direction = self.localToGlobal(action,self.env.getSnake(agent.id))
                    
                    actions.append(action)
                observations,_,_,_ = self.env.step(actions)
                self.env.render() 
                sleep(self.tickInterval)

    def localToGlobal(self,action,snake) :
        leftBinding = {'UP': 'LEFT', 'DOWN': 'RIGHT', 'LEFT': 'DOWN', 'RIGHT': 'UP'}
        rightBinding = {'UP': 'RIGHT', 'DOWN': 'LEFT', 'LEFT': 'UP', 'RIGHT': 'DOWN'}

        #choose to go left
        if action.direction == 'LEFT' :
            return leftBinding[snake.direction]
        #choose to go forward
        elif action.direction == 'STRAIGHT' :
            return snake.direction
        #choose to go right
        elif action.direction == 'RIGHT' :
            return  rightBinding[snake.direction]