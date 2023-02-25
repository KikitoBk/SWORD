from time import sleep,time
from Environnement.Snake import Snake
from Environnement.SnakeEnv import SnakeEnv
import concurrent.futures

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
                startTime = time()
                with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                    # submit the function and each object to the thread pool
                    futures = [executor.submit(agent.getAction, observations[i]) for i,agent in enumerate(self.agents)]

                    # iterate over the completed futures and retrieve their return values
                    for future in concurrent.futures.as_completed(futures):
                        action = future.result()
                        if(self.getAgentByID(action.id).useLocal) :
                            action.direction = self.localToGlobal(action,self.env.getSnake(action.id))
                        
                        actions.append(action)
                observations,_,_,_ = self.env.step(actions)
                self.env.render() 
                timeElapsed = time()-startTime
                sleepTime = self.tickInterval - timeElapsed
                if(sleepTime>0) :
                    sleep(sleepTime)
                    

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
    
    def getAgentByID(self,id) :
        for agent in self.agents :
            if(agent.id == id ) :
                return agent