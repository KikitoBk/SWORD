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
        self.DIRECTION = Enum('Direction',{'LEFT':leftKey,'RIGHT':rightKey,'UP':upKey,'DOWN':downKey})
        self._bodyParts = [Body(x,y+l+1) for l in range(length)]
        self.actualDirection = self.DIRECTION.UP
        self.nextDirection = self.DIRECTION.UP
        self.lastRemoved = Body(x,y+length+1)

        self.score = 0

        def on_press(key) :
            if hasattr(key, 'char'):
                charKey = key.char
                if(charKey==self.DIRECTION.LEFT.value or charKey==self.DIRECTION.RIGHT.value or charKey==self.DIRECTION.UP.value or charKey==self.DIRECTION.DOWN.value) :
                    self.turn(self.DIRECTION(charKey))

        #Listen to keyboard inputs
        listeners = keyboard.Listener(on_press=on_press)
        listeners.start()
            
    def getOccupiedSquares(self) :
        return ([(self.x,self.y)]+self.getTailSquares())
    
    def getTailSquares(self) :
        return [(body.x,body.y) for body in self._bodyParts]
    
    def onTick(self) : 
        self._bodyParts.insert(0,Body(self.x,self.y))
        self.lastRemoved = self._bodyParts.pop()
        if(self.nextDirection == self.DIRECTION.LEFT) :

            self.x -= 1
        elif(self.nextDirection == self.DIRECTION.UP) :
            self.y -= 1
        elif(self.nextDirection == self.DIRECTION.RIGHT) :
            self.x += 1
        elif(self.nextDirection == self.DIRECTION.DOWN) :
            self.y += 1
        self.actualDirection = self.nextDirection
    
    def grow(self) :
        self._bodyParts.append(self.lastRemoved)
        self.score += 1


    def turn(self,direction) :
        #check if we can turn (not opposite direction)
        if(not( ((self.actualDirection == self.DIRECTION.DOWN) and (direction == self.DIRECTION.UP)) or ((self.actualDirection == self.DIRECTION.UP) and (direction == self.DIRECTION.DOWN)) or ((self.actualDirection == self.DIRECTION.RIGHT) and (direction == self.DIRECTION.LEFT)) or ((self.actualDirection == self.DIRECTION.LEFT) and (direction == self.DIRECTION.RIGHT)) ) ):
            self.nextDirection = direction

    def reset(self):
        self.x = self.xinit
        self.y = self.yinit
        self._bodyParts = [Body(self.x,self.y+l+1) for l in range(self.lengthinit)]
        self.actualDirection = self.DIRECTION.UP
        self.nextDirection = self.DIRECTION.UP
        self.lastRemoved = Body(self.x,self.y+self.lengthinit+1)
        self.length = self.lengthinit
        self.score = 0

# class Direction(Enum):
#     LEFT = 'q'
#     UP = 'z'
#     RIGHT = 'd'
#     DOWN = 's'

