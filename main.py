# from Grid import Grid 
from Snake import Snake
from PlayerAgent import PlayerAgent
from GameManager import GameManager


gridSizeX = 30
gridSizeY = 30 
interval = 0.10

snake1 = Snake('player',gridSizeX//3,gridSizeY//3,3,'green')
player = PlayerAgent('player','q','z','d','s')

game = GameManager(interval,[player],[snake1])
game.run()