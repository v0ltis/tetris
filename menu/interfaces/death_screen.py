import pygame
from classes.gamemode import Gamemode
from classes.button import Button
from classes.server import Server
from interfaces.scoreboard import Scoreboard
from datetime import datetime
import sys
import time


class DeathScreen:

    def __init__(self, gamemode: Gamemode):
        self.gamemode = gamemode

        # Load the fonts:
        font_path = sys.path[0] + "/font/upheavtt.ttf"
        self.font = pygame.font.Font(font_path, 40)

        self.error_font = pygame.font.Font(font_path, 30)

        self.objects = []

        self.server = Server()

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

        button_send = Button(
            coords=(150, 450), height=50, width=300, font=self.font,
            text="Send", funct=self.send, screen=self.screen
        )

        button_quit = Button(
            coords=(150, 700), height=50, width=300, font=self.font,
            text="Quit", funct=self.quit_function, screen=self.screen
        )

        self.objects.append(button_quit)
        self.objects.append(button_send)
        self.text = ""

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
                        self.text = self.text[:-1]

                    # Unicode standard is used for string
                    # formation
                    else:
                        if len(self.text) < 13:
                            self.text += event.unicode

            self.display_tetris_text(self.font, self.text, (300, 350), (255, 255, 255))

            # Button to go see the scoreboard ?

            for obj in self.objects:
                obj.process()

            pygame.display.flip()

    def quit_function(self):
        self.pygame.quit()
        print("Merci d'avoir joué")

    def send(self):

        # Resume allow us to update the timer, and take in count the pause time when
        # writing username
        self.gamemode.resume()

        timer = self.gamemode.get_time()
        if not self.text.isspace() or self.text != "":
            success = self.server.send_stats(name=self.text, score=self.gamemode.get_score(), date=datetime.now(), gamemode=self.gamemode.id, duration=timer)

            if not success:
                pygame.draw.rect(self.screen, (72, 72, 72), pygame.Rect(10, 650, 580, 115))
                self.display_tetris_text(self.font, "Une erreur est survenue", (300, 675), (255, 255, 255))
                self.display_tetris_text(self.font, "lors de l'envoi de vos", (300, 705), (255, 255, 255))
                self.display_tetris_text(self.font, "statistiques au serveur.", (300, 735), (255, 255, 255))

                wait_time = time.time() + 5

                while time.time() < wait_time:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.quit_function()

                    pygame.display.flip()

        Scoreboard(self.gamemode).process()
