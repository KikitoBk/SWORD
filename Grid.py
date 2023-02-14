from Snake import Snake
from random import randint
from threading import Timer
class Grid:
    def __init__(self,sizeX,sizeY,tickInterval):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.snake = Snake(5,5,3)
        self.spawnApple()
        self.tickInterval = tickInterval
        Timer(tickInterval,self.onTick).start()

    def spawnApple(self): 
        occupiedSquare = self.snake.getOccupiedSquares()

        self.appleX = randint(0,self.sizeX-1)
        self.appleY = randint(0,self.sizeY-1)

        while((self.appleX,self.appleY) in occupiedSquare) :
            self.appleX = randint(0,self.sizeX-1)
            self.appleY = randint(2,self.sizeY-1)




        
    def onTick(self) :
        self.snake.onTick()
        #print(self.snake.getOccupiedSquares())
        self.printGrind()
        if(self.snake.x == self.appleX and self.snake.y == self.appleY) :
            self.snake.grow()
            self.spawnApple()
            
        if(self.snake.x < 0 or self.snake.y < 0 or self.snake.x > self.sizeX or self.snake.y > self.sizeY) :
            print('Snake hit a wall')
        elif((self.snake.x,self.snake.y) in self.snake.getTailSquares()) :
            print('Snake hit himself')
        else :
            Timer(self.tickInterval,self.onTick).start()


    def printGrind(self) :
        print('+'+'-'*self.sizeX+'+')
        for y in range(self.sizeY) :
            line = '|'
            for x in range(self.sizeX) :
                if((x,y) in self.snake.getOccupiedSquares()) :
                    line += 'O'
                elif(x == self.appleX and y == self.appleY) :
                    line += 'A'
                else :
                    line += ' '
            line += '|'
            print(line)
        print('+'+'-'*self.sizeX+'+')

