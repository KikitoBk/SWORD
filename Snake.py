from Body import Body
from enum import Enum

class Snake :
    #TODO add keyboard input listener (natif way if possible)
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self._bodyParts = []
        self.direction = Direction.UP
        for l in range(length) :
            self._bodyParts.append(Body(x,y+l+1))
        self._lastRemoved = Body(x,y+length+1)
        
        
            
    def getOccupiedSquares(self) :
        occupiedSquare = [(self.x,self.y)]
        occupiedSquare.extend(self.getTailSquares())
        return occupiedSquare
    
    def getTailSquares(self) :
        return [(body.x,body.y) for body in self._bodyParts]
    
    def onTick(self) : 
        self._bodyParts.insert(0,Body(self.x,self.y))
        self._lastRemoved = self._bodyParts.pop()
        if(self.direction == Direction.LEFT) :
            self.x -= 1
        elif(self.direction == Direction.UP) :
            self.y -= 1
        elif(self.direction == Direction.RIGHT) :
            self.x += 1
        elif(self.direction == Direction.DOWN) :
            self.y += 1
    
    def grow(self) :
        self._bodyParts.append(self._lastRemoved)

class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4
