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



## How to contribute

Feel free to contact us for any improvements to this project, note that we're beginner in the AI domain. We are open to build again either the main structure or minor details as long as it improves the project in some way. 