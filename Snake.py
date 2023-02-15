from Body import Body
from enum import Enum
from pynput import keyboard

class Snake :
    def __init__(self,id,x,y,length,color='green',leftKey='q',rightKey='d',upKey='z',downKey='s'):
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
        self.score = 0
            
    def getOccupiedSquares(self) :
        return ([(self.x,self.y)]+self.getTailSquares())
    
    def getTailSquares(self) :
        return [(body.x,body.y) for body in self._bodyParts]
    
    def step(self,action) :
        self._bodyParts.insert(0,Body(self.x,self.y))
        self.lastRemoved = self._bodyParts.pop()
        if(action == 'UP' and self.direction != 'DOWN') :
            self.y -= 1
        elif(action == 'DOWN' and self.direction != 'UP') :
            self.y += 1
        elif(action == 'LEFT' and self.direction != 'RIGHT') :
            self.x -= 1
        elif(action == 'RIGHT' and self.direction != 'LEFT') :
            self.x += 1
    
    def grow(self) :
        self._bodyParts.append(self.lastRemoved)
        self.score += 1

    def reset(self):
        self.x = self.xinit
        self.y = self.yinit
        self._bodyParts = [Body(self.x,self.y+l+1) for l in range(self.lengthinit)]
        self.actualDirection = self.DIRECTION.UP
        self.nextDirection = self.DIRECTION.UP
        self.lastRemoved = Body(self.x,self.y+self.lengthinit+1)
        self.length = self.lengthinit
        self.score = 0