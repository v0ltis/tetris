import pygame
import typing


class Button:
    def __init__(self, coords: typing.Tuple[float, float], height: float, width: float, font: pygame.font.Font,
                 screen: pygame.display, text: str = "Button", funct: typing.Callable = None, one_press: bool = False):
        """
        Represents a button on the screen.

        :param coords: Tuple of the X and Y coordinates of the button
        :param height: Size of the button
        :param width: Size of the button
        :param font: Font of the button's text
        :param screen: The screen where the button will be displayed
        :param text: The text of the button
        :param funct: The function that will be called when the button is pressed
        :param one_press: If the button must trigger the associated function only once when pressed
        """

        self.x, self.y = coords
        # X and Y coordinates of the button

        self.height = height
        self.width = width
        # The height and width of the button

        self.function = funct
        # The associated function of the button

        self.one_press = one_press
        # If the button must trigger the associated function only once when pressed,

        # Buttons Definition:
        self.button_surface = pygame.Surface((self.width, self.height))
        # define a surface for the button
        self.button_rect = pygame.Rect((self.x, self.y, self.width, self.height))
        # button_rect is a pygame.Rect object, which is a rectangle with a position and a size

        self.font = font
        # the font of the button's text

        self.button_surf = self.font.render(text, True, (20, 20, 20))
        # the text of the button
        self.already_pressed = False
        # if the button has already been pressed

        self.screen = screen
        # the screen where the button will be displayed

    def process(self):
        self.button_surface.fill('#ffffff')
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if self.one_press:
                    self.function()
                elif not self.already_pressed:
                    self.function()
                    self.already_pressed = True
            else:
                self.already_pressed = False
        self.button_surface.blit(self.button_surf, [
            self.button_rect.width / 2 - self.button_surf.get_rect().width / 2,
            self.button_rect.height / 2 - self.button_surf.get_rect().height / 2
        ])
        self.screen.blit(self.button_surface, self.button_rect)
