# from Grid import Grid 
from DQNAgent import DQNAgent
from Snake import Snake
from PlayerAgent import PlayerAgent
from GameManager import GameManager


gridSizeX = 30
gridSizeY = 30
interval = 0.025
snake1 = Snake('AI',gridSizeX//3,gridSizeY//3,3,'green')
snake2 = Snake('player2',gridSizeX//2,gridSizeY//2,3,'yellow')
dqn = DQNAgent('AI','weight/v4/sword_v4_72.h5',epsilon=0)
player2 = PlayerAgent('player2','q','z','d','s')

game = GameManager(interval,gridSizeX,gridSizeY,[dqn],[snake1])
game.run()