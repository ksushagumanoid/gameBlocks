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
    str, sel_dif = text("Выберите сложность:", 40, 100, 350)
    name, rectName = text("Игра в Блоки", 100, 90, 80)
    while start:

        screen.blit(bg, (0, 0))
        screen.blit(str, sel_dif)
        screen.blit(name, rectName)
        buttonStart.draw(screen, 100, 200, "Cтарт", gameScene, (10, 20))
        buttonEasy.draw(screen, 100, 400, "ЛЕГКО", gameScene, (10, 10))
        buttonMiddle.draw(screen, 250, 400, "СРЕДНЕ", gameScene, (15, 10))
        buttonHard.draw(screen, 400, 400, "ТРУДНО", gameScene, (15, 20))
        buttonRules.draw(screen, 100, 600, "Правила", rulesScene)
        buttonAuthor.draw(screen, 100, 800, "Об авторе", aboutScene)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                switch_scene(lambda : endScene("Вы покинули игру."))


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
    str[0], rules[0] = text("Правила", 50, 100, dely)
    str[1], rules[1] = text("Перетаскивай фигуры по сетке и собирай линии!", 40, 50, 90 + dely)
    str[2], rules[2] = text("1. Нажмите на кнопку рядом с фигурой, которую вы хотите выбрать.", 40, 50, 140 + dely)
    str[3], rules[3] = text("2. Проедьтесь вдоль сетки и посмотрите, куда лучше поместить фигуру.", 40, 50, 190 + dely)
    str[4], rules[4] = text("3. Поставьте фигуру, нажав на левую кнопку мыши.", 40, 50, 240 + dely)
    str[5], rules[5] = text("4. Посмотрите, какие разноцветные фигуры получаются!", 40, 50, 290 + dely)
    str[6], rules[6] = text("5. Повторяйте это до тех пор, пока не выстроится линия!", 40, 50, 340 + dely)
    str[7], rules[7] = text("6. Игра закончится, когда вы наберете максимальное количество очков!", 40, 50, 390 + dely)

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
    str[0], rules[0] = text("ОБ АВТОРЕ", 50, 100, dely)
    str[1], rules[1] = text("создано Понятовской Ксенией", 40, 40, 90 + dely)
    str[2], rules[2] = text("Студентка 2 курса ФКН Воронежского Государственного Университета", 40, 50, 140 + dely)
    str[3], rules[3] = text("20 лет", 40, 50, 190 + dely)
    str[4], rules[4] = text("версия 1.0.0", 40, 390, 640 + dely)
    str[5], rules[5] = text("Контакты:", 40, 50, 290 + dely)
    str[6], rules[6] = text("e-mail: ponyatksu@gmail.com", 40, 60, 340 + dely)
    str[7], rules[7] = text("Телефон: 89204199453", 40, 60, 390 + dely)
    while start:
        screen.blit(bg, (0, 0))
        for i in range(len(str)):
            screen.blit(str[i], rules[i])

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                switch_scene(startScene)


def endScene(string):
    start = True
    bg = pygame.image.load('out.jpg').convert()
    pygame.display.set_caption("end")
    str, rect = text(string, 50, 30, 150)
    buttonBack = Button.Button(170, 50, 3)
    while start:
        screen.blit(bg, (0, 0))
        screen.blit(str, rect)
        buttonBack.draw(screen, 300, 450, "Вернуться", startScene)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


def gameScene(I, J):
    font = pygame.font.Font(None, 60)

    I_J_Choice = 6
    tile = 40
    pygame.display.set_caption("game")
    buttonBack = Button.Button(300, 50, 3)
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
        ind = 'Вы покинули игру.'
        buttonBack.draw(screen, 50 + I * tile, I_J_Choice * tile + 600, "Вернуться", lambda: endScene(ind))
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
                gameProcess = False
                switch_scene(lambda: endScene("Вы покинули игру."))
            if event.type == pygame.MOUSEMOTION and gameBoard.draw_det:
                if 0 < event.pos[0] < tile * I and 0 < event.pos[1] < tile * J:
                    x = event.pos[0] - event.pos[0] % tile
                    y = event.pos[1] - event.pos[1] % tile
                    gameBoard.moveDet(game_screen, x, y)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and gameBoard.draw_det:
                if 30 < event.pos[0] < tile * I and 30 < event.pos[1] < tile * J:
                    gameBoard.placement(game_screen, grid)

        gameBoard.check_win(grid)
        score = font.render("Общий счет: {}".format(gameBoard.score), True, pygame.Color("White"))
        screen.blit(score, (30, 30 + tile * J + 40))

        if gameBoard.score >= 100 * max(gameBoard.I_max, gameBoard.J_max):
            switch_scene(endScene("Вы победили!"))
            gameProcess = False

        if all(but.haveDetail == False for but in buttonChoice):
            if not gameBoard.draw_det:
                gameBoard.newChoice(choiceScreen, choice, buttonChoice)
                gameBoard.drawChoice(choiceScreen, buttonChoice)
        pygame.display.update()
        clock.tick(fps)


switch_scene(startScene)
while current_scene is not None:
    current_scene()
