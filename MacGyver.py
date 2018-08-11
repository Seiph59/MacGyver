import os
import pygame
from pygame.locals import * 
from constants import ICONE,RESOLUTION,WINDOW_TITLE,BACKGROUND,SPRITESHEET,MACGYVER,GUARDIAN

pygame.init()

def getPosition(getIndex):
    y = int(getIndex / 15)
    x = getIndex % 15
    return x*20, y*20

    

fenetre = pygame.display.set_mode((300,300))

icone = pygame.image.load(ICONE)
pygame.display.set_icon(icone)

pygame.display.set_caption(WINDOW_TITLE)

fond = pygame.image.load(BACKGROUND).convert()
base = pygame.image.load(SPRITESHEET)
macgyver = pygame.image.load(MACGYVER).convert_alpha()
macgyver = pygame.transform.scale(macgyver,(19,19))
guardian = pygame.image.load(GUARDIAN).convert_alpha()
guardian = pygame.transform.scale(guardian,(19,19))

wall = base.subsurface((120,100,20,20))
way = base.subsurface((20,0,20,20))
start = base.subsurface((160,20,20,20))
finish = base.subsurface((220,20,20,20))

fenetre.blit(fond,(0,0))

openFile = open('Labyrinth.txt', 'r')
lignes = openFile.readlines()
for i in range(len(lignes)): 
    ligne = lignes[i]
    #print(ligne)
    if ligne == "wall \n": 
        fenetre.blit(wall,(getPosition(i)))
    elif ligne == "way \n":
        fenetre.blit(way,(getPosition(i)))
    elif ligne == "start \n":
        fenetre.blit(start,(getPosition(i)))
        #fenetre.blit(macgyver,(getPosition(i)))
    elif ligne == "finish \n":
        fenetre.blit(finish,(getPosition(i)))
        #fenetre.blit(guardian,(getPosition(i)))
    pygame.display.flip()    
    
    

openFile.close() 


continuer = 1 

while continuer: 
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            continuer = False 
    






