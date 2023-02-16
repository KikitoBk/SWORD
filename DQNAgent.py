import tensorflow as tf
from collections import deque
import random
import numpy as np

from Action import Action

class DQNAgent:
    def __init__(self,id, gamma=0.95, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01, learning_rate=0.001, batch_size=32):
        self.id = id
        self.state_size = 11
        self.action_size = 3
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.learning_rate = learning_rate
        self.batch_size = batch_size

        self.memory = deque(maxlen=2000)
        self.model = self._build_model()

    def _build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(32, input_dim=self.state_size, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(self.action_size, activation='linear')
        ])
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            actionInt = random.randrange(self.action_size)
        else :
            q_values = self.model.predict(np.array([state]))
            actionInt = np.argmax(q_values[0])
        
        if(state[3]) :
            actualDirection = 'UP'
        elif(state[4]) :
            actualDirection = 'DOWN'
        elif(state[5]) :
            actualDirection = 'LEFT'
        elif(state[6]) :
            actualDirection = 'RIGHT'
        
        leftBinding = {'UP': 'LEFT', 'DOWN': 'RIGHT', 'LEFT': 'DOWN', 'RIGHT': 'UP'}
        rightBinding = {'UP': 'RIGHT', 'DOWN': 'LEFT', 'LEFT': 'UP', 'RIGHT': 'DOWN'}

        #choose to go left
        if actionInt == 0 :
            return actionInt,Action(self.id,leftBinding[actualDirection])
        #choose to go forward
        elif actionInt == 1 :
            return actionInt,Action(self.id,actualDirection)
        #choose to go right
        elif actionInt == 2 :
            return actionInt,Action(self.id,rightBinding[actualDirection])

    def getAction(self,state) :
        if np.random.rand() <= self.epsilon:
            actionInt = random.randrange(self.action_size)
        else :
            q_values = self.model.predict(np.array([state]))
            actionInt =  np.argmax(q_values[0]) 
        
        if(state[3]) :
            actualDirection = 'UP'
        elif(state[4]) :
            actualDirection = 'DOWN'
        elif(state[5]) :
            actualDirection = 'LEFT'
        elif(state[6]) :
            actualDirection = 'RIGHT'
        
        leftBinding = {'UP': 'LEFT', 'DOWN': 'RIGHT', 'LEFT': 'DOWN', 'RIGHT': 'UP'}
        rightBinding = {'UP': 'RIGHT', 'DOWN': 'LEFT', 'LEFT': 'UP', 'RIGHT': 'DOWN'}

        #choose to go left
        if actionInt == 0 :
            return Action(self.id,leftBinding[actualDirection])
        #choose to go forward
        elif actionInt == 1 :
            return Action(self.id,actualDirection)
        #choose to go right
        elif actionInt == 2 :
            return Action(self.id,rightBinding[actualDirection])

    def replay(self):
        if len(self.memory) < self.batch_size:
            return
        minibatch = random.sample(self.memory, self.batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(np.array([next_state]))[0])
            target_f = self.model.predict(np.array([state]))
            target_f[0][action] = target
            self.model.fit(np.array([state]), target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)