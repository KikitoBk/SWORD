from time import sleep
import numpy as np
from Snake import Snake
from SnakeEnv import SnakeEnv
from DQNAgent import DQNAgent

# Create the Snake game environment
env = SnakeEnv(10,10,[Snake('AI',5,5,4)])

# Set the state size and action size
state_size = 11

# Create the DQN agent
agent = DQNAgent('AI',epsilon_decay=0.997)

# Train the agent
num_episodes = 50
for episode in range(num_episodes):
    state = env.reset()
    # state = np.reshape(state, [1, state_size])
    done = False
    score = 0
    while not done:
        actionInt, action = agent.act(state)
        next_state, reward, done, _ = env.step([action])
        env.render()
        # next_state = np.reshape(next_state, [1, state_size])
        agent.remember(state, actionInt, reward, next_state, done)
        state = next_state
        score += reward
        if done:
            print(f"episode: {episode+1}/{num_episodes}, score: {score}, epsilon: {agent.epsilon:.2f}")
        agent.replay()
    sleep(1)

# Save the trained model
agent.save('snake_dqn.h5')
