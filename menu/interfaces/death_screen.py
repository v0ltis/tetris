import pygame
from classes.gamemode import Gamemode
from classes.button import Button
#from classes.text_entry import TextEntry
import os
import sys


class DeathScreen:

    def __init__(self, gamemode: Gamemode):
        self.gamemode = gamemode

        # Load the fonts:
        font_path = os.path.dirname(sys.argv[0]) + "/font/upheavtt.ttf"
        self.font = pygame.font.Font(font_path, 40)

    def display_tetris_text(self, font, script: str, coord: tuple, color):
        text = font.render(script, True, color)
        text_rect = text.get_rect()
        text_rect.center = coord

        self.screen.blit(text, text_rect)

    def process(self):
        self.pygame = pygame
        self.pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Triste")

        button_quit = Button(
            coords=(150, 700), height=50, width=300, font=self.font,
            text="Quit", funct=self.quit_function, screen=self.screen
        )

        self.objects = [button_quit]

        self.text_enter = ""
        self.input_active = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_function()

            # Display the score you made
            self.display_tetris_text(self.font, "Your score: ", (300, 200), (255, 255, 255))
            self.display_tetris_text(self.font, str(self.gamemode.get_score()), (300, 250), (255, 255, 255))

            # You can enter your name
            self.display_tetris_text(self.font, "Enter you name: ", (300, 300), (255, 255, 255))
            color = (72, 72, 72)
            pygame.draw.rect(self.screen, color, pygame.Rect(300, 350, 100, 100))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.input_active = True
                    self.text_enter = ""
                elif event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.text_enter =  self.text_enter[:-1]
                    else:
                        self.text_enter += event.unicode

            self.display_tetris_text(self.font, self.text_enter, (300, 350), (255, 255, 255))
            print(self.text_enter)

            # Button to go see the scoreboard ?

            for obj in self.objects:
                obj.process()

            pygame.display.flip()

    def quit_function(self):
        self.pygame.quit()
        print("Merci d'avoir joué")