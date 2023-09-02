import pygame
import sys
from classes.button import Button
from interfaces.menu_heritage_sample import MenuHeritage


class Command(MenuHeritage):

    def __init__(self, menu):
        super().__init__(menu)

        font_path = sys.path[0] + "/font/upheavtt.ttf"
        self.font = pygame.font.Font(font_path, 20)

    def display_tetris_text(self, font, script: str, coord: tuple, color):
        text = font.render(script, True, color)
        text_rect = text.get_rect()
        text_rect.center = coord

        self.menu.screen.blit(text, text_rect)

    def process(self):
        #Clear the screen
        self.menu.pygame = pygame.init()
        self.menu.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("triste")

        button_play = Button(
            coords=(150, 675), height=50, width=300, font=self.menu.button_font,
            text="Play", funct=self.menu.game, screen=self.menu.screen
        )

        button_quit = Button(
            coords=(150, 750), height=50, width=300, font=self.menu.button_font,
            text="Quit", funct=self.menu.quit_function, screen=self.menu.screen
        )

        self.menu.objects = [button_play, button_quit]

        while True:
            #command
            self.display_tetris_text(self.font, "Right", (100, 100), (255, 255, 255))
            self.display_tetris_text(self.font, "Left", (100, 200), (255, 255, 255))
            self.display_tetris_text(self.font, "Up", (100, 300), (255, 255, 255))
            self.display_tetris_text(self.font, "Down", (100, 400), (255, 255, 255))
            self.display_tetris_text(self.font, "Space", (100, 500), (255, 255, 255))
            self.display_tetris_text(self.font, "R.Control", (100, 600), (255, 255, 255))


            #Text
            self.display_tetris_text(self.font, "Go right", (400, 100), (255, 255, 255))
            self.display_tetris_text(self.font, "Go left", (400, 200), (255, 255, 255))
            self.display_tetris_text(self.font, "Rotate the piece", (400, 300), (255, 255, 255))
            self.display_tetris_text(self.font, "Go down one block", (400, 400), (255, 255, 255))
            self.display_tetris_text(self.font, "Go full down", (400, 500), (255, 255, 255))
            self.display_tetris_text(self.font, "Hold piece", (400, 600), (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            for obj in self.menu.objects:
                obj.process()

            pygame.display.flip()