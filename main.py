# from Grid import Grid 
from Snake import Snake

gridSizeX = 30
gridSizeY = 30 
interval = 0.10
snake1 = Snake('Joueur1',gridSizeX//3,gridSizeY//3,3,'green','q','d','z','s')
snake2 = Snake('Joueur2',gridSizeX//2,gridSizeY//2,3,'orange','j','l','i','k')
snakes = [snake1,snake2]
# grid = Grid(gridSizeX,gridSizeY,interval,snakes)