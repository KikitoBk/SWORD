# from Grid import Grid 
from DQNAgent import DQNAgent
from Snake import Snake
from PlayerAgent import PlayerAgent
from GameManager import GameManager


gridSizeX = 30
gridSizeY = 30
interval = 0.10
snake1 = Snake('player',gridSizeX//3,gridSizeY//3,3,'green')
snake2 = Snake('player2',gridSizeX//2,gridSizeY//2,3,'yellow')
player = PlayerAgent('player','q','z','d','s')
player2 = PlayerAgent('player2','j','i','l','k')

game = GameManager(interval,gridSizeX,gridSizeY,[player,player2],[snake1,snake2])
game.run()