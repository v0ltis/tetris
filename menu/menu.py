import pygame
from pygame import mixer
import sys
import os
from button import Button
from Setting import setting
from game_choice import game_choice

pygame.init()
mixer.init()
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("Triste")

mixer.music.load(os.path.dirname(sys.argv[0]) + "/original-tetris-theme-tetris-soundtrack.mp3")
mixer.music.set_volume(1)
mixer.music.play(-1)
font_path = file_path = os.path.dirname(sys.argv[0]) + "/font/upheavtt.ttf"
font = pygame.font.Font(font_path , 100)

text = font.render("TETRIS", True, (255,255,255))
text_rect = text.get_rect()
text_rect.center = (300,100)

def game():
    game_choice()

def setting_function():
    setting()

def quit_function():
    pygame.quit()
    print("Merci d'avoir joué")

button_play = Button( (100,500), 75, 400, "Play", game)
button_settings = Button((100, 600), 75, 400, "Settings", setting_function)
button_quit = Button((150, 700), 50, 300, "Quit", quit_function)

objects = [button_play, button_settings, button_quit]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_function()
    
    screen.blit(text, text_rect)

    for object in objects:
        object.process()

    pygame.display.flip()