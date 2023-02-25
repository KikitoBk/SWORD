from Agent.DQNAgent import DQNAgent
from Agent.PlayerAgent import PlayerAgent
from GameManager.GameManager import GameManager

gridSizeX = 30
gridSizeY = 30
tickDuration = 0.10

# Here you can define as many players as you want
players = []
players.append(PlayerAgent())
players.append(DQNAgent('violet','weight/sword_v3_70.h5'))


game = GameManager(tickDuration,gridSizeX,gridSizeY,players)
game.run()