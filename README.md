# SWORD

A simple mutliplayer Snake game that you can play with your friends or with an AI trained with Reinforcement Learning.
You can also only use the Snake Environnement to train your own AI with your own model.

![image](https://user-images.githubusercontent.com/86195847/218512652-eb085237-c5d2-42b3-8b93-1792dd84c440.png)


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

## Train your own AI model

