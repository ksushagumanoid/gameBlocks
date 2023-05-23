import pygame
import Button

pygame.init()
res = (600, 800)
screen = pygame.display.set_mode(res)
current_scene = None


def switch_scene(scene):
    global current_scene
    current_scene = scene


def startScene():
    start = True
    button = Button.Button(100, 100, 2)
    while start:
        pygame.display.set_caption("start")
        screen.fill((255, 0, 0))
        button.draw(screen, 100, 100, "start", draw.gameScene)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                switch_scene(None)


def gameScene():
    game = True
    button = Button.Button(100, 100, 1)
    while game:
        pygame.display.set_caption("game")
        screen.fill((0, 255, 0))
        button.draw(screen, 100, 100, "back", switch_scene, startScene)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                switch_scene(None)



switch_scene(gameScene)
while current_scene is not None:
    current_scene()
