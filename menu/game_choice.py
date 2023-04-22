import pygame
from button import Button

pygame.init()

def function():
    print("Yes")

def game_choice():
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("Gamemode")

    one_piece = Button((20,100),200,250,"One Piece", function)
    basic_mode = Button((20,400),200,250,"Basic Mode", function)
    hard_mode = Button((330,100),200,250,"Hard Mode", function)
    wtf = Button((330,400),200,250,"wtf?!?", function)


    objects = [one_piece, basic_mode, hard_mode, wtf]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for object in objects:
            object.process()

        pygame.display.flip()