import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, x, y, w):
        """
        Creates a paddle at x, y with a width of w
        args: int x, int y, int w
        """
        super().__init__()
        self.x = x
        self.y = y
        self.width = w
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()

    def change_size(self, w):
        """
        Increases or decreases the length of the paddle by w
        args: int w
        """
        self.width += w

    def move_right(self):
        """
        Moves the paddle to the right
        """
        self.x += 1

    def move_left(self):
        """
        Moves the paddle to the left
        """
        self.x -= 1
