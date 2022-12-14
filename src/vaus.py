import pygame


class Vaus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Creates a paddle at x, y with a width of w
        args: int x, int y, int w
        """
        super().__init__()
        self.image = pygame.image.load("assets/vaus.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x):
        """
        Updates the x position to the same as the mouse x
        args: int x
        """
        self.rect.centerx = x
