import pygame
from classes.button import Button
from interfaces.menu_heritage_sample import MenuHeritage
import sys


class PauseMenu(MenuHeritage):
    def __init__(self, game_interface_object, matrix, gamemode):

        self.game_inter_object = game_interface_object

        self.matrix = matrix

        self.gamemode = gamemode

        self.font = pygame.font.Font(sys.path[0] + "/font/upheavtt.ttf", 40)

        self.objects = []

    def process(self):
        # clear the screen:
        self.pygame = pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("triste")

        self.display_tetris_text(self.font, "Your score: ", (300, 200), (255, 255, 255))
        self.display_tetris_text(self.font, str(self.gamemode.get_score()), (300, 250), (255, 255, 255))

        self.display_tetris_text(self.font, "Time: ", (300, 350), (255, 255, 255))
        self.display_tetris_text(self.font, str(int(self.gamemode.get_time())), (300, 400), (255, 255, 255))

        button_resume = Button(
            coords=(150, 550), height=50, width=300, font=self.font,
            text="Resume Game", funct=self.resume_game, screen=self.screen
        )

        self.objects.append(button_resume)

        button_quit = Button(
            coords=(150, 700), height=50, width=300, font=self.font,
            text="Quit", funct=self.quit_function, screen=self.screen
        )

        self.objects.append(button_quit)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            for obj in self.objects:
                obj.process()

            pygame.display.flip()

    def resume_game(self):
        self.gamemode.resume()
        self.game_inter_object(self.gamemode, self.matrix).process()

    def display_tetris_text(self, font, script: str, coord: tuple, color):
        text = font.render(script, True, color)
        text_rect = text.get_rect()
        text_rect.center = coord

        self.screen.blit(text, text_rect)
