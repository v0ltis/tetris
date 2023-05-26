import pygame
from classes.button import Button
from interfaces.menu_heritage_sample import MenuHeritage
from classes.launch_gamemode import GamemodeLauncher


class GameChoice(MenuHeritage):

    def __init__(self, menu):
        super().__init__(menu)

    def process(self):
        # clear the screen:
        self.menu.pygame = pygame.init()
        self.menu.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Triste")

        one_piece = Button(
            coords=(20, 50), height=200, width=250, font=self.menu.button_font,
            text="One Piece", funct=lambda: GamemodeLauncher(3).launch(), screen=self.menu.screen
        )

        basic_mode = Button(
            coords=(20, 300), height=200, width=250, font=self.menu.button_font,
            text="Basic Mode", funct=lambda: GamemodeLauncher(0).launch(), screen=self.menu.screen
        )

        hard_mode = Button(
            coords=(330, 50), height=200, width=250, font=self.menu.button_font,
            text="Blitz", funct=lambda: GamemodeLauncher(2).launch(), screen=self.menu.screen
        )

        one_color = Button(
            coords=(330, 300), height=200, width=250, font=self.menu.button_font,
            text="One Color", funct=lambda: GamemodeLauncher(1).launch(), screen=self.menu.screen
        )

        extended = Button(
            coords=(20, 550), height=200, width=250, font=self.menu.button_font,
            text="Extended", funct=lambda: GamemodeLauncher(4).launch(), screen=self.menu.screen
        )

        button_quit = Button(
            coords=(330, 550), height=200, width=250, font=self.menu.button_font,
            text="Quit", funct=self.quit_function, screen=self.menu.screen
        )

        self.menu.objects = [one_piece, basic_mode, hard_mode, one_color, extended, button_quit]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            for obj in self.menu.objects:
                obj.process()

            pygame.display.flip()
