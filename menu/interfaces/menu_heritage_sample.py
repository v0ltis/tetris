class MenuHeritage:
    def __init__(self, menu):
        self.menu = menu

    def quit_function(self):
        self.menu.pygame.quit()
        print("Merci d'avoir joué")
