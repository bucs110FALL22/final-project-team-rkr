import pygame


class Brick(pygame.sprite.Sprite):

    def __init__(self, x, y, t):
        """
        Creates a brick object at x, y with different variations (hp and items)
        args: int x, int y, int t
        """
        super().__init__()
        hp = {0: 1}
        self.x = x
        self.y = y
        self.type = t
        self.hp = hp[self.type]
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()

    def take_damage(self, damage):
        """
        Reduces hp of the brick and updates sprite
        args: int damage
        """
        self.hp -= damage

    def drop_item():
        """
        Creates an item object which drops downwards from the brick
        """
        return
