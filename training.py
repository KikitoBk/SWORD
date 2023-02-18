from time import sleep
import numpy as np
from Snake import Snake
from SnakeEnv import SnakeEnv
from DQNAgent import DQNAgent

# Create the Snake game environment
env = SnakeEnv(10,10,[Snake('AI',5,5,4)])

# Create the DQN agent
agent = DQNAgent(id='AI',epsilon=0.01)
agent.load('weight/v4/sword_v4_65.h5')
# Train the agent
num_episodes = 200
for episode in range(65,num_episodes):
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
    if(episode%10 == 0 and episode != 0 or episode > 20):
        agent.save('weight/v4/sword_v4_{}.h5'.format(episode+1))

# Save the trained model
