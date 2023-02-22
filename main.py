# from Grid import Grid 
from Agent.DQNAgent import DQNAgent
from Environnement.Snake import Snake
from Agent.PlayerAgent import PlayerAgent
from GameManager.GameManager import GameManager

gridSizeX = 20
gridSizeY = 20
interval = 0.15
dqn2 = DQNAgent('green','weight/sword_v3_70.h5',epsilon=0)
dqn = DQNAgent('yellow','weight/sword_v3_70.h5',epsilon=0)
game = GameManager(interval,gridSizeX,gridSizeY,[dqn,dqn2])
game.run()