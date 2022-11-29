import pygame
import math


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        """
        Creates a ball object
        args: int x, int y
        """
        super().__init__()
        self.angle = 0
        self.damage = 1
        self.image = pygame.image.load("assets/ball.png")
        self.rect = self.image.get_rect()
    
    def update(self, x):
        self.rect.centerx = x

    def move_foward(self):
        """
        Moves the ball foward towards according to it's angle
        """
        self.x += 1 * math.cos(self.angle)
        self.y += 1 * math.sin(self.angle)

    def bounce(self):
        """
        Changes the angle of the ball
        """
        self.angle += 90