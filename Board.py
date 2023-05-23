import pygame
import random


class Board:
    def __init__(self, i, j, TILE):
        self.TILE = TILE
        self.haveDet = 1  # 1 - нету, 0 - есть
        self.color = pygame.Color("Gray")
        self.cell = pygame.Rect(i * TILE, j * TILE, TILE, TILE)
        color_dict = pygame.colordict.THECOLORS
        self.colors = list(color_dict.values())

    def fillCell(self):
        self.haveDet = 0
        self.color = random.choice(self.colors)



    def notFillCell(self):
        self.haveDet = 1
        self.color = pygame.Color("Gray")
