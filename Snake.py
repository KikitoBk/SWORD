from Body import Body
from enum import Enum
from pynput import keyboard
class Snake :
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self._bodyParts = [Body(x,y+l+1) for l in range(length)]
        self.direction = Direction.UP
        self._lastRemoved = Body(x,y+length+1)

        def on_press(key) :
            if(key==Direction.LEFT.value or key==Direction.RIGHT.value or key==Direction.UP.value or key==Direction.DOWN.value) :
                self.turn(Direction(key))

        #Listen to keyboard inputs
        listeners = keyboard.Listener(on_press=on_press)
        listeners.start()
            
    def getOccupiedSquares(self) :
        return ([(self.x,self.y)]+self.getTailSquares())
    
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

    def turn(self,direction) :
        self.direction = direction

class Direction(Enum):
    LEFT = 'q'
    UP = 'z'
    RIGHT = 'd'
    DOWN = 's'