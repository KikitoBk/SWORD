from Agent import Agent
from pynput import keyboard
from Action import Action


class PlayerAgent (Agent):
    def __init__(self,id,leftKey,upKey,rigthKey,downKey) :
        super().__init__(id)
        self.direction = 'UP'
        self.keyBinding = dict()
        self.keyBinding[leftKey] = 'LEFT'
        self.keyBinding[upKey] = 'UP'
        self.keyBinding[rigthKey] = 'RIGHT'
        self.keyBinding[downKey] = 'DOWN'

        #Listen to keyboard inputs
        listeners = keyboard.Listener(on_press=self._on_press)
        listeners.start()

    def _on_press(self,key) :
        if hasattr(key, 'char'):
            self.direction = self.keyBinding.get(key.char,self.direction)

    def getAction(self,state):
        return Action(self.id,self.direction)