class MenuHeritage:
    def __init__(self, menu):
        self.menu = menu

    def quit_function(self):
        self.menu.pygame.quit()
        self.menu.sys.quit()
        print("Merci d'avoir joué")
