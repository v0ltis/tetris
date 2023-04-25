import pygame
from pygame import mixer
import sys
import os

from interfaces.main_menu import Menu


def start():
    # Initialize pygame & mixer:
    pygame.init()
    mixer.init()
    screen = pygame.display.set_mode((600, 800))

    # Load the fonts:
    font_path = os.path.dirname(sys.argv[0]) + "/font/upheavtt.ttf"
    font = pygame.font.Font(font_path, 100)
    btn_font = pygame.font.Font(font_path, 40)

    # Initialize the menu:
    menu = Menu(pygame, mixer, screen, font, btn_font)
    menu.load("Tetris", os.path.dirname(sys.argv[0]) + "/music/original-tetris-theme-tetris-soundtrack.mp3")

    # Main loop:
    menu.start()


if __name__ == "__main__":
    start()
