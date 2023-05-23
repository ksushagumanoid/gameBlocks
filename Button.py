import math
import pygame


class Button:

    def __init__(self, width, height, index_button, game, args=None):
        self.width = width
        self.height = height
        self.index = index_button
        self.haveDetail = True
        self.detail = None
        #self.action = action
        self.game = game
        self.args = args

    def draw_without_text(self, screen, x, y, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(screen, (23, 204, 58, 10), (x, y, self.width, self.height))
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(screen, (13, 162, 58, 100), (x, y, self.width, self.height))

    def draw(self, screen, x, y, message, action, args):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(screen, (23, 204, 58), (x, y, self.width, self.height))
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if click[0] == 1:
                if args is not None:
                    action(args)
                else:
                    action()
        else:
            pygame.draw.rect(screen, (13, 162, 58), (x, y, self.width, self.height))

        font_type = pygame.font.Font('arialmt.ttf', 30)
        text = font_type.render(message, True, (0, 0, 0))
        screen.blit(text, (x + 10, y + 10))

    def draw_circle(self, screen, x, y):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        r = self.height // 5
        if not self.haveDetail:
            pygame.draw.circle(screen, (128, 128, 128, 10), (x, y), r)
        else:
            pygame.draw.circle(screen, (23, 204, 58, 10), (x, y), r)
            if math.pow(x - mouse[0], 2) + math.pow(y - mouse[1], 2) < math.pow(r, 2):
                if click[0] == 1:
                    print(self.detail)
                    det = self.detail
                    self.game.selectedDetail(det)
                    self.haveDetail = False
            else:
                pygame.draw.circle(screen, (13, 162, 58, 100), (x, y), r)

