from threading import Timer
from tkinter import *
from random import randint

class SnakeEnv : 
    def __init__(self,sizeX,sizeY,snakes):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.squareSize = 20
        self.XGridSize = sizeX * self.squareSize
        self.YGridSize = sizeY * self.squareSize
        self.snakes = snakes
        self.done = False
        self.spawnApple()
        self._displayWindow()
    
    def reset(self):
        self.root.destroy()
        for snake in self.snakes :
            snake.reset()
        self.__init__(self.sizeX,self.sizeY,self.snakes)
        
    def step(self,action):
        allTailSquares = []
        for snake in self.snakes :
            if(snake.id == action.id) :
                snake.step(action.direction)    
            allTailSquares += snake.getTailSquares()
        allHeadSquares = [(snake.x,snake.y) for snake in self.snakes]
        
        for snake in self.snakes :
            
            # Checking apple
            if(snake.x == self.appleX and snake.y == self.appleY) :
                snake.grow()
                self.canvas.itemconfig('score_'+snake.id,text=str(snake.score))
                self.spawnApple()
                self._refreshApple()
                reward = 1
                
            # Checking collision with wall
            if(snake.x < 0 or snake.y < 0 or snake.x > self.sizeX or snake.y > self.sizeY) :
                self.done = True
                reward = -1

            # Checking collision with snakes tails
            elif((snake.x,snake.y) in allTailSquares) :
                self.done = True
                reward = -1
            
            # Checking collision with head
            elif(allHeadSquares.count((snake.x,snake.y))>=2) :
                self.done = True
                reward = -1 
            
            else :
                reward = 0

            self._refreshSnake(snake)
            return self._getObservations(),reward,self.done, {}
     
    
    def render(self):
        # self._refreshApple()
        # for snake in self.snakes :
        #     self._refreshSnake(snake)
        self.canvas.tag_raise('score')
        self.root.update_idletasks()
        self.root.update()
    
    def _getObservations(self) :
        
        
        state = [
            # TODO 
            # Actual direction
            
            #Apple location 
            self.snakes[0].x > self.appleX,
            self.snakes[0].x > self.appleX,
            self.snakes[0].y > self.appleY,
            self.snakes[0].y < self.appleY  
        ]
    
    def _displayWindow(self) :
        self.root = Tk()
        self.root.focus_force()

        self.root.title('SWORD')
        self.root.resizable(False,False)
        self.root.geometry('{}x{}+{}+{}'.format(self.XGridSize,self.YGridSize,20,20))
        self.canvas = Canvas(self.root,width=self.XGridSize,height=self.YGridSize,bg='black')
        self.canvas.pack()
        for snake in self.snakes :
            self._drawSnake(snake)
        Timer(self.tickInterval,self.onTick).start()
        self.root.update_idletasks()
        self.root.update()
        
    # Draw the entire snake
    def _drawSnake(self,snake) :
        for x,y in snake.getOccupiedSquares() :
            self.canvas.create_rectangle(x*self.squareSize,y*self.squareSize,x*self.squareSize+self.squareSize,y*self.squareSize+self.squareSize,fill=snake.color,tag=snake.id+':'+str(x)+','+str(y))
        self.canvas.create_text(snake.x*self.squareSize,snake.y*self.squareSize,fill='white',font=('Times',self.squareSize if self.squareSize > 10 else 10),text=str(self.snakes[0].score),tags=('score','score_'+snake.id),width=50,anchor='w')
        
    # Only remove the last part of the snake and draw the head
    def _refreshSnake(self,snake) :  
        # Last body part
        self.canvas.delete(snake.id+':'+str(snake.lastRemoved.x)+','+str(snake.lastRemoved.y))
        # Head
        self.canvas.create_rectangle(snake.x*self.squareSize,snake.y*self.squareSize,snake.x*self.squareSize+self.squareSize,snake.y*self.squareSize+self.squareSize,fill=snake.color,tag=snake.id+':'+str(snake.x)+','+str(snake.y))
        self.canvas.move('score_'+snake.id,(snake.x-snake._bodyParts[0].x)*self.squareSize,(snake.y-snake._bodyParts[0].y)*self.squareSize)

    def _refreshApple(self) :
        self.canvas.delete('apple')
        self.canvas.create_rectangle(self.appleX*self.squareSize,self.appleY*self.squareSize,self.appleX*self.squareSize+self.squareSize,self.appleY*self.squareSize+self.squareSize,fill='red',tag='apple')

    def _spawnApple(self,x=None,y=None): 
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
                self._spawnApple()