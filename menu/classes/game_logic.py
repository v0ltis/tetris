from menu.classes.gamemode import Gamemode
from menu.interfaces.game_interface import GameInterface
import pygame


class GameLogic:
    """
    Must be invoked by the GameInterface class, when Gamemode and Interface is set up.
    """
    def __init__(self, gamemode: Gamemode, interface: GameInterface, matrix):
        self.gamemode = gamemode
        self.interface = interface
        self.matrix = matrix

    def process(self):
        """
        This is a SAMPLE, it WILL need to be changed.
        """

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self.matrix.move_left()

                if event.key == pygame.K_RIGHT:
                    self.matrix.move_right()

                if event.key == pygame.K_UP:
                    self.matrix.rotate()

                if event.key == pygame.K_SPACE:
                    self.matrix.drop()

                if event.key == pygame.K_ESCAPE:
                    return "pause"