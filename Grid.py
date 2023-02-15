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
        
            # Checking apple
            if(snake.x == self.appleX and snake.y == self.appleY) :
                snake.grow()
                self.canvas.itemconfig('score',text=str(snake.score))
                self.spawnApple()
                self.drawApple()
                
            # Checking collision with wall
            if(snake.x < 0 or snake.y < 0 or snake.x > self.sizeX or snake.y > self.sizeY) :
                print('Snake hit a wall')
                shouldStop |= True 

            # Checking collision with himself
            elif((snake.x,snake.y) in snake.getTailSquares()) :
                print('Snake hit himself')
                shouldStop |= True

            # TODO Checking collsion with others
            
            else :
                shouldStop |= False

            self.refreshSnake(snake)

        if(not(shouldStop)):
            Timer(self.tickInterval,self.onTick).start()

        #put score in first plan
        self.canvas.tag_raise('score')

    def drawGrid(self) :
        root = Tk()
        root.title('Snake')
        root.resizable(False,False)
        root.geometry('{}x{}'.format(self.XGridSize,self.YGridSize))
        self.canvas = Canvas(root,width=self.XGridSize,height=self.YGridSize,bg='black')
        self.canvas.pack()
        for snake in self.snakes :
            self.drawSnake(snake)
        self.drawApple()
        Timer(self.tickInterval,self.onTick).start()
        root.mainloop()

    # Draw the entire snake
    def drawSnake(self,snake) :
        for x,y in snake.getOccupiedSquares() :
            self.canvas.create_rectangle(x*self.squareSize,y*self.squareSize,x*self.squareSize+self.squareSize,y*self.squareSize+self.squareSize,fill=snake.color,tag=(str(snake.x)+','+str(snake.y)))
        self.canvas.create_text(snake.x*self.squareSize,snake.y*self.squareSize,fill='white',font=('Times',10),text=str(self.snakes[0].score),tags=('score'),width=50,anchor='w')
        
    # Only remove the last part of the snake and draw the head
    def refreshSnake(self,snake) :  
        # Last body part
        self.canvas.delete(str(snake.lastRemoved.x)+','+str(snake.lastRemoved.y))
        # Head
        self.canvas.create_rectangle(snake.x*self.squareSize,snake.y*self.squareSize,snake.x*self.squareSize+self.squareSize,snake.y*self.squareSize+self.squareSize,fill=snake.color,tag=(str(snake.x)+','+str(snake.y)))
        self.canvas.move('score',(snake.x-snake._bodyParts[0].x)*self.squareSize,(snake.y-snake._bodyParts[0].y)*self.squareSize)

    def drawApple(self) :
        self.canvas.delete('apple')
        self.canvas.create_rectangle(self.appleX*self.squareSize,self.appleY*self.squareSize,self.appleX*self.squareSize+self.squareSize,self.appleY*self.squareSize+self.squareSize,fill='red',tag='apple')