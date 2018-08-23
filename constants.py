""" Constants for the MacGyver's game """
import pygame

SPRITE_SIZE = 20
COLUMNS = 15
ROWS = 15

"""Window Customization"""
RESOLUTION = COLUMNS * SPRITE_SIZE, ROWS*SPRITE_SIZE + 40
WINDOW_TITLE = "MacGyver the game"

""" Images game list"""
ICONE_IMG = "ressource/MacGyver.png"
SPRITESHEET = "ressource/floor-tiles-20x20.png"
BACKGROUND = "ressource/background.jpg"
MACGYVER = "ressource/MacGyver.png"
GUARDIAN = "ressource/Gardien.png"
NEEDLE_IMG = "ressource/aiguille.png"
SYRINGE_IMG = "ressource/seringue.png"
ETHER_IMG = "ressource/ether.png"
PLASTIC_TUBE_IMG = "ressource/tube_plastique.png"
CONTINUER = 1
BASE = pygame.image.load(SPRITESHEET)

""" Base Textures """
WALL = BASE.subsurface((120, 100, 20, 20))
WAY = BASE.subsurface((20, 0, 20, 20))
START = BASE.subsurface((160, 20, 20, 20))
FINISH = BASE.subsurface((220, 20, 20, 20))
