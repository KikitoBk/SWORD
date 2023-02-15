from Snake import Snake
from random import randint
from threading import Timer
from tkinter import *

class Grid:
    def __init__(self,sizeX,sizeY,tickInterval,snakes):
        self.sizeX = sizeX -1
        self.sizeY = sizeY -1
        self.squareSize = 20
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
        allTailSquares = []
        for snake in self.snakes :
            snake.onTick()
            allTailSquares += snake.getTailSquares()
        allHeadSquares = [(snake.x,snake.y) for snake in self.snakes]
        for snake in self.snakes :
            
            # Checking apple
            if(snake.x == self.appleX and snake.y == self.appleY) :
                snake.grow()
                self.canvas.itemconfig('score_'+snake.id,text=str(snake.score))
                self.spawnApple()
                self.drawApple()
                
            # Checking collision with wall
            if(snake.x < 0 or snake.y < 0 or snake.x > self.sizeX or snake.y > self.sizeY) :
                print(snake.id+' hit a wall')
                shouldStop |= True 

            # Checking collision with snakes tails
            elif((snake.x,snake.y) in allTailSquares) :
                print(snake.id+' hit a snake tail')
                shouldStop |= True
            
            # Checking collision with head
            elif(allHeadSquares.count((snake.x,snake.y))>=2) :
                print(snake.id+' hit someoneelse head')
                shouldStop |= True  
            
            else :
                shouldStop |= False



            self.refreshSnake(snake)

        if(not(shouldStop)):
            Timer(self.tickInterval,self.onTick).start()

        else :
            #window score print and replay button
            self.canvas.create_rectangle(0,0,self.XGridSize,self.YGridSize,fill='black',tag='score')
            self.canvas.create_text(self.XGridSize/2,self.YGridSize//3-50,fill='white',font=('Times',self.squareSize if self.squareSize > 10 else 10),text='Click to Replay',tags=('score','score_'+snake.id),width=200,anchor='center')
            for i,snake in enumerate(self.snakes) :
                Label(self.root,text="score of player "+snake.id+" : "+str(snake.score),wraplength=0,bg='black',fg='white',anchor='center',font=('Times',self.squareSize if self.squareSize > 10 else 10)).place(x=20,y=self.YGridSize//3+50*i)
                #self.canvas.create_text(self.XGridSize//3,self.YGridSize//3+50*i,fill='white',font=('Times',self.squareSize if self.squareSize > 10 else 10),text="score of player "+snake.id+" : "+str(snake.score),width=None,tags=('score','score_'+snake.id),anchor='center')

            self.canvas.tag_raise('score')
            self.canvas.bind('<Button-1>',self.replay)
            
        
        #put score in first plan
        self.canvas.tag_raise('score')

    def replay(self,event):
        self.root.destroy()
        for snake in self.snakes :
            snake.reset()
        self.__init__(self.sizeX+1,self.sizeY+1,self.tickInterval,self.snakes)
        
        

    def drawGrid(self) :
        self.root = Tk()
        self.root.focus_force()

        self.root.title('SWORD')
        self.root.resizable(False,False)
        self.root.geometry('{}x{}+{}+{}'.format(self.XGridSize,self.YGridSize,20,20))
        self.canvas = Canvas(self.root,width=self.XGridSize,height=self.YGridSize,bg='black')
        self.canvas.pack()
        for snake in self.snakes :
            self.drawSnake(snake)
        self.drawApple()
        Timer(self.tickInterval,self.onTick).start()
        self.root.mainloop()

    # Draw the entire snake
    def drawSnake(self,snake) :
        for x,y in snake.getOccupiedSquares() :
            self.canvas.create_rectangle(x*self.squareSize,y*self.squareSize,x*self.squareSize+self.squareSize,y*self.squareSize+self.squareSize,fill=snake.color,tag=snake.id+':'+str(x)+','+str(y))
        self.canvas.create_text(snake.x*self.squareSize,snake.y*self.squareSize,fill='white',font=('Times',self.squareSize if self.squareSize > 10 else 10),text=str(self.snakes[0].score),tags=('score','score_'+snake.id),width=50,anchor='w')
        
    # Only remove the last part of the snake and draw the head
    def refreshSnake(self,snake) :  
        # Last body part
        self.canvas.delete(snake.id+':'+str(snake.lastRemoved.x)+','+str(snake.lastRemoved.y))
        # Head
        self.canvas.create_rectangle(snake.x*self.squareSize,snake.y*self.squareSize,snake.x*self.squareSize+self.squareSize,snake.y*self.squareSize+self.squareSize,fill=snake.color,tag=snake.id+':'+str(snake.x)+','+str(snake.y))
        self.canvas.move('score_'+snake.id,(snake.x-snake._bodyParts[0].x)*self.squareSize,(snake.y-snake._bodyParts[0].y)*self.squareSize)

    def drawApple(self) :
        self.canvas.delete('apple')
        self.canvas.create_rectangle(self.appleX*self.squareSize,self.appleY*self.squareSize,self.appleX*self.squareSize+self.squareSize,self.appleY*self.squareSize+self.squareSize,fill='red',tag='apple')