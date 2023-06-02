import pygame
import sys
from classes.button import Button
from interfaces.menu_heritage_sample import MenuHeritage
from interfaces.credits import Credits
from interfaces.command import Command


class Settings(MenuHeritage):
    def __init__(self, menu):
        super().__init__(menu)

        font_path = sys.path[0] + "/font/upheavtt.ttf"
        self.font = pygame.font.Font(font_path, 40)

    def display_tetris_text(self, font, script: str, coord: tuple, color):
        text = font.render(script, True, color)
        text_rect = text.get_rect()
        text_rect.center = coord

        self.menu.screen.blit(text, text_rect)

    def process(self):
        # clear the screen:
        self.menu.pygame = pygame.init()
        self.menu.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("triste")

        button_command = Button(
            coords=(150, 100), height=50, width=300, font=self.font,
            text="Commands", funct=self.command, screen=self.menu.screen
        )

        button_save = Button(
            coords=(150, 400), height=50, width=300, font=self.font,
            text="Save", funct=self.save, screen=self.menu.screen
        )

        button_credits = Button(
            coords=(150, 500), height=50, width=300, font=self.font,
            text="Credits", funct=self.credits, screen=self.menu.screen
        )

        button_play = Button(
            coords=(150, 675), height=50, width=300, font=self.menu.button_font,
            text="Play", funct=self.menu.game, screen=self.menu.screen
        )

        button_quit = Button(
            coords=(150, 750), height=50, width=300, font=self.menu.button_font,
            text="Quit", funct=self.quit_function, screen=self.menu.screen
        )

        self.menu.objects = [button_play, button_quit, button_save, button_credits, button_command]
        self.text = ""

        while True:

            self.display_tetris_text(self.font, "Enter the volume", (300, 250), (255, 255, 255))
            self.display_tetris_text(self.font, "between 0 and 1", (300, 300), (255, 255, 255))

            color = (72, 72, 72)
            pygame.draw.rect(self.menu.screen, color, pygame.Rect(10, 325, 580, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:

                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:

                        # get text input from 0 to -1 i.e. end.
                        self.text = self.text[:-1]

                    # Unicode standard is used for string
                    # formation
                    elif event.unicode in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                        if len(self.text) < 3:
                            self.text += event.unicode

            self.display_tetris_text(self.font, self.text, (300, 350), (255, 255, 255))

            for obj in self.menu.objects:
                obj.process()

            pygame.display.flip()

    def save(self):
        try:
            self.menu.mixer.music.set_volume(float(self.text))
        except:
            print("Could not change volume.")

    def credits(self):
        Credits.process(self)

    def command(self):
        Command.process(self)