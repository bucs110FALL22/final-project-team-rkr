import pygame
import math


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        """
        Creates a ball object
        args: int x, int y
        """
        super().__init__()
        self.angle = math.pi / 3
        self.changex = math.cos(self.angle)
        self.changey = math.sin(self.angle)
        self.damage = 1
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("assets/ball.png")
        self.rect = self.image.get_rect()

    def follow_mouse(self, x=0):
        self.rect.centerx = x
        self.x = x
        self.y = self.rect.centery

    def update(self):
        self.x += self.changex
        self.rect.centerx = self.x
        self.y -= self.changey
        self.rect.centery = self.y

    def bounce(self, direction):
        if direction == 0:
            self.changey *= -1
        elif direction == 1:
            self.changex *= - 1
