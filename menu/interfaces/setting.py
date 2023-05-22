import pygame
from classes.button import Button
from interfaces.menu_heritage_sample import MenuHeritage


class Settings(MenuHeritage):
    def __init__(self, menu):
        super().__init__(menu)

    def process(self):
        # clear the screen:
        self.menu.pygame = pygame.init()
        self.menu.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("triste")

        # button_play = Button((150, 550), 50, 300, "Play", test)
        button_play = Button(
            coords=(150, 550), height=50, width=300, font=self.menu.button_font,
            text="Play", funct=self.menu.game, screen=self.menu.screen
        )

        button_quit = Button(
            coords=(150, 700), height=50, width=300, font=self.menu.button_font,
            text="Quit", funct=self.quit_function, screen=self.menu.screen
        )

        self.menu.objects = [button_play, button_quit]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            for obj in self.menu.objects:
                obj.process()

            pygame.display.flip()
