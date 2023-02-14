from Snake import Snake
from random import randint
from threading import Timer
from tkinter import *

class Grid:
    def __init__(self,sizeX,sizeY,tickInterval,snakes):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.squareSize = 10
        self.XGridSize = sizeX * self.squareSize
        self.YGridSize = sizeY * self.squareSize
        self.snakes = snakes
        self.spawnApple()
        self.tickInterval = tickInterval
        self.drawGrid()

    def spawnApple(self,x=None,y=None): 
        occupiedSquares = []
        for snake in self.snakes :
            occupiedSquares.extend(snake.getOccupiedSquares())

        if(x==None and y==None) :
            self.appleX = randint(0,self.sizeX-1)
            self.appleY = randint(0,self.sizeY-1)

            while((self.appleX,self.appleY) in occupiedSquares) :
                self.appleX = randint(0,self.sizeX-1)
                self.appleY = randint(0,self.sizeY-1)
        else :
            if((x,y) not in occupiedSquares) :
                self.appleX = x
                self.appleY = y
            else :
                self.spawnApple()

    def onTick(self) :
        shouldStop = False
        for snake in self.snakes :
            snake.onTick()
        
            if(snake.x == self.appleX and snake.y == self.appleY) :
                snake.grow()
                self.spawnApple()
                
            if(snake.x < 0 or snake.y < 0 or snake.x > self.sizeX or snake.y > self.sizeY) :
                print('Snake hit a wall')
            elif((snake.x,snake.y) in snake.getTailSquares()) :
                print('Snake hit himself')
            else :
                shouldStop = True

        self.refreshGrid()
        if(not(shouldStop)):
            Timer(self.tickInterval,self.onTick).start()

    def drawGrid(self) :
        root = Tk()
        root.title('Snake')
        root.resizable(False,False)
        root.geometry('{}x{}'.format(self.XGridSize,self.YGridSize))
        self.canvas = Canvas(root,width=self.XGridSize,height=self.YGridSize)
        self.canvas.pack()
        self.canvas.create_rectangle(0,0,self.XGridSize,self.YGridSize,fill='black')
        self.drawSnake()
        self.drawApple()
        self.drawScore()

        Timer(self.tickInterval,self.onTick).start()
        root.mainloop()

    def refreshGrid(self) :
        self.canvas.delete('all')
        self.canvas.create_rectangle(0,0,self.XGridSize,self.YGridSize,fill='black')
        self.drawSnake()
        self.drawApple()
        self.drawScore()

    def drawSnake(self) :
        for x,y in self.snake.getOccupiedSquares() :
            self.canvas.create_rectangle(x*self.squareSize,y*self.squareSize,x*self.squareSize+self.squareSize,y*self.squareSize+self.squareSize,fill='green')
        
    def drawApple(self) :
        self.canvas.create_rectangle(self.appleX*self.squareSize,self.appleY*self.squareSize,self.appleX*self.squareSize+self.squareSize,self.appleY*self.squareSize+self.squareSize,fill='red')

    def drawScore(self) :
        self.canvas.create_text(50,20,fill='white',font='Times 20',text='Score: '+str(self.snake.score))
        

