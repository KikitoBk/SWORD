from time import sleep
import numpy as np
from Snake import Snake
from SnakeEnv import SnakeEnv
from DQNAgent import DQNAgent

def localToGlobal(action,snake) :
    leftBinding = {'UP': 'LEFT', 'DOWN': 'RIGHT', 'LEFT': 'DOWN', 'RIGHT': 'UP'}
    rightBinding = {'UP': 'RIGHT', 'DOWN': 'LEFT', 'LEFT': 'UP', 'RIGHT': 'DOWN'}

    #choose to go left
    if action.direction == 'LEFT' :
        return leftBinding[snake.direction]
    #choose to go forward
    elif action.direction == 'STRAIGHT' :
        return snake.direction
    #choose to go right
    elif action.direction == 'RIGHT' :
        return  rightBinding[snake.direction]


# Create the Snake game environment
env = SnakeEnv(10,10,[Snake('AI',5,5,20)])

# Create the DQN agent
agent = DQNAgent('AI',epsilon=0.01)
agent.load('weight/sword_v3_44.h5')
# Train the agent
num_episodes = 50
for episode in range(num_episodes):
    sleep(1)
    [state,*_] = env.reset()
    
    env.render()
    
    done = False
    score = 0
    while not done:
        actionInt, action,isLocal = agent.act(state)
        if(isLocal) :
            action.direction = localToGlobal(action,env.getSnake('AI'))
        [next_state,*_], [reward,*_], done, _ = env.step([action])
        print(next_state,reward)
        env.render()
        agent.remember(state, actionInt, reward, next_state, done)
        state = next_state
        score += reward
        if done:
            print(f"episode: {episode+1}/{num_episodes}, score: {score}, epsilon: {agent.epsilon:.2f}")
        agent.replay()
    
    agent.save('weight/sword_v3_{}.h5'.format(episode+45))

# Save the trained model


