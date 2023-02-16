import numpy as np
from Snake import Snake
from SnakeEnv import SnakeEnv
from DQNAgent import DQNAgent

# Create the Snake game environment
env = SnakeEnv(30,30,[Snake('AI',15,15,3)])

# Set the state size and action size
state_size = env.observation_space.shape[0]

# Create the DQN agent
agent = DQNAgent(state_size, 3)

# Train the agent
num_episodes = 1000
for episode in range(num_episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    done = False
    score = 0
    while not done:
        action = agent.act(state)
        next_state, reward, done, info = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        score += reward
        if done:
            print(f"episode: {episode+1}/{num_episodes}, score: {score}, epsilon: {agent.epsilon:.2f}")
        agent.replay()

# Save the trained model
agent.save('snake_dqn.h5')
