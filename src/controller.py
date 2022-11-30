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
        self.setup()

    def mainloop(self):
        while not self.start:
            self.menuloop()
        while True:
            self.gameloop()
        self.gameoverloop()
        # select state loop

    ### below are some sample loop states ###

    def menuloop(self):
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    raise SystemExit
            elif event.type == pygame.MOUSEMOTION:
                self.vaus.update(event.pos[0])
                for ball in self.balls:
                    ball.follow_mouse(event.pos[0])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.start = True
        # update data

        self.redraw()

    def gameloop(self):
        self.events()

        # update data

        self.redraw()

    def gameoverloop(self):
        # event loop

        # update data

        self.redraw()

    def setup(self):
        self.start = False
        self.vaus = pygame.sprite.Group()
        vaus = Vaus(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT - 100, 10)
        self.vaus.add(vaus)
        self.balls = pygame.sprite.Group()
        ball = Ball()
        ball.rect.bottom = vaus.rect.top
        self.balls.add(ball)
        level1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.bricks = pygame.sprite.Group()
        for i, row in enumerate(level1):
            for j, b in enumerate(row):
                board[i][j] = Brick(j * 80 + 24, (i + 1) * 20, b)
                self.bricks.add(board[i][j])

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    raise SystemExit
            elif event.type == pygame.MOUSEMOTION:
                self.vaus.update(event.pos[0])
        for ball in self.balls:
            if pygame.sprite.spritecollideany(ball, self.vaus):
                ball.bounce(0)
        self.check_boundary()
        self.balls.update()

    def check_boundary(self):
        for ball in self.balls:
            if ball.rect.bottom >= DISPLAY_HEIGHT:
                print("LOST")
            elif ball.rect.top <= 0:
                ball.bounce(0)
            elif ball.rect.left <= 0 or ball.rect.right >= DISPLAY_WIDTH:
                ball.bounce(1)

    def redraw(self):
        self.screen.fill("white")
        self.vaus.draw(self.screen)
        self.balls.draw(self.screen)
        self.bricks.draw(self.screen)
        pygame.display.flip()
