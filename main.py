from Grid import Grid 
from Snake import Snake

gridSizeX = 50
gridSizeY = 50 
interval = 0.05
snake1 = Snake(gridSizeX//2,gridSizeY//2,3,'green','q','d','z','s')
snake2 = Snake(gridSizeX//3,gridSizeY//3,3,'orange','j','l','i','k')
snakes = [snake1]
grid = Grid(gridSizeX,gridSizeY,interval,snakes)
