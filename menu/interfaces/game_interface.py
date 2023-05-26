import pygame
from time import sleep
from classes.gamemode import Gamemode
import os
import sys
from interfaces.death_screen import DeathScreen
from interfaces.menu_pause import PauseMenu


class GameInterface:

    # Init with the Gamemode choosen and the matrix
    def __init__(self, gamemode: Gamemode, matrix):
        self.gamemode = gamemode
        self.matrix = matrix

        # Load the fonts:
        font_path = sys.path[0] + "/font/upheavtt.ttf"
        self.font = pygame.font.Font(font_path, 40)

        self.is_ended = False

    def display_tetris_text(self, font, script: str, coord: tuple, color):
        text = font.render(script, True, color)
        text_rect = text.get_rect()
        text_rect.center = coord

        self.screen.blit(text, text_rect)

    # Draw the board to play on
    def process(self):

        # Initialize the interface
        self.init_display()

        while not self.is_ended:
            self.display_grid()

            # Prevent text from overlapping
            # this one is the score
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(400, 675, 150, 50))
            self.display_tetris_text(self.font, str(self.gamemode.get_score()), (475, 700), (255, 255, 255))

            # and this one is the time
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(400, 575, 150, 50))
            self.display_tetris_text(self.font, str(int(self.gamemode.get_time())), (475, 600), (255,255,255))
            pygame.display.flip()
            sleep(0.2)

            if self.gamemode.should_go_down():
                is_not_placed, _, _ = self.matrix.down(self.gamemode.actual_piece)

                if is_not_placed is False:
                    self.gamemode.next_round()

                    self.is_ended = self.matrix.loose()

            self.controll()

        # Fonction après la perte:
        DeathScreen(self.gamemode).process()

    def init_display(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Triste")

        # next-piece rectangle
        color_next = (72, 72, 72)
        pygame.draw.rect(self.screen, color_next, pygame.Rect(375, 100, 200, 150))

        # texts
        self.display_tetris_text(self.font, "NEXT PIECE", (475, 275), (255,255,255))
        self.display_tetris_text(self.font, "Time", (475, 550), (255,255,255))
        self.display_tetris_text(self.font, "Score", (475, 650), (255,255,255))

    # Draw the grid and the actual piece
    def display_grid(self):
        grid = self.matrix.game_matrix()
        for x in range(22):
            for y in range(10):
                box = grid[x][y]
                case_x = 100 + x*31 
                case_y = 30 + y*31
                pygame.draw.rect(self.screen, (128, 128, 128), pygame.Rect(case_y, case_x, 29.5, 29.5))
                # If the value on the grid equal 1, apply the color of the piece
                if box == 1:

                    # If the gamemode is set to invisible
                    if self.gamemode.invisible_pieces:
                        # If the box color is the same as the falling's one
                        if box.color == self.gamemode.actual_piece.color:
                            pygame.draw.rect(self.screen, box.color, pygame.Rect(case_y, case_x, 29.5, 29.5))

                    else:
                        pygame.draw.rect(self.screen, box.color, pygame.Rect(case_y, case_x, 29.5, 29.5))

        # display the next piece
        color_next = (72, 72, 72)
        pygame.draw.rect(self.screen, color_next, pygame.Rect(375, 100, 200, 150))

        next_piece = self.gamemode.next_piece
        for x in range(len(next_piece.display_shape)):
            for y in range(len(next_piece.display_shape[x])):
                if next_piece.display_shape[x][y] == 1:
                    pygame.draw.rect(self.screen, next_piece.color, pygame.Rect(430 + 31 * x, 130 + 31 * y, 29.5, 29.5))

    def controll(self):

        piece = self.gamemode.actual_piece

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                is_not_placed = None

                if event.key == pygame.K_LEFT:
                    self.matrix.left(piece)

                elif event.key == pygame.K_RIGHT:
                    self.matrix.right(piece)

                elif event.key == pygame.K_UP:
                    self.matrix.rotate(piece)

                elif event.key == pygame.K_DOWN:
                    is_not_placed, rows, _ = self.matrix.down(piece)

                elif event.key == pygame.K_SPACE:
                    is_not_placed, rows, _ = self.matrix.drop(piece)

                elif event.key == pygame.K_ESCAPE:
                    self.gamemode.pause()
                    PauseMenu(GameInterface, self.matrix, self.gamemode).process()

                if is_not_placed is False:
                    self.gamemode.add_score(rows)
                    self.gamemode.next_round()
                    self.is_ended = self.matrix.loose()

            elif event.type == pygame.QUIT:
                pygame.quit()