import os
import pygame
from classes import MacGyver, getIndex, Item, getPosition
from pygame.locals import * 
from constants import ICONE,RESOLUTION,WINDOW_TITLE,BACKGROUND,SPRITESHEET,MACGYVER,GUARDIAN,SYRINGE,NEEDLE,PLASTIC_TUBE,ETHER

pygame.init()

window = pygame.display.set_mode((RESOLUTION))

icone = pygame.image.load(ICONE)
pygame.display.set_icon(icone)

pygame.display.set_caption(WINDOW_TITLE)

base = pygame.image.load(SPRITESHEET)
macgyver = pygame.image.load(MACGYVER).convert_alpha()
macgyver = pygame.transform.scale(macgyver,(19,19))
guardian = pygame.image.load(GUARDIAN).convert_alpha()
guardian = pygame.transform.scale(guardian,(19,19))
ether = pygame.image.load(ETHER).convert_alpha()
ether = pygame.transform.scale(ether,(19,19))
needle = pygame.image.load(NEEDLE).convert_alpha()
needle = pygame.transform.scale(needle,(19,19))
syringe = pygame.image.load(SYRINGE).convert_alpha()
syringe = pygame.transform.scale(syringe,(19,19))
plasticTube = pygame.image.load(PLASTIC_TUBE).convert_alpha()
plasticTube = pygame.transform.scale(plasticTube,(19,19))

comicFont = pygame.font.SysFont('Comic Sans MS', 45)
textWin = comicFont.render("YOU WIN !", True,(255,255,255))
textLost = comicFont.render("YOU LOST !", True,(255,255,255))

needleI = Item (1,2)
etherI = Item (12,8)
syringeI = Item (3,5)
plasticTubeI = Item (2,11)

wall = base.subsurface((120,100,20,20))
way = base.subsurface((20,0,20,20))
start = base.subsurface((160,20,20,20))
finish = base.subsurface((220,20,20,20))

openFile = open('Labyrinth.txt', 'r')
lignes = openFile.readlines()
for i in range(len(lignes)): 
    ligne = lignes[i]
    #print(ligne)
    if ligne == "wall \n": 
        window.blit(wall,(getPosition(i)))
    elif ligne == "way \n":
        window.blit(way,(getPosition(i)))
    elif ligne == "start \n":
        window.blit(start,(getPosition(i)))
        #window.blit(mac.image,(mac.x,mac.y))
    elif ligne == "finish \n":
        window.blit(finish,(getPosition(i)))
        window.blit(guardian,(getPosition(i)))
    
    window.blit(needle,(needleI.case_x,needleI.case_y))
    window.blit(syringe,(syringeI.case_x,syringeI.case_y))
    window.blit(ether,(etherI.case_x,etherI.case_y))
    window.blit(plasticTube,(plasticTubeI.case_x,plasticTubeI.case_y))
    pygame.display.flip()


    mac = MacGyver()
    window.blit(macgyver,(mac.case_x,mac.case_y))
    pygame.display.flip()    
    
openFile.close() 




"""Loop of the game """

continuer = 1 

while continuer: 

    pygame.time.Clock().tick(30)
    previousPosition = (mac.case_x, mac.case_y)
    for event in pygame.event.get():

        if event.type is pygame.QUIT:
            continuer = False 
        
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mac.move('right')
                window.blit(way,(previousPosition))
            elif event.key == K_LEFT:
                mac.move('left')
                window.blit(way,(previousPosition))
            elif event.key == K_UP:
                mac.move('top')
                window.blit(way,(previousPosition))
            elif event.key == K_DOWN:
                mac.move('bottom')
                if getIndex(mac.x,mac.y - 1) != 3:
                    window.blit(way,(previousPosition))
                else:
                    window.blit(start,(previousPosition))
        
    window.blit(macgyver,(mac.case_x,mac.case_y))
    pygame.display.flip()
    
    if mac.case_x == needleI.case_x and mac.case_y == needleI.case_y and needleI.counter < 1:
        needleI.counter += 1
    
    if mac.case_x == syringeI.case_x and mac.case_y == syringeI.case_y and syringeI.counter < 1:
        syringeI.counter += 1

    if mac.case_x == etherI.case_x and mac.case_y == etherI.case_y and etherI.counter < 1:
        etherI.counter += 1

    if mac.case_x == plasticTubeI.case_x and mac.case_y == plasticTubeI.case_y and plasticTubeI.counter < 1:
        plasticTubeI.counter += 1

    items = needleI.counter + syringeI.counter + plasticTubeI.counter + etherI.counter

    if getIndex(mac.x, mac.y) == 202 and items == 4:
        window.blit(textWin,(30,110))
        window.blit(finish,(getPosition(217)))
        pygame.display.flip()
        pygame.time.delay(2000)
        continuer = False
    
    elif getIndex(mac.x, mac.y) == 202 and items != 4:
        window.blit(textLost,(30,110))
        pygame.time.delay(1000)
        window.blit(way,(getPosition(202)))
        pygame.display.flip()
        pygame.time.delay(2000)
        continuer = False




