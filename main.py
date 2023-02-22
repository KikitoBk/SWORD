# from Grid import Grid 
from Agent.DQNAgent import DQNAgent
from Environnement.Snake import Snake
from Agent.PlayerAgent import PlayerAgent
from GameManager.GameManager import GameManager

gridSizeX = 20
gridSizeY = 20
interval = 0.15
snake1 = Snake('AI',gridSizeX//3,gridSizeY//3,3,'green')
snake2 = Snake('AI2',gridSizeX//2,gridSizeY//2,3,'yellow')
dqn2 = DQNAgent('AI2','weight/sword_v3_70.h5',epsilon=0)
dqn = DQNAgent('AI','weight/sword_v3_70.h5',epsilon=0)

game = GameManager(interval,gridSizeX,gridSizeY,[dqn,dqn2],[snake1,snake2])
game.run()