import numpy as np
from SnakeEnv import SnakeEnv
from DQNAgent import DQNAgent

# Create the Snake game environment
env = SnakeEnv()

# Set the state size and action size
state_size = env.observation_space.shape[0]
action_size = env.action_space.n

# Create the DQN agent
agent = DQNAgent(state_size, action_size)

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
