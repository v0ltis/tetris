import pygame
import sys
from classes.button import Button

class Credits:

    def __init__(self):
        font_path = sys.path[0] + "/font/upheavtt.ttf"
        self.font = pygame.font.Font(font_path, 40)

        self.objects = []

    def display_tetris_text(self, font, script: str, coord: tuple, color):
        text = font.render(script, True, color)
        text_rect = text.get_rect()
        text_rect.center = coord

        self.screen.blit(text, text_rect)

    def process(self):
        self.pygame = pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("triste")

        button_quit = Button(
            coords=(150, 750), height=50, width=300, font=self.font,
            text="Quit", funct=self.quit_function, screen=self.screen
        )

        self.image_barnabe = pygame.image.load(sys.path[0] + "/image/Barnabé.png").convert()
        self.image_valer = pygame.image.load(sys.path[0] + "/image/Valérian.png").convert()

        self.objects = [button_quit]

        while True:

            self.display_tetris_text(self.font, "This game was made", (300, 100), (255, 255, 255))
            self.display_tetris_text(self.font, "By the 2 best student", (300, 150), (255, 255, 255))
            self.display_tetris_text(self.font, "Of M.CHEVALIER-GALLAIS", (300, 200), (255, 255, 255))
            self.display_tetris_text(self.font, "In 2022/2023", (300, 250), (255, 255, 255))

            self.display_tetris_text(self.font, "Barbabé", (475, 475), (255, 255, 255))
            self.image_barnabe = pygame.transform.scale(self.image_barnabe, (152.7, 149.1))
            self.screen.blit(self.image_barnabe, (400, 500))
            self.display_tetris_text(self.font, "*Barnabé", (475, 675), (255, 255, 255))

            self.display_tetris_text(self.font, "Valériane", (150, 475), (255, 255, 255))
            self.image_valer = pygame.transform.scale(self.image_valer, (152.7, 149.1))
            self.screen.blit(self.image_valer, (70, 500))
            self.display_tetris_text(self.font, "*Valérian", (150, 675), (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            for obj in self.objects:
                obj.process()

            pygame.display.flip()

    def quit_function(self):
        pygame.quit()