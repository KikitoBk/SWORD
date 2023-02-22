from Environnement.Body import Body
from enum import Enum
from pynput import keyboard

class Snake :
    def __init__(self,id,x,y,length,color='green'):
        self.id = id
        self.xinit = x
        self.yinit = y
        self.x = self.xinit
        self.y = self.yinit
        self.color = color
        self.lengthinit = length
        self._bodyParts = [Body(x,y+l+1) for l in range(length)]
        self.direction = 'UP'
        self.lastRemoved = Body(x,y+length+1)
        self.lastPosition = Body(self.x,self.y)
        self.score = 0

    def getOccupiedSquares(self) :
        return ([(self.x,self.y)]+self.getTailSquares())
    
    def getTailSquares(self) :
        return [(body.x,body.y) for body in self._bodyParts]
    
    def step(self,action) :
        self.lastPosition.setPosition(self.x,self.y)
        self._bodyParts.insert(0,Body(self.x,self.y))
        self.lastRemoved = self._bodyParts.pop()

        directions = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}
        dx, dy = directions.get(self.direction)
        ax, ay = directions.get(action)
        
        if (ax,ay) != (-dx,-dy)  :
            self.x += ax
            self.y += ay
            self.direction = action
        else :
            self.x += dx
            self.y += dy

    def grow(self) :
        self._bodyParts.append(self.lastRemoved)
        self.score += 1

    def reset(self):
        self.x = self.xinit
        self.y = self.yinit
        self._bodyParts = [Body(self.x,self.y+l+1) for l in range(self.lengthinit)]
        self.direction = 'UP'
        self.lastRemoved = Body(self.x,self.y+self.lengthinit+1)
        self.length = self.lengthinit
        self.score = 0