import tensorflow as tf
from collections import deque
import random
import numpy as np
from Agent.Agent import Agent

from Environnement.Action import Action

class DQNAgent(Agent):
    def __init__(self,color='green',file=None, gamma=0.95, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01, learning_rate=0.001, batch_size=12):
        super().__init__(color)
        self.state_size = 6
        self.action_size = 3
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.learning_rate = learning_rate
        self.batch_size = batch_size

        self.memory = deque(maxlen=2000)
        self.model = self._build_model()
        if(file!=None) :
            self.load(file)

    def _build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(6, input_dim=self.state_size, activation='relu'),
            tf.keras.layers.Dense(6, activation='relu'),
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
        
        #choose to go left
        if actionInt == 0 :
            return actionInt,Action(self.id,'LEFT'),True
        #choose to go forward
        elif actionInt == 1 :
            return actionInt,Action(self.id,'STRAIGHT'),True
        #choose to go right
        elif actionInt == 2 :
            return actionInt,Action(self.id,'RIGHT'),True

    def getAction(self,state) :
        if np.random.rand() <= self.epsilon:
            actionInt = random.randrange(self.action_size)
        else :
            q_values = self.model.predict(np.array([state]))
            actionInt =  np.argmax(q_values[0]) 
        
        #choose to go left
        if actionInt == 0 :
            return Action(self.id,'LEFT'),True
        #choose to go forward
        elif actionInt == 1 :
            return Action(self.id,'STRAIGHT'),True
        #choose to go right
        elif actionInt == 2 :
            return Action(self.id,'RIGHT'),True

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
