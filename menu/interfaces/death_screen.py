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
        font_path = sys.path[0] + "/font/upheavtt.ttf"
        self.font = pygame.font.Font(font_path, 40)

        self.objects = []

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

        self.objects.append(button_quit)
        text = ""

        while True:

            # Display the score you made
            self.display_tetris_text(self.font, "Your score: ", (300, 200), (255, 255, 255))
            self.display_tetris_text(self.font, str(self.gamemode.get_score()), (300, 250), (255, 255, 255))

            # You can enter your name
            self.display_tetris_text(self.font, "Enter you name: ", (300, 300), (255, 255, 255))
            color = (72, 72, 72)

            pygame.draw.rect(self.screen, color, pygame.Rect(10, 325, 580, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_function()

                elif event.type == pygame.KEYDOWN:

                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:

                        # get text input from 0 to -1 i.e. end.
                        text = text[:-1]

                    # Unicode standard is used for string
                    # formation
                    else:
                        if len(text) < 20:
                            text += event.unicode

            self.display_tetris_text(self.font, text, (300, 350), (255, 255, 255))

            # Button to go see the scoreboard ?

            for obj in self.objects:
                obj.process()

            pygame.display.flip()

    def quit_function(self):
        self.pygame.quit()
        print("Merci d'avoir joué")
