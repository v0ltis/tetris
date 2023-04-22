import pygame
from button import Button
from game_choice import game_choice

def test():
    game_choice()

def quit_function():
    pygame.quit()

def setting():
    pygame.init()

    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("Settings")

    button_play = Button((150, 550), 50, 300, "Play", test)
    button_quit = Button((150, 700), 50, 300, "Quit", quit_function)

    objects = [button_play, button_quit]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for object in objects:
            object.process()

        pygame.display.flip()