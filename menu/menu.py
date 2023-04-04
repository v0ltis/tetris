import pygame
import os
import sys
import typing

pygame.init()
screen = pygame.display.set_mode((600,800))

objects = []

font_path = file_path = os.path.dirname(sys.argv[0]) + "/font/upheavtt.ttf"
font = pygame.font.Font(font_path , 40)

class Button:
    
    def __init__(self, coords: typing.Tuple[float, float] , height:float, width:float, text:str="Button", funct:typing.Callable = None, one_press:bool = False):
        self.x , self.y = coords
        self.height = height
        self.width = width
        self.function = funct
        self.one_press = one_press

        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect((self.x, self.y, self.width, self.height))

        self.button_surf = font.render(text, True, (20,20,20))
        self.already_pressed = False

        objects.append(self)

    def process(self):
        self.button_surface.fill('#ffffff')
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.one_press:
                    self.function()
                elif not self.already_pressed:
                    self.function()
                    self.already_pressed = True
            else:
                self.already_pressed = False
        self.button_surface.blit(self.button_surf, [
            self.button_rect.width/2 - self.button_surf.get_rect().width/2,
            self.button_rect.height/2 - self.button_surf.get_rect().height/2
        ])
        screen.blit(self.button_surface, self.button_rect)

def function():
    print('It works')

def quit_function():
    pygame.quit()

button_play = Button(100, 500, 75, 400, "TEST", function)
button_settings = Button(100, 600, 75, 400, "Settings", function)
button_quit = Button(150, 700, 50, 300, "Quit", quit_function)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for object in objects:
        object.process()

    pygame.display.flip()