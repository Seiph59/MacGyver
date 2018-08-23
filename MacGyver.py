""" Main file, launch from  this file the game,
    it is important to have a Labyrinth.txt file,
    if you don't have one, launch "labyrinth.py" before
    MacGyver.py
"""

import pygame
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_DOWN, K_UP
import classes
import constants as const


pygame.init()
WINDOW = pygame.display.set_mode((const.RESOLUTION))
level = classes.Labyrinth('Labyrinth.txt')

ICONE = pygame.image.load(const.ICONE_IMG)
pygame.display.set_icon(ICONE)
pygame.display.set_caption(const.WINDOW_TITLE)


MAC_GYVER = pygame.image.load(const.MACGYVER).convert_alpha()
MAC_GYVER = pygame.transform.scale(MAC_GYVER, (19, 19))
GUARD = pygame.image.load(const.GUARDIAN).convert_alpha()
GUARD = pygame.transform.scale(GUARD, (19, 19))
ETHER = pygame.image.load(const.ETHER_IMG).convert_alpha()
ETHER = pygame.transform.scale(ETHER, (19, 19))
NEEDLE = pygame.image.load(const.NEEDLE_IMG).convert_alpha()
NEEDLE = pygame.transform.scale(NEEDLE, (19, 19))
# syringe = pygame.image.load(SYRINGE).convert_alpha()
# syringe = pygame.transform.scale(syringe,(19,19))
PLASTIC_TUBE = pygame.image.load(const.PLASTIC_TUBE_IMG).convert_alpha()
PLASTIC_TUBE = pygame.transform.scale(PLASTIC_TUBE, (19, 19))

""" Writing """
COMIC_FONT = pygame.font.SysFont('Comic Sans MS', 45)
COMIC_FONT_INV = pygame.font.SysFont('Comic Sans MS', 15)
TEXT_WIN = COMIC_FONT.render("YOU WIN !", True, (255, 255, 255))
TEXT_LOST = COMIC_FONT.render("YOU LOST !", True, (255, 255, 255))
INVENTORY = COMIC_FONT_INV.render(" INVENTORY: ", True, (255, 255, 255))

"""Random position for each Item """

random_index = classes.random_position()
position_x = random_index[0]
position_y = random_index[1]
needle = classes.Item(position_x, position_y)

random_index = classes.random_position()
position_x = random_index[0]
position_y = random_index[1]
ether = classes.Item(position_x, position_y)

random_index = classes.random_position()
position_x = random_index[0]
position_y = random_index[1]
plastic_tube = classes.Item(position_x, position_y)

level.display(WINDOW)

# Display the 3 Items

WINDOW.blit(NEEDLE, (needle.case_x, needle.case_y))
WINDOW.blit(ETHER, (ether.case_x, ether.case_y))
WINDOW.blit(PLASTIC_TUBE, (plastic_tube.case_x, plastic_tube.case_y))
pygame.display.flip()


mac_gyver = classes.MacGyver()
WINDOW.blit(MAC_GYVER, (mac_gyver.case_x, mac_gyver.case_y))
pygame.display.flip()

while const.CONTINUER:  # Loop of the game

    pygame.time.Clock().tick(30)
    # previousPosition = (mac.case_x, mac.case_y)
    for event in pygame.event.get():

        if event.type is pygame.QUIT:
            const.CONTINUER = 0

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

    level.display(WINDOW)
    WINDOW.blit(INVENTORY, (10, 305))

    if (mac_gyver.case_x == needle.case_x and
            mac_gyver.case_y == needle.case_y and needle.counter < 1):
        needle.counter += 1

    elif needle.counter != 1:
        WINDOW.blit(NEEDLE, (needle.case_x, needle.case_y))
    else:
        WINDOW.blit(NEEDLE, (170, 305))

    if (mac_gyver.case_x == ether.case_x
            and mac_gyver.case_y == ether.case_y
            and ether.counter < 1):

        ether.counter += 1

    elif ether.counter != 1:
        WINDOW.blit(ETHER, (ether.case_x, ether.case_y))
    else:
        WINDOW.blit(ETHER, (200, 305))

    if (mac_gyver.case_x == plastic_tube.case_x
            and mac_gyver.case_y == plastic_tube.case_y
            and plastic_tube.counter < 1):

        plastic_tube.counter += 1

    elif plastic_tube.counter != 1:
        WINDOW.blit(PLASTIC_TUBE, (plastic_tube.case_x, plastic_tube.case_y))
    else:
        WINDOW.blit(PLASTIC_TUBE, (230, 310))
    WINDOW.blit(MAC_GYVER, (mac_gyver.case_x, mac_gyver.case_y))
    items = needle.counter + plastic_tube.counter + ether.counter
    pygame.display.flip()

    if classes.get_index(mac_gyver.position_x, mac_gyver.position_y) == 202 and items == 3:
        WINDOW.blit(TEXT_WIN, (30, 110))
        WINDOW.blit(const.FINISH, (classes.get_position(217)))
        pygame.display.flip()
        pygame.time.delay(2000)
        const.CONTINUER = 0

    elif (classes.get_index(mac_gyver.position_x, mac_gyver.position_y) == 202
          and items != 3):
        WINDOW.blit(TEXT_LOST, (30, 110))
        WINDOW.blit(const.WAY, (classes.get_position(202)))
        pygame.display.flip()
        pygame.time.delay(2000)
        const.CONTINUER = 0
