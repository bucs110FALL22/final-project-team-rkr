import pygame
import math
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        """
        Creates a ball object
        args: int x, int y
        """
        super().__init__()
        self.speed = 3
        self.angle = random.randrange(30, 60) * math.pi / 180
        self.changex = math.cos(self.angle) * self.speed
        self.changey = math.sin(self.angle) * self.speed
        self.damage = 1
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("assets/ball.png")
        self.rect = self.image.get_rect()

    def follow_mouse(self, x=0):
        """
        Updates the x position to the same as the mouse x
        args: int x
        """
        self.rect.centerx = x
        self.x = x
        self.y = self.rect.centery

    def update(self):
        """
        Updates x and y and mirrors the rect values accordingly since rect
        only allows for integer values
        """
        self.x += self.changex
        self.rect.centerx = self.x
        self.y -= self.changey
        self.rect.centery = self.y

    def hit_vaus(self):
        self.angle = random.randrange(30, 60) * math.pi / 180
        if self.changex < 0:
            self.angle = (self.angle * -1) + math.pi
        self.changex = math.cos(self.angle) * self.speed
        self.changey = math.sin(self.angle) * self.speed

    def bounce(self):
        """
        Changes the direction of the ball
        """
        self.changey *= -1

    def hit_walls(self, direction):
        if direction == "topbottom":
            self.changey *= -1
        elif direction == "leftright":
            self.changex *= -1

    def damages(self):
        """
        Returns the damage of the ball so other programs can read it
        """
        return self.damage
