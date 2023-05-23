import pygame
import random
import copy
import Board


class Game:
    def __init__(self, I_max, J_max, TILE):
        self.I_max = I_max
        self.J_max = J_max
        self.TILE = TILE
        self.grid = []
        self.choice = []
        self.I_J_choice = 6
        self.choiceCount = 3
        self.need_choice = True
        self.draw_det = False
        self.selected_detail = None
        self.detail = None
        self.detChoice = None
        self.allDetails = None

    def fillGrid(self, grid):
        for i in range(self.I_max):
            grid.append([])
            for j in range(self.J_max):
                grid[i].append(Board.Board(i, j, self.TILE))

    def fillChoice(self, choice):
        for i in range(self.I_J_choice):
            choice.append([])
            for j in range(self.I_J_choice):
                choice[i].append(Board.Board(i, j, self.TILE))

    def check_win(self, grid):
        # Проверка строк на полное заполнение
        for j in range(self.J_max):
            is_full = all(grid[i][j].haveDet == 0 for i in range(self.I_max))
            if is_full:
                for k in range(self.I_max):
                    grid[k][j].Board.notFillCell()

        # Проверка столбцов на полное заполнение
        for i in range(self.I_max):
            is_full = all(grid[i][j].haveDet == 0 for j in range(self.J_max))
            if is_full:
                for k in range(self.J_max):
                    grid[i][k].Board.notFillCell()

    def selectedDetail(self, det):
        print(det)
        self.selected_detail = det
        self.draw_det = True



    @staticmethod
    def drawField(screen, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                pygame.draw.rect(screen, board[i][j].color, board[i][j].cell)


    def moveDet(self, screen, x, y):
        delx = self.selected_detail[2].x - x
        dely = self.selected_detail[2].y - y

        for i in range(len(self.selected_detail)):
            self.selected_detail[i].x -= delx
            self.selected_detail[i].y -= dely
            pygame.draw.rect(screen, pygame.Color("Yellow"), self.selected_detail[i])
            pygame.display.update()

    def placement(self, screen, board):
        can_place = True
        for i in range(len(self.selected_detail)):
            pos_x = self.selected_detail[i].x // self.TILE
            pos_y = self.selected_detail[i].y // self.TILE
            print(pos_x, " ", pos_y)
            if board[pos_x][pos_y].haveDet:  # Проверяем, что квадратик уже не закрашен
                can_place = False
                break
        if can_place:
            for i in range(len(selected_detail)):
                pos_x = selected_detail[i].x // self.TILE
                pos_y = selected_detail[i].y // self.TILE

                board[pos_x][pos_y].fillCell()
            for i in range(len(board)):
                for j in range(len(board[i])):
                    pygame.draw.rect(screen, board[i][j].color, board[i][j].cell)
            self.draw_det = False  # вывести на экран!!!!!!

    def drawChoice(self, screenChoice, buttonChoice):
        if self.need_choice:
            tmpDet = self.detChoice
            for k in range(len(screenChoice)):
                for i in range(len(tmpDet)):
                    self.detail.x = self.detChoice[i].x
                    self.detail.y = self.detChoice[i].y
                    pygame.draw.rect(screenChoice[k], pygame.Color("Green"), self.detail)
                    buttonChoice[k].haveDetail = True
                    buttonChoice[k].detail = tmpDet
                self.detChoice = copy.deepcopy(random.choice(self.allDetails))
            self.need_choice = False

    @staticmethod
    def newChoice(screenChoice, boardChoice, buttonChoice):
        for i in range(len(boardChoice)):
            for j in range(len(boardChoice[i])):
                boardChoice[i][j].Board.notFillCell()

        for k in range(len(boardChoice)):
            screenChoice[k].fill(pygame.Color("Black"))
            buttonChoice[k].detail = True
            for i in range(len(boardChoice)):
                for j in range(len(boardChoice[i])):
                    pygame.draw.rect(screenChoice[k], boardChoice[i][j].Board.color, boardChoice[i][j].Board.cell)


    def details(self):
        details = [
            [[-2, 0], [-1, 0], [0, 0], [1, 0]],
            [[-1, 1], [-1, 0], [0, 0], [1, 0]],
            [[1, 1], [-1, 0], [0, 0], [1, 0]],
            [[-1, 1], [0, 1], [0, 0], [-1, 0]],
            [[1, 0], [1, 1], [0, 0], [-1, 0]],
            [[0, 1], [-1, 0], [0, 0], [1, 0]],
            [[-1, 1], [0, 1], [0, 0], [1, 0]],
        ]
        det = [[], [], [], [], [], [], []]
        for i in range(0, len(details)):
            for j in range(0, len(details[i])):
                det[i].append(
                    pygame.Rect(details[i][j][0] * self.TILE + self.TILE * (self.I_J_choice // 2), details[i][j][1] * self.TILE + self.TILE, self.TILE, self.TILE))
        self.allDetails = det
        self.detail = pygame.Rect(0, 0, self.TILE, self.TILE)
        self.detChoice = copy.deepcopy(random.choice(det))
