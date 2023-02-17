from time import sleep
import numpy as np
from Snake import Snake
from SnakeEnv import SnakeEnv
from DQNAgent import DQNAgent

# Create the Snake game environment
env = SnakeEnv(10,10,[Snake('AI',5,5,4)])

# Create the DQN agent
agent = DQNAgent('AI',epsilon=0.01)
agent.load('weight/sword_v2.h5')
# Train the agent
num_episodes = 10
for episode in range(num_episodes):
    state = env.reset()
    sleep(1)
    
    done = False
    score = 0
    while not done:
        actionInt, action = agent.act(state)
        next_state, reward, done, _ = env.step([action])
        env.render()
        agent.remember(state, actionInt, reward, next_state, done)
        state = next_state
        score += reward
        if done:
            print(f"episode: {episode+1}/{num_episodes}, score: {score}, epsilon: {agent.epsilon:.2f}")
        agent.replay()
    agent.save('weight/sword_v3_{}.h5'.format(episode+1))

# Save the trained model
