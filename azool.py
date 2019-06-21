import numpy as np
import sys
import math

np.random.seed(200)

WALL_SIZE = 5

# create the tile wall
def create_wall():
    wall = np.zeroes((WALL_SIZE, WALL_SIZE))
    return wall

# creates array to store tiles before they're added to the wall
def create_pattern_lines():
	pattern_lines = np.tril(np.ones((5, 5)), k = -1)
	return pattern_lines

# flip array to display in same orientation as board game
def display_pattern_lines(pattern_lines):
	return np.flip(pattern_lines, 0)



class Player(object):
    pass

class TileBag(object):
    pass

class Tile(object):
    def __init__(self):
        colors = ["red", "yellow", "teal", "black", "white"]
        values = [1, 2, 3, 4, 5]

class Factory(object):
    pass






game_over = FALSE

# game loop
while not game_over:
	pass