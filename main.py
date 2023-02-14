from Grid import Grid 
from Snake import Snake

gridSizeX = 50
gridSizeY = 50 
interval = 0.05
# Snake(gridSizeX//2,gridSizeY//2,3)
snakes = [Snake(gridSizeX//2,gridSizeY//2,3,'q','d','z','s'),Snake(gridSizeX//3,gridSizeY//3,3,'j','l','i','k')]
grid = Grid(gridSizeX,gridSizeY,interval,snakes)
