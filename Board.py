import pygame


class Board:
    def __init__(self, i, j, TILE):
        self.TILE = TILE
        self.haveDet = 1  # 1 - нету, 0 - есть
        self.color = pygame.Color(128, 128, 128, 255)
        self.cell = pygame.Rect(i * TILE, j * TILE, TILE, TILE)

    def fillCell(self):
        self.haveDet = 0
        self.color = self.activeColor()

    def activeColor(self):
        return pygame.Color("Green")

    def notFillCell(self):
        self.haveDet = 1
        self.color = (128, 128, 128, 255)
