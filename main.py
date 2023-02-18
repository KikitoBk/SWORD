# from Grid import Grid 
from DQNAgent import DQNAgent
from Snake import Snake
from PlayerAgent import PlayerAgent
from GameManager import GameManager


gridSizeX = 10
gridSizeY = 10
interval = 0.05
snake1 = Snake('AI',gridSizeX//3,gridSizeY//3,3,'green')
snake2 = Snake('AI2',gridSizeX//2,gridSizeY//2,3,'yellow')
dqn = DQNAgent('AI','weight/sword_v2.h5',epsilon=0)
dqn2 = DQNAgent('AI2','weight/sword_v2.h5',epsilon=0)

game = GameManager(interval,gridSizeX,gridSizeY,[dqn,dqn2],[snake1,snake2])
game.run()