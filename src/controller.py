import pygame
from src.ball import Ball
from src.brick import Brick
from src.vaus import Vaus


DISPLAY_WIDTH = 768
DISPLAY_HEIGHT = 1024


class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Arkanoid")

    def mainloop(self):
        self.menuloop()
        while True:
            self.gameloop()
        self.gameoverloop()
        # select state loop

    ### below are some sample loop states ###

    def menuloop(self):
        self.vaus = pygame.sprite.Group()
        vaus = Vaus(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT - 100, 10)
        self.vaus.add(vaus)
        self.balls = pygame.sprite.Group()
        ball = Ball()
        ball.rect.bottom = vaus.rect.top
        self.balls.add(ball)
        # event loop

        # update data

        # redraw

    def gameloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    raise SystemExit
            elif event.type == pygame.MOUSEMOTION:
                self.vaus.update(event.pos[0])
                self.balls.update(event.pos[0])

        # event loop

        # update data

        # redraw
        self.screen.fill("white")
        self.vaus.draw(self.screen)
        self.balls.draw(self.screen)
        pygame.display.flip()

    def gameoverloop(self):
        pass
        # event loop

        # update data

        # redraw
