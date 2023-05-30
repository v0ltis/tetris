import pygame
import sys
from classes.button import Button
from classes.server import Server
from classes.gamemode import Gamemode
from datetime import datetime

class Scoreboard:

    def __init__(self, gamemode: Gamemode):

        font_path = sys.path[0] + "/font/upheavtt.ttf"
        self.font = pygame.font.Font(font_path, 20)

        self.gamemode = gamemode

        self.objects = []

        self.server = Server()

        self.error = False

        self.users = []

        self.get_users_data()

    def display_tetris_text(self, font, script: str, coord: tuple, color, left = False):
        text = font.render(script, True, color)
        text_rect = text.get_rect()

        text_rect.center = coord

        if left:
            text_rect.left = coord[0]

        self.screen.blit(text, text_rect)

    def get_users_data(self):

        server_resp = self.server.get_stats(quantity=10, offset=0, gamemode=self.gamemode.id)

        if server_resp is False:
            self.error = True

        else:
            self.users = server_resp

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

        while True:
            self.display_tetris_text(self.font, "Scoreboard", (300, 100), (255, 255, 255))

            if self.error:
                # Afficher message du style impossible de se connecter au serveur

                pass

            else:
                # afficher un tableau avec les valeurs, s'il n'y a pas eu d'erreur
                # côté serveur

                self.display_tetris_text(self.font, "Nom", (20, 200), (255, 255, 255), left=True)
                self.display_tetris_text(self.font, "Score", (150, 200), (255, 255, 255), left=True)
                self.display_tetris_text(self.font, "Durée", (250, 200), (255, 255, 255), left=True)
                self.display_tetris_text(self.font, "Date", (350, 200), (255, 255, 255), left=True)

                for i in range(len(self.users)):
                    user = self.users[i]

                    username = user["username"]
                    score = str(user["score"])
                    duration = str(int(user["duration"])) # We remove the .0 at the end

                    raw_timestamp = user["date"] # Date format: YYYY-MM-DDTHH:MM:SS

                    # Convert a string containing an hour to a datetime object
                    # For example, we are saying that the year is at the beginning of the string, then it's a "-" and then it's the month ...
                    # cf: https://docs.python.org/fr/3/library/datetime.html#strftime-and-strptime-format-codes
                    datetime_object = datetime.strptime(raw_timestamp, '%Y-%m-%dT%H:%M:%S')

                    # we now convert the datetime object to a super string, with format DD/MM/YYYY, HH:MM:SS
                    # cf: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
                    date = datetime_object.strftime("%d/%m/%Y, %H:%M:%S")

                    self.display_tetris_text(self.font, username, (20, 200 + (40 * (i+1) )), (255, 255, 255), left=True)
                    self.display_tetris_text(self.font, score, (150, 200 + (40 * (i+1))), (255, 255, 255), left=True)
                    self.display_tetris_text(self.font, duration, (250, 200 + (40 * (i+1) )), (255, 255, 255), left=True)
                    self.display_tetris_text(self.font, date, (350, 200 + (40 * (i+1) )), (255, 255, 255), left=True)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_function()

            for obj in self.objects:
                obj.process()

            pygame.display.flip()

    def quit_function(self):
        self.pygame.quit()
        print("Merci d'avoir joué")