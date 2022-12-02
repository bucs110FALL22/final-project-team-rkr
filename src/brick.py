import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, t=0):
        """
        Creates a brick object at x, y with different variations (hp and items)
        args: int x, int y, int t
        """
        super().__init__()
        hp = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: -1}
        self.type = t
        self.hp = hp[self.type]
        self.image = pygame.image.load(f"assets/brick{t}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def take_damage(self, damage):
        """
        Reduces hp of the brick and updates sprite
        args: int damage
        """
        self.hp -= damage

    def get_hp(self):
        """
        Returns hp left
        return: int hp
        """
        return self.hp

    def get_type(self):
        """
        Returns the brick type
        return: int type
        """
        return self.type
