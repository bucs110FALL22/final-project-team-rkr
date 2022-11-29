import pygame


class Vaus(pygame.sprite.Sprite):
    def __init__(self, x, y, w):
        """
        Creates a paddle at x, y with a width of w
        args: int x, int y, int w
        """
        super().__init__()
        self.width = w
        self.image = pygame.image.load("assets/vaus.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_size(self, w):
        """
        Increases or decreases the length of the paddle by w
        args: int w
        """
        self.width += w

    def update(self, x):
        self.rect.centerx = x