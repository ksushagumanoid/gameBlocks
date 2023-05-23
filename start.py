import game as g
import pygame
import Button
import game
import random

pygame.init()
res = (1100, 950)
screen = pygame.display.set_mode(res)
current_scene = None

def text(message, font_sixe, x, y):
    text_color = (255, 255, 255)  # Белый цвет (RGB)
    font = pygame.font.Font(None, font_sixe)  # Шрифт None (по умолчанию), размер 36
    str = font.render(message, True, text_color)
    text_rect = str.get_rect()
    text_rect.x = x
    text_rect.y = y
    return str, text_rect
def switch_scene(scene):
    global current_scene
    current_scene = scene


def startScene():
    start = True
    buttonStart = Button.Button(450, 100, 3)
    buttonEasy = Button.Button(150, 100, 7)
    buttonMiddle = Button.Button(150, 100, 8)
    buttonHard = Button.Button(150, 100, 9)
    buttonRules = Button.Button(450, 100, 4)
    buttonAuthor = Button.Button(450, 100, 5)
    bg = pygame.image.load('out.jpg').convert()
    pygame.display.set_caption("start")
    str, sel_dif = text("Select difficulty:", 40, 100, 350)
    while start:

        screen.blit(bg, (0, 0))
        screen.blit(str, sel_dif)
        buttonStart.draw(screen, 100, 200, "start", gameScene, (10, 20))
        buttonEasy.draw(screen, 100, 400, "EASY", gameScene, (15, 20))
        buttonMiddle.draw(screen, 250, 400, "MIDDLE", gameScene, (15, 10))
        buttonHard.draw(screen, 400, 400, "HARD", gameScene, (10, 10))
        buttonRules.draw(screen, 100, 600, "Rules", rulesScene)
        buttonAuthor.draw(screen, 100, 800, "About Author", aboutScene)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                switch_scene(None)

def difScene():
    buttonEasy = Button.Button(400, 100, 7)
    buttonMiddle = Button.Button(400, 100, 8)
    buttonHard = Button.Button(400, 100, 9)
    start = True
    bg = pygame.image.load('out.jpg').convert()
    pygame.display.set_caption("Difficult")
    while start:
        screen.blit(bg, (0, 0))
        buttonEasy.draw(screen, 100, 200, "EASY", gameScene, (10, 20))
        buttonMiddle.draw(screen, 100, 400, "MIDDLE", gameScene, (10, 10))
        buttonHard.draw(screen, 100, 600, "HARD", gameScene, (5, 5))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                switch_scene(startScene)


def rulesScene():
    start = True
    bg = pygame.image.load('out.jpg').convert()
    pygame.display.set_caption("Rules")
    str = []
    rules = []
    for i in range(8):
        str.append(None)
        rules.append(None)
    dely = 100
    str[0], rules[0] = text("RULES", 50, 100, dely)
    str[1], rules[1] = text("Drag shapes across the grid and collect lines!", 40, 50, 90 + dely)
    str[2], rules[2] = text("1. Click on the button next to the shape you want to select", 40, 50, 140 + dely)
    str[3], rules[3] = text("2. Drive along the grid and see where it is better to put the figure", 40, 50, 190 + dely)
    str[4], rules[4] = text("3. Click on the left mouse button to put the figure on the field", 40, 50, 240 + dely)
    str[5], rules[5] = text("4. Look how colorful they are!", 40, 50, 290 + dely)
    str[6], rules[6] = text("5. Repeat this until the line is lined up!", 40, 50, 340 + dely)
    str[7], rules[7] = text("6. The game will end when you score the maximum number of points!", 40, 50, 390 + dely)

    while start:
        screen.blit(bg, (0, 0))
        for i in range(len(str)):
            screen.blit(str[i], rules[i])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                switch_scene(startScene)
def aboutScene():
    start = True
    bg = pygame.image.load('out.jpg').convert()
    pygame.display.set_caption("Author")
    str = []
    rules = []
    for i in range(8):
        str.append(None)
        rules.append(None)
    dely = 100
    str[0], rules[0] = text("ABOUT AUTHOR", 50, 100, dely)
    str[1], rules[1] = text("powered by Ponyatovskaya Ksenia", 40, 40, 90 + dely)
    str[2], rules[2] = text("student of CSF of Voronozh State University", 40, 50, 140 + dely)
    str[3], rules[3] = text("20 years old", 40, 50, 190 + dely)
    str[4], rules[4] = text("version 1.0.0", 40, 390, 640 + dely)
    str[5], rules[5] = text("Contacts:", 40, 50, 290 + dely)
    str[6], rules[6] = text("e-mail: ponyatksu@gmail.com", 40, 60, 340 + dely)
    str[7], rules[7] = text("phone: 89204199453", 40, 60, 390 + dely)
    while start:
        screen.blit(bg, (0, 0))
        for i in range(len(str)):
            screen.blit(str[i], rules[i])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                switch_scene(startScene)
def gameScene(I, J):
    font = pygame.font.Font(None, 70)

    I_J_Choice = 6
    tile = 40
    pygame.display.set_caption("game")
    GAME_RES = I * tile, J * tile
    GAME_CHOICE = I_J_Choice * tile, I_J_Choice * tile
    gameBoard = game.Game(I, J, tile)
    grid = []
    gameBoard.fillGrid(grid)
    choice = []
    gameBoard.fillChoice(choice)

    game_screen = pygame.Surface(GAME_RES)
    clock = pygame.time.Clock()
    fps = 60

    choiceScreen = []
    for k in range(3):
        choiceScreen.append(pygame.Surface(GAME_CHOICE))

    buttonChoice = []
    for k in range(3):
        buttonChoice.append(Button.Button(I_J_Choice * tile + 10, I_J_Choice * tile + 10, k, game))

    bg = pygame.image.load('out.jpg').convert()
    game_bg = pygame.image.load('in.jpg').convert()

    gameBoard.details()

    gameProcess = True
    while gameProcess:
        screen.blit(bg, (0, 0))
        screen.blit(game_screen, (30, 30))
        game_screen.blit(game_bg, (0, 0))
        screen.blit(choiceScreen[0], (50 + tile * I + 10, 50))
        screen.blit(choiceScreen[1], (50 + tile * I + 10, 50 + I_J_Choice * tile + 25))
        screen.blit(choiceScreen[2], (50 + tile * I + 10, 50 + I_J_Choice * tile * 2 + 50))
        r = buttonChoice[0].height // 5

        gameBoard.drawField(game_screen, grid)
        for k in range(3):
            gameBoard.drawField(choiceScreen[k], choice)

        buttonChoice[0].draw_circle(screen, 50 + tile * I + tile * I_J_Choice + r + 20,
                                    50 + 20 * 2 + r * 2,
                                    random.choice(gameBoard.colors), gameBoard)
        buttonChoice[1].draw_circle(screen, 50 + tile * I + tile * I_J_Choice + r + 20,
                                    50 + tile * I_J_Choice + 20 * 2 + r * 2,
                                    random.choice(gameBoard.colors), gameBoard)
        buttonChoice[2].draw_circle(screen, 50 + tile * I + tile * I_J_Choice + r + 20,
                                    50 + tile * 2 * I_J_Choice + 20 * 3 + r * 2,
                                    random.choice(gameBoard.colors), gameBoard)

        gameBoard.drawChoice(choiceScreen, buttonChoice)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION and gameBoard.draw_det:
                if 0 < event.pos[0] - 30 + tile < tile * I and 0 < event.pos[1] - 30 + tile < tile * J:
                    x = event.pos[0] - event.pos[0] % tile
                    y = event.pos[1] - event.pos[1] % tile
                    gameBoard.moveDet(game_screen, x, y)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and gameBoard.draw_det:
                if 30 + tile < event.pos[0] < tile * I + 30 - tile and 0 < event.pos[1] - 30 - tile < tile * J:
                    gameBoard.placement(game_screen, grid)

        gameBoard.check_win(grid)
        score = font.render("Total Score: {}".format(gameBoard.score), True, pygame.Color("White"))
        screen.blit(score, (30 + 80, 30 + tile * J + 40))

        if all(but.haveDetail == False for but in buttonChoice):
            if not gameBoard.draw_det:
                gameBoard.newChoice(choiceScreen, choice, buttonChoice)
                gameBoard.drawChoice(choiceScreen, buttonChoice)
        pygame.display.update()

        pygame.display.flip()
        clock.tick(fps)




switch_scene(startScene)
while current_scene is not None:
    current_scene()
