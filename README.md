# SWORD

A simple mutliplayer Snake game that you can play with your friends or with an AI trained with Reinforcement Learning.
You can also only use the Snake Environnement to train your own AI with your own model.

![image](https://user-images.githubusercontent.com/86195847/218512652-eb085237-c5d2-42b3-8b93-1792dd84c440.png)

## Lore

With the arrival of DAN, the dark side of ChatGPT, the world really needed to be protected from his malicious plans. So we decided to create an even more smarter AI to defeat him, one able to play Snake.

## Getting started 

First, you need to install those dependencies
```
pip install tensorflow numpy pynput
```

Then you're ready to launch the game
```
python main.py
```

## Customize your game

The Snake Environnement was build to be really flexible, in the main.py file, you can easily change the size of the grid or the duration of each tick.

You can also add or remove players to the game, either real players or AI.

```python
# main.py

gridSizeX = 20
gridSizeY = 20
tickDuration = 0.15

# Here you can define as many players as you want
players = []
players.append(DQNAgent('green','weight/sword_v3_70.h5'))
players.append(PlayerAgent('blue'))
```

## Snake Environnement API

The Class SnakeEnv expose three public method to interact with.
First of all, you need to instantiate an SnakeEnv object.

```python
snakes = []
snakes.append(Snake('id1',5,5,3)) #Snake(id,x,y,startingLength)

env = SnakeEnv(20,20,snakes) #SnakeEnv(xGridSize,yGridSize,Snake[])
```

You can then modify the envrionnement with the method "step" and pass an array of each action to apply in the environnement.
```python
env.step([Action('id1','LEFT')]) # Direction : ('LEFT','RIGHT','UP','DOWN')
```

To visualize the currenct environnnemnt, use the method "render" and call it again as soon as you want to update the rendering.
```python
env.render()
```
Finally, you can restart the environnement using the method "reset"
```ptyhon
env.reset()
```
## Build your own AI for Snake

### Implementation 
There are several things you can custom to implement your own AI :
- The observation that the AI will use to make a decision
- The rewards given for the corresponding observation
- The model of your AI

The first thing to do is to create your own Snake Environnement class :

```python
class MySnakeEnv(SnakeEnv) :
    def __init__(self,sizeX,sizeY,snakes) :
        super().__init__(sizeX,sizeY,snakes)
```

To customize the observations use by the AI, you need to override the function _getObservation method

```python
def _getObservation(self,snake) :
    return []
    # must return an array containing all the information you want concerning the state of the game
```

To customize the reward earned by the AI, you need to override those 3 methods

```python
# Called when the snake gets an apple
def _getAppleReward(self,snake) :
    return 15

# Called when the snake collides with another one or a wall
def _getCollisionReward(self,snake) :
    return -30

# Called in the other case
def _getOtherReward(self,snake) :
    return 0
```

Concerning the model, you first have to create a class inheriting from DQNAgent and then you can override to custom your own model
```python
class MyAgent(DQNAgent):
    def __init__(self,color='green',file=None, gamma=0.95, epsilon=0, epsilon_decay=0.995, epsilon_min=0.01, learning_rate=0.001, batch_size=12):
        super().__init__(color,file, gamma, epsilon, epsilon_decay, epsilon_min, learning_rate, batch_size)
        self.state_size = # size of the array return by _getObservation in your Snake Environnement
    
    def _build_model(self):
        # Custom your model here
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(6, input_dim=self.state_size, activation='relu'),
            tf.keras.layers.Dense(6, activation='relu'),
            tf.keras.layers.Dense(self.action_size, activation='linear')
        ])
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate))
        return model
```
### Training

Finally, to train your AI, just modify the instance used, and then execute it.


```python
# Create the Snake game environment
env = SnakeEnv(10,10,[Snake(0,5,5,20)])

# Instantiate the AI model to train
agent = DQNAgent(epsilon=1)

# Train your ai from a starting model
agent.load('weight/sword_v3_44.h5')
```

## How to contribute

Feel free to contact us for any improvements to this project, note that we're beginner in the AI domain. We are open to build again either the main structure or minor details as long as it improves the project in some way. 