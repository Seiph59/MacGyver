""" Main file, launch from  this file the game,
    it is important to have a Labyrinth.txt file,
    if you don't have one, launch "labyrinth.py" before
    MacGyver.py
"""

import pygame
import classes
import constants as const

game = classes.MacGyverGame()
game.load_map('Labyrinth.txt')
game.start_game()
