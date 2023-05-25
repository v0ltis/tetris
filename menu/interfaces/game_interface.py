import pygame
from time import sleep
from classes.gamemode import Gamemode
import os
import sys
#from classes.game_logic import GameLogic


class GameInterface:

    # Init with the Gamemode choosen and the matrix
    def __init__(self, gamemode: Gamemode, matrix):
        self.gamemode = gamemode
        self.matrix = matrix

        # Load the fonts:
        font_path = os.path.dirname(sys.argv[0]) + "/font/upheavtt.ttf"
        self.font = pygame.font.Font(font_path, 40)

    def display_tetris_text(self, font, script: str, coord: tuple, color):
        text = font.render(script, True, color)
        text_rect = text.get_rect()
        text_rect.center = coord

        self.screen.blit(text, text_rect)

    # Draw the board to play on
    def process(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Triste")

        color_next = (72, 72, 72)
        pygame.draw.rect(self.screen, color_next, pygame.Rect(375,100,200,150))
        self.display_tetris_text(self.font, "NEXT PIECE", (475, 275), (255,255,255))
        self.display_tetris_text(self.font, "Time", (475, 550), (255,255,255))
        self.display_tetris_text(self.font, "Score", (475, 650), (255,255,255))

        while True:
            self.display_grid()
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(400, 675, 150, 50))
            self.display_tetris_text(self.font, str(self.gamemode.get_score()), (475, 700), (255,255,255))
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(400, 575, 150, 50))
            self.display_tetris_text(self.font, str(int(self.gamemode.get_time())), (475, 600), (255,255,255))
            pygame.display.flip()
            sleep(0.2)
            self.control_down()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    # TODO: CONNECT THE GAMEMODE CLASS TO THE INTERFACE, SO THE GAMEMODE LOGIC IS EXECUTED IN THE WHILE LOOP

    # Draw the grid and the actual piece
    # TODO: DOCUMENTATION!!!!!!!!!!!!!!!!!!!
    def display_grid(self):
        grid = self.matrix.game_matrix()
        for x in range(22):
            for y in range(10):
                box = grid[x][y]
                case_x = 100 + x*31 
                case_y = 30 + y*31
                pygame.draw.rect(self.screen, box.color, pygame.Rect(case_y, case_x, 29.5, 29.5))
                if box == 1:
                    pygame.draw.rect(self.screen, box.color, pygame.Rect(case_y, case_x, 29.5, 29.5))

    def control_down(self):
        # if the piece is placed
        can_still_be_moved, _, _ = self.matrix.down(self.gamemode.actual_piece)
        # if the piece is placed, we go to the next round.
        if not can_still_be_moved:
            self.gamemode.next_round()
