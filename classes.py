""" Classes files, used on MacGyver.py
    Launch MacGyver.py to launch the Game"""

import random
import pygame
import constants as const
from labyrinth import WAYS


def get_index(coordinate_x, coordinate_y):
    """ Transform Coordinate to index """
    ligne = coordinate_x + coordinate_y*15
    return ligne


def get_position(index):
    """ Transform index to a position on map
    with Sprites
    """
    position_y = int(index / 15)
    position_x = index % 15
    return position_x * const.SPRITE_SIZE, position_y * const.SPRITE_SIZE


def get_item(index):
    """ Transform index to coordinates for item positioning"""
    coordinate_y = int(index / 15)
    coordinate_x = index % 15
    return coordinate_x, coordinate_y


def random_position():
    """ Generate a random position for each item"""
    random_choice = random.choice(WAYS)
    r_position = get_item(random_choice)
    return r_position


class Labyrinth:  # pylint: disable=too-few-public-methods
    """Structure's class to display map and
    convert index, coordinates
    """
    def __init__(self, file):
        self.file = file

    def display(self, window):
        """ Display the map and all the textures on window"""
        base = pygame.image.load(const.SPRITESHEET)
        wall = base.subsurface((120, 100, 20, 20))
        way = base.subsurface((20, 0, 20, 20))
        start = base.subsurface((160, 20, 20, 20))
        finish = base.subsurface((220, 20, 20, 20))
        guardian = pygame.image.load(const.GUARDIAN).convert_alpha()
        guardian = pygame.transform.scale(guardian, (19, 19))

        open_file = open(self.file)
        lignes = open_file.readlines()
        for i, value in enumerate(lignes):
            # ligne = i
            # print(ligne)
            if value == "wall \n":
                window.blit(wall, (get_position(i)))
            elif value == "way \n":
                window.blit(way, (get_position(i)))
            elif value == "start \n":
                window.blit(start, (get_position(i)))
                # window.blit(mac.image,(mac.x,mac.y))
            elif value == "finish \n":
                window.blit(finish, (get_position(i)))
                window.blit(guardian, (get_position(i)))

        open_file.close()


class MacGyver:  # pylint: disable=too-few-public-methods
    """
    Class who manage the main character,
    and his movements on the map
    """

    def __init__(self):
        self.case_x = 60
        self.case_y = 0
        self.position_x = 3
        self.position_y = 0

    def move(self, direction):
        """ Method  for the character's movements"""
        if direction == 'right':
            if self.position_x < (const.COLUMNS - 1):
                if get_index(self.position_x, self.position_y) + 1 in WAYS:
                    self.position_x += 1
                    self.case_x = self.position_x * const.SPRITE_SIZE

        if direction == 'bottom':
            if self.position_y < (const.ROWS - 1):
                if get_index(self.position_x, self.position_y) + 15 in WAYS:
                    self.position_y += 1
                    self.case_y = self.position_y * const.SPRITE_SIZE

        if direction == 'left':
            if self.position_x > 0:
                if get_index(self.position_x, self.position_y) - 1 in WAYS:
                    self.position_x -= 1
                    self.case_x = self.position_x * const.SPRITE_SIZE

        if direction == 'top':
            if self.position_y > 0:
                if get_index(self.position_x, self.position_y) - 15 in WAYS:
                    self.position_y -= 1
                    self.case_y = self.position_y * const.SPRITE_SIZE


class Item:  # pylint: disable=too-few-public-methods
    """ Class to manage each item
    on the map
    """
    def __init__(self, coordinate_x, coordinate_y):
        # self.coordinate_x = 0
        # self.coordinate_y = 0
        self.counter = 0
        self.case_x = coordinate_x * const.SPRITE_SIZE
        self.case_y = coordinate_y * const.SPRITE_SIZE
