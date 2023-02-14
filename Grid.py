from Snake import Snake
from random import randint
from threading import Timer
from tkinter import *
from tkinter import messagebox

class Grid:
    def __init__(self,sizeX,sizeY,tickInterval):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.squareSize = 10
        self.XGridSize = sizeX * self.squareSize
        self.YGridSize = sizeY * self.squareSize
        self.snake = Snake(sizeX//2,sizeY//2,30)
        #self.snake2 = Snake(sizeX//3,sizeY//3,3)
        self.spawnApple()
        self.tickInterval = tickInterval
        self.drawGrid()
        
        

    def spawnApple(self): 
        occupiedSquare = self.snake.getOccupiedSquares()

        self.appleX = randint(0,self.sizeX-1)
        self.appleY = randint(0,self.sizeY-1)

        while((self.appleX,self.appleY) in occupiedSquare) :
            self.appleX = randint(0,self.sizeX-1)
            self.appleY = randint(0,self.sizeY-1)




        
    def onTick(self) :
        self.snake.onTick()
        #print(self.snake.getOccupiedSquares())
        #self.printGrind()
        
        if(self.snake.x == self.appleX and self.snake.y == self.appleY) :
            self.snake.grow()
            #change score text with tag 'score'
            self.canvas.itemconfig('score',text='Score: '+str(self.snake.score))

            self.spawnApple()
            self.drawApple()
            
        if(self.snake.x < 0 or self.snake.y < 0 or self.snake.x > self.sizeX or self.snake.y > self.sizeY) :
            print('Snake hit a wall')
        elif((self.snake.x,self.snake.y) in self.snake.getTailSquares()) :
            print('Snake hit himself')
        else :
            Timer(self.tickInterval,self.onTick).start()

        self.refreshSnake()

        #put score in first plan
        self.canvas.tag_raise('score')

        self.canvas.update()


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

    #tkinter to draw the grid
    def drawGrid(self) :
        root = Tk()
        root.title('Snake')
        root.resizable(False,False)
        root.geometry('{}x{}'.format(self.XGridSize,self.YGridSize))
        #root.bind('<Key>',self.onKeyPress)

        self.canvas = Canvas(root,width=self.XGridSize,height=self.YGridSize)
        self.canvas.pack()
        self.canvas.create_rectangle(0,0,self.XGridSize,self.YGridSize,fill='black')
        self.drawSnake()
        self.drawApple()
        self.drawScore()

        Timer(self.tickInterval,self.onTick).start()

        root.mainloop()


    def refreshSnake(self) :
        
        #erase the last part of the snake via lastremove
        self.canvas.create_rectangle(self.snake.lastRemoved.x*self.squareSize,self.snake.lastRemoved.y*self.squareSize,self.snake.lastRemoved.x*self.squareSize+self.squareSize,self.snake.lastRemoved.y*self.squareSize+self.squareSize,fill='black')
        #draw the head of the snake
        self.canvas.create_rectangle(self.snake.x*self.squareSize,self.snake.y*self.squareSize,self.snake.x*self.squareSize+self.squareSize,self.snake.y*self.squareSize+self.squareSize,fill='green')




    def drawSnake(self) :
        for x,y in self.snake.getOccupiedSquares() :
            self.canvas.create_rectangle(x*self.squareSize,y*self.squareSize,x*self.squareSize+self.squareSize,y*self.squareSize+self.squareSize,fill='green')
        
    def drawApple(self) :
        self.canvas.create_rectangle(self.appleX*self.squareSize,self.appleY*self.squareSize,self.appleX*self.squareSize+self.squareSize,self.appleY*self.squareSize+self.squareSize,fill='red')

    def drawScore(self) :
        self.textScore = self.canvas.create_text(50,20,fill='white',font='Times 20',text='Score: '+str(self.snake.score),tag='score',width=200)
        

