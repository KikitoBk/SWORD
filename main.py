from Agent.DQNAgent import DQNAgent
from Agent.PlayerAgent import PlayerAgent
from GameManager.GameManager import GameManager

gridSizeX = 20
gridSizeY = 20
tickDuration = 0.15

# Here you can define as many players as you want
players = []
players.append(DQNAgent('green','weight/sword_v3_70.h5'))
players.append(PlayerAgent('blue'))


game = GameManager(tickDuration,gridSizeX,gridSizeY,players)
game.run()