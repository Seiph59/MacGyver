import pygame
from constants import COLUMNS, ROWS, SPRITE_SIZE
from labyrinth import ways

def getIndex(x, y):
    ligne = x + y*15 
    return ligne

def getPosition(getIndex):
    y = int(getIndex / 15)
    x = getIndex % 15
    return x*20, y*20

class MacGyver: 
    def __init__(self):
        self.case_x = 60
        self.case_y = 0
        self.x = 3
        self.y = 0

    def move(self, direction):

        if direction == 'right':
            if self.x < (COLUMNS - 1):
                if getIndex(self.x, self.y) + 1 in ways:
                    self.x += 1
                    self.case_x = self.x * SPRITE_SIZE
        
        if direction == 'bottom':
            if self.y < (ROWS - 1):
                if getIndex(self.x,self.y) + 15 in ways:
                    self.y += 1
                    self.case_y = self.y * SPRITE_SIZE
        
        if direction == 'left':
            if self.x > 0:
                if getIndex(self.x, self.y) - 1 in ways:
                    self.x -= 1
                    self.case_x = self.x * SPRITE_SIZE
        
        if direction == 'top':
            if self.y > 0:
                if getIndex(self.x, self.y) - 15 in ways:
                    self.y -= 1
                    self.case_y = self.y * SPRITE_SIZE

class Item:
    def __init__(self,x,y):
        self.x = 0
        self.y = 0
        self.counter = 0
        self.case_x = x * SPRITE_SIZE
        self.case_y = y * SPRITE_SIZE