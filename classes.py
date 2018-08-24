""" Classes files, used on MacGyver.py
    Launch MacGyver.py to launch the Game"""

import random
import pygame
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_DOWN, K_UP
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


class MacGyverGame:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((const.RESOLUTION))
        icone = pygame.image.load(const.ICONE_IMG)
        pygame.display.set_icon(icone)
        pygame.display.set_caption(const.WINDOW_TITLE)
        mac_gyver_image = pygame.image.load(const.MACGYVER).convert_alpha()
        self.mac_gyver = pygame.transform.scale(mac_gyver_image, (19, 19))
        guard_image = pygame.image.load(const.GUARDIAN).convert_alpha()
        self.guard = pygame.transform.scale(guard_image, (19, 19))
        ether_image = pygame.image.load(const.ETHER_IMG).convert_alpha()
        self.ether = pygame.transform.scale(ether_image, (19, 19))
        needle_image = pygame.image.load(const.NEEDLE_IMG).convert_alpha()
        self.needle = pygame.transform.scale(needle_image, (19, 19))
        # syringe = pygame.image.load(SYRINGE).convert_alpha()
        # syringe = pygame.transform.scale(syringe,(19,19))
        plastic_tube_image = pygame.image.load(const.PLASTIC_TUBE_IMG).convert_alpha()
        self.plastic_tube = pygame.transform.scale(plastic_tube_image, (19, 19))

        """ Writing """
        self.comic_font = pygame.font.SysFont('Comic Sans MS', 45)
        self.comic_font_inv = pygame.font.SysFont('Comic Sans MS', 15)
        self.text_win = self.comic_font.render("YOU WIN !", True, (255, 255, 255))
        self.text_lost = self.comic_font.render("YOU LOST !", True, (255, 255, 255))
        self.inventory = self.comic_font_inv.render(" INVENTORY: ", True, (255, 255, 255))

    def load_map(self, src):

        """Random position for each Item """

        random_index = random_position()
        position_x = random_index[0]
        position_y = random_index[1]
        self.needle_item = Item(position_x, position_y)

        random_index = random_position()
        position_x = random_index[0]
        position_y = random_index[1]
        self.ether_item = Item(position_x, position_y)

        random_index = random_position()
        position_x = random_index[0]
        position_y = random_index[1]
        self.plastic_tube_item = Item(position_x, position_y)

        self.level = Labyrinth(src)
        self.level.display(self.window)

        # Display the 3 Items

        self.window.blit(self.needle, (self.needle_item.case_x, self.needle_item.case_y))
        self.window.blit(self.ether, (self.ether_item.case_x, self.ether_item.case_y))
        self.window.blit(self.plastic_tube, (self.plastic_tube_item.case_x, self.plastic_tube_item.case_y))


        mac_gyver = MacGyver()
        self.window.blit(self.mac_gyver, (mac_gyver.case_x, mac_gyver.case_y))
        pygame.display.flip()

    def start_game(self):
        progress = 1
        while progress:  # Loop of the game
            pygame.time.Clock().tick(30)
            # previousPosition = (mac.case_x, mac.case_y)
            for event in pygame.event.get():

                if event.type is pygame.QUIT:
                    progress = 0

                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        mac_gyver.move('right')
                        # window.blit(way,(previousPosition))
                    elif event.key == K_LEFT:
                        mac_gyver.move('left')
                        # window.blit(way,(previousPosition))
                    elif event.key == K_UP:
                        mac_gyver.move('top')
                        # window.blit(way,(previousPosition))
                    elif event.key == K_DOWN:
                        mac_gyver.move('bottom')

            self.level.display(self.window)
            self.window.blit(self.inventory, (10, 305))

            if (mac_gyver.case_x == self.needle_item.case_x and
                    mac_gyver.case_y == self.needle_item.case_y and self.needle_item.counter < 1):
                self.needle_item.counter += 1

            elif self.needle_item.counter != 1:
                self.window.blit(self.needle, (self.needle_item.case_x, self.needle_item.case_y))
            else:
                self.window.blit(self.needle, (170, 305))

            if (mac_gyver.case_x == self.ether_item.case_x
                    and mac_gyver.case_y == self.ether_item.case_y
                    and self.ether_item.counter < 1):

                self.ether_item.counter += 1

            elif self.ether_item.counter != 1:
                self.window.blit(ETHER, (self.ether_item.case_x, self.ether_item.case_y))
            else:
                self.window.blit(ETHER, (200, 305))

            if (mac_gyver.case_x == self.plastic_tube_item.case_x
                    and mac_gyver.case_y == self.plastic_tube_item.case_y
                    and self.plastic_tube_item.counter < 1):

                self.plastic_tube_item.counter += 1

            elif self.plastic_tube_item.counter != 1:
                self.window.blit(PLASTIC_TUBE, (self.plastic_tube_item.case_x, self.plastic_tube_item.case_y))
            else:
                self.window.blit(PLASTIC_TUBE, (230, 310))
            self.window.blit(MAC_GYVER, (mac_gyver.case_x, mac_gyver.case_y))
            items = self.needle_item.counter + self.plastic_tube_item.counter + self.ether_item.counter
            pygame.display.flip()

            if get_index(mac_gyver.position_x, mac_gyver.position_y) == 202 and items == 3:
                self.window.blit(self.text_win, (30, 110))
                self.window.blit(const.FINISH, (get_position(217)))
                pygame.display.flip()
                pygame.time.delay(2000)
                progress = 0

            elif (get_index(mac_gyver.position_x, mac_gyver.position_y) == 202
                and items != 3):
                self.window.blit(self.text_lost, (30, 110))
                self.window.blit(const.WAY, (get_position(202)))
                pygame.display.flip()
                pygame.time.delay(2000)
                progress = 0