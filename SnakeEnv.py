from threading import Timer
from time import sleep
from tkinter import *
from random import randint
import math

class SnakeEnv : 
    def __init__(self,sizeX,sizeY,snakes):
        self.sizeX = sizeX -1
        self.sizeY = sizeY -1
        self.squareSize = 20
        self.XGridSize = sizeX * self.squareSize
        self.YGridSize = sizeY * self.squareSize
        self.snakes = snakes
        self.done = False
        self._spawnApple()
    
    def reset(self):
        if hasattr(self,'root') :
            self.root.destroy()
            del self.root
        for snake in self.snakes :
            snake.reset()
        self.__init__(self.sizeX+1,self.sizeY+1,self.snakes)
        return self._getObservations()
        
    def step(self,actions):
        #Applying actions
        for snake in self.snakes :
            for action in actions : 
                if(snake.id == action.id) :
                    snake.step(action.direction)
        reward = []
        for snake in self.snakes :
            # Checking apple
            if(snake.x == self.appleX and snake.y == self.appleY) :
                snake.grow()
                self.canvas.itemconfig('score_'+snake.id,text=str(snake.score))
                self._spawnApple()
                self._refreshApple()
                
                reward.append(15)
                
            if(self._isColliding(snake.x,snake.y)) :
                self.done |= True
                reward.append(-30)
            else :
                if(abs(snake.lastPosition.x-self.appleX) > abs(snake.x - self.appleX) or abs(snake.lastPosition.y-self.appleY) > abs(snake.y - self.appleY)) :
                    reward.append(1)
                else :
                    reward.append(-3)

                # reward.append((self._getMaxDistance()-self._distanceFrom(snake.x,snake.y,self.appleX,self.appleY))*10/self._getMaxDistance())
                # rew = int(not(snake.x > self.appleX)) + int(not(snake.x < self.appleX))+int(not(snake.y > self.appleY))+int(not(snake.y < self.appleY))
                # reward.append(rew)
        # print(reward[0])
        return self._getObservations(),reward[0],self.done, {}
     
    
    def render(self):
        if not(hasattr(self,'root')) :
            self._displayWindow()
            sleep(1)
        for snake in self.snakes :
            self._refreshSnake(snake)
        self.canvas.tag_raise('score')
        self.root.update_idletasks()
        self.root.update()
    
    def _getObservations(self) :

        directions = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}
        x,y = self.snakes[0].x,self.snakes[0].y
        dx,dy = directions[self.snakes[0].direction]

        obs = [
            
            #nearest left danger
            # self._nearestDanger(x,y,-dy,dx),
            int(self._isColliding(x-dy,y+dx)),
                       
            #nearest forward danger
            # self._nearestDanger(x,y,dx,dy),
            int(self._isColliding(x+dx,y+dy)),


            #nearest right danger
            # self._nearestDanger(x,y,dy,-dx),
            int(self._isColliding(x+dy,y-dx)),


            # Actual direction
            int(self.snakes[0].direction == 'UP'),
            int(self.snakes[0].direction == 'DOWN'),
            int(self.snakes[0].direction == 'LEFT'),
            int(self.snakes[0].direction == 'RIGHT'),

            #Distance to apple
            int(self.snakes[0].x - self.appleX),
            int(self.snakes[0].y - self.appleY),
        ]
        # print(obs)
        return obs
        
    
    def _isColliding(self,x,y) :
        allTailSquares = []
        for snake in self.snakes :
            allTailSquares += snake.getTailSquares()
        allHeadSquares = [(snake.x,snake.y) for snake in self.snakes]
        # Checking collision with wall
        if(x < 0 or y < 0 or x > self.sizeX or y > self.sizeY) :
            return True

        # Checking collision with snakes tails
        if((x,y) in allTailSquares) :
            return True

        # Checking collision with head
        if (allHeadSquares.count((x,y))>=2) :
            return True
        
        return False

    def _nearestDanger(self,baseX,baseY,deltaX,deltaY) :
        if (self._isColliding(baseX,baseY)) :
            return 0
        else :
            return self._nearestDanger(baseX+deltaX,baseY+deltaY,deltaX,deltaY) + 1

    def _distanceFrom(self,sourceX,sourceY,targetX,targetY) :
        return abs(targetX - sourceX) + abs(targetY - sourceY)
    
    def _getMaxDistance(self) :
        return math.sqrt(pow(self.sizeX,2)+pow(self.sizeY,2))
    
    def _displayWindow(self) :
        self.root = Tk()
        self.root.focus_force()

        self.root.title('SWORD')
        self.root.resizable(False,False)
        self.root.geometry('{}x{}+{}+{}'.format(self.XGridSize,self.YGridSize,20,20))
        self.canvas = Canvas(self.root,width=self.XGridSize,height=self.YGridSize,bg='black')
        self.canvas.pack()
        self._refreshApple()
        for snake in self.snakes :
            self._drawSnake(snake)
        # Timer(self.tickInterval,self.onTick).start()
        self.root.update_idletasks()
        self.root.update()
        
    # Draw the entire snake
    def _drawSnake(self,snake) :
        for x,y in snake.getOccupiedSquares() :
            self.canvas.create_rectangle(x*self.squareSize,y*self.squareSize,x*self.squareSize+self.squareSize,y*self.squareSize+self.squareSize,fill=snake.color,tag=snake.id+':'+str(x)+','+str(y))
        self.canvas.create_text(snake.x*self.squareSize,snake.y*self.squareSize,fill='white',font=('Times',self.squareSize if self.squareSize > 10 else 10),text=str(snake.score),tags=('score','score_'+snake.id),width=50,anchor='w')
        
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