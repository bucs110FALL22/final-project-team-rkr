import pygame
import math
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, s):
        """
        Creates a ball object with speed s
        args: int speed
        """
        super().__init__()
        self.speed = s
        self.angle = random.randrange(30, 60) * math.pi / 180
        if random.randint(0, 1) == 0:
            self.angle = (self.angle * -1) + math.pi
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
        """
        Changes the ball to a semi-random direction
        """
        self.angle = random.randrange(30, 60) * math.pi / 180
        if self.changex < 0:
            self.angle = (self.angle * -1) + math.pi
        self.changex = math.cos(self.angle) * self.speed
        self.changey = math.sin(self.angle) * self.speed

    def bounce(self):
        """
        Bounces the ball
        """
        self.x -= self.changex * 2
        self.rect.centerx = self.x
        self.y += self.changey * 2
        self.rect.centery = self.y
        self.changey *= -1

    def hit_walls(self, direction):
        """
        Changes the direction of the ball based on the direction of collision
        args: str direction
        """
        if direction == "topbottom":
            self.changey *= -1
        elif direction == "leftright":
            self.changex *= -1

    def damages(self):
        """
        Returns the damage of the ball so other programs can read it
        return: int damage
        """
        return self.damage