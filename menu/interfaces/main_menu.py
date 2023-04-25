import pygame

from menu.interfaces.setting import Settings
from menu.classes.button import Button
from menu.interfaces.game_choice import GameChoice


class Menu:
    def __init__(
            self, pyg: pygame, mixer: pygame.mixer, screen: pygame.display, font: pygame.font, btn_font: pygame.font
    ):
        self.pygame = pyg

        self.mixer = mixer

        self.screen = screen

        self.font = font

        self.button_font = btn_font

        self.objects = []

    def load(self, window_name: str, music_path):
        # Initialize the window:
        self.pygame.display.set_caption(window_name)

        # Initialize the music player:
        self.mixer.music.load(music_path)
        self.mixer.music.set_volume(0.5)
        # -1 means that the music will loop
        self.mixer.music.play(-1)

        # initialize the font:
        text = self.font.render("TETRIS", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (300, 100)

        # Initialize the buttons:

        self.objects.append(
            Button(
                coords=(100, 500), height=75, width=400, font=self.button_font,
                text="Play", funct=self.game, screen=self.screen
            )
        )

        self.objects.append(
            Button(
                coords=(100, 600), height=75, width=400, font=self.button_font,
                text="Settings", funct=self.setting_function, screen=self.screen
            )
        )

        self.objects.append(
            Button(
                coords=(150, 700), height=50, width=300, font=self.button_font,
                text="Quit", funct=self.quit_function, screen=self.screen
            )
        )

    def display_tetris_text(self):
        text = self.font.render("TETRIS", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (300, 100)

        self.screen.blit(text, text_rect)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_function()

            self.display_tetris_text()

            for obj in self.objects:
                obj.process()

            pygame.display.flip()

    def game(self):
        # Go to the gamemode selection menu
        GameChoice(self).process()

    def setting_function(self):
        # Go to the settings menu
        Settings(self).process()

    def quit_function(self):
        self.pygame.quit()
        print("Merci d'avoir joué")
