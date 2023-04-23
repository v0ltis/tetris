import pygame
from button import Button
from one_piece import game_one_piece
from basic_mode import basic
from hard_mode import hard
from impossible_mode import impossible

pygame.init()

def quit_function():
    pygame.quit()
    print("Merci d'avoir joué")

def game_choice():
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("Triste")

    one_piece = Button((20,50),200,250,"One Piece", game_one_piece)
    basic_mode = Button((20,300),200,250,"Basic Mode", basic)
    hard_mode = Button((330,50),200,250,"Hard Mode", hard)
    wtf = Button((330,300),200,250,"Impossible Mode", impossible)
    button_quit = Button((150, 700), 50, 300, "Quit", quit_function)


    objects = [one_piece, basic_mode, hard_mode, wtf, button_quit]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for object in objects:
            object.process()

        pygame.display.flip()