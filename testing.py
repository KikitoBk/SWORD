import numpy as np
from SnakeEnv import SnakeEnv
from DQNAgent import DQNAgent

# Create the Snake game environment
env = SnakeEnv()

# Set the state size and action size
state_size = env.observation_space.shape[0]
action_size = env.action_space.n

# Load the trained DQN agent
agent = DQNAgent(state_size, action_size)
agent.load('snake_dqn.h5')

# Play the game using the trained agent
state = env.reset()
state = np.reshape(state, [1, state_size])
done = False
score = 0
while not done:
    action = agent.act(state)
    next_state, reward, done, info = env.step(action)
    next_state = np.reshape(next_state, [1, state_size])
    state = next_state
    score += reward
    env.render()
print(f"Score: {score}")
env.close()
