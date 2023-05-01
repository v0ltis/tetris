import pygame
from menu.classes.gamemode import Gamemode


class GameInterface:
    def __init__(self, gamemode: Gamemode, matrix):
        self.gamemode = gamemode

    def process(self):
        pygame.init()
        screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Triste")

        color = (128, 128, 128)
        pygame.draw.rect(screen, color, pygame.Rect(30,100,400,650))
        color_next = (72, 72, 72)
        pygame.draw.rect(screen, color_next, pygame.Rect(450,200,130,100))

        while True:
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    # TODO: CONNECT THE GAMEMODE CLASS TO THE INTERFACE, SO THE GAMEMODE LOGIC IS EXECUTED IN THE WHILE LOOP