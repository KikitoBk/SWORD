from Body import Body
from enum import Enum
from pynput import keyboard
class Snake :
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self._bodyParts = [Body(x,y+l+1) for l in range(length)]
        self.actualDirection = Direction.UP
        self.nextDirection = Direction.UP
        self._lastRemoved = Body(x,y+length+1)

        self.score = 0

        def on_press(key) :
            charKey = key.char
            if(charKey==Direction.LEFT.value or charKey==Direction.RIGHT.value or charKey==Direction.UP.value or charKey==Direction.DOWN.value) :
                self.turn(Direction(charKey))

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
        if(self.nextDirection == Direction.LEFT) :
            self.x -= 1
        elif(self.nextDirection == Direction.UP) :
            self.y -= 1
        elif(self.nextDirection == Direction.RIGHT) :
            self.x += 1
        elif(self.nextDirection == Direction.DOWN) :
            self.y += 1
        self.actualDirection = self.nextDirection
    
    def grow(self) :
        self._bodyParts.append(self._lastRemoved)
        self.score += 1


    def turn(self,direction) :
        #print('turning',direction)
        #check if we can turn (not opposite direction)
        if(not( ((self.actualDirection == Direction.DOWN) and (direction == Direction.UP)) or ((self.actualDirection == Direction.UP) and (direction == Direction.DOWN)) or ((self.actualDirection == Direction.RIGHT) and (direction == Direction.LEFT)) or ((self.actualDirection == Direction.LEFT) and (direction == Direction.RIGHT)) ) ):
            self.nextDirection = direction

class Direction(Enum):
    LEFT = 'q'
    UP = 'z'
    RIGHT = 'd'
    DOWN = 's'

