import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, t=0):
        """
        Creates a brick object at x, y with different variations (hp and items)
        args: int x, int y, int t
        """
        super().__init__()
        hp = {1: 1}
        self.type = t
        self.hp = hp[self.type]
        self.image = pygame.image.load("assets/brick.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def take_damage(self, damage):
        """
        Reduces hp of the brick and updates sprite
        args: int damage
        """
        self.hp -= damage

    def update(self):
        if self.hp > 0:
            pass

    def get_hp(self):
        return self.hp

    def drop_item():
        """
        Creates an item object which drops downwards from the brick
        """
        return
