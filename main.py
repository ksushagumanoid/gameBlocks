import pygame
import Button
import game

pygame.init()

current_scene = None

I = 10
J = 20
I_J_Choice = 6
tile = 40
RES = 900, 950
GAME_RES = I * tile, J * tile
GAME_CHOICE = I_J_Choice * tile, I_J_Choice * tile
game = game.Game(I, J, tile)
grid = []
game.fillGrid(grid)
choice = []
game.fillChoice(choice)

screen = pygame.display.set_mode(RES)
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

game.details()

gameProcess = True
while gameProcess:
    screen.blit(bg, (0, 0))
    screen.blit(game_screen, (30, 30))
    game_screen.blit(game_bg, (30, 30))
    screen.blit(choiceScreen[0], (50 + tile * I + 10, 50))
    screen.blit(choiceScreen[1], (50 + tile * I + 10, 50 + I_J_Choice * tile + 25))
    screen.blit(choiceScreen[2], (50 + tile * I + 10, 50 + I_J_Choice * tile * 2 + 50))
    r = buttonChoice[0].height // 5

    game.drawField(game_screen, grid)
    for k in range(3):
        game.drawField(choiceScreen[k], choice)



    buttonChoice[0].draw_circle(screen, 50 + tile * I + tile * I_J_Choice + r + 20, 50 + 20 * 2 + r * 2)
    buttonChoice[1].draw_circle(screen, 50 + tile * I + tile * I_J_Choice + r + 20, 50 +
                                tile * I_J_Choice + 20 * 2 + r * 2)
    buttonChoice[2].draw_circle(screen, 50 + tile * I + tile * I_J_Choice + r + 20,
                                50 + tile * 2 * I_J_Choice + 20 * 3 + r * 2)

    game.drawChoice(choiceScreen, buttonChoice)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION and game.draw_det:
            if 0 < event.pos[0] - 50 + tile < tile * I and 0 < event.pos[1] - 50 + tile < tile * J:
                x = event.pos[0] - event.pos[0] % tile
                y = event.pos[1] - event.pos[1] % tile
                game.moveDet(game_screen, x, y)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game.draw_det:
            if 30 + tile < event.pos[0] < tile * I + 30 - tile and 0 < event.pos[1] - 30 - tile < tile * J:
                game.placement(game_screen, grid)



    game.check_win(grid)



    if not all(but.detail for but in buttonChoice):
        if not game.draw_det:
            game.newChoice(choiceScreen, choice, buttonChoice)



    pygame.display.flip()
    clock.tick(fps)
