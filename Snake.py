from Body import Body
from enum import Enum

class Snake :
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self.bodyParts = []
        self.direction = Direction.UP
        for l in range(length) :
            self.bodyParts.append(Body(x,y-l-1))
    
    def onTick(self) : 
        self.bodyParts.insert(0,Body(self.x,self.y))
        self.bodyParts.pop()
        if(self.direction == Direction.LEFT) :
            self.x -= 1
        elif(self.direction == Direction.UP) :
            self.y += 1
        elif(self.direction == Direction.RIGHT) :
            self.x += 1
        elif(self.direction == Direction.DOWN) :
            self.y -= 1

class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4
