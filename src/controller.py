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
        while True:
            if not self.start:
                self.menuloop()
            elif self.lives > 0:
                self.gameloop()
            else:
                self.gameoverloop()
                self.game_over_events()
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
                self.vauses.update(event.pos[0])
                for ball in self.balls:
                    ball.rect.bottom = self.vaus.rect.top
                    ball.follow_mouse(event.pos[0])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.start = True
        # update data

        self.redraw()

    def gameloop(self):
        """
        Main game loop
        """
        self.events()  # checks for events
        for ball in self.balls:  # bounces from vauses
            if pygame.sprite.spritecollideany(ball, self.vauses):
                ball.bounce(0)
        for brick in self.bricks:  # break bricks
            for ball in self.balls:
                if pygame.sprite.collide_rect(brick, ball):
                    ball.bounce(self.x_or_y(brick.rect, ball.rect))
                    brick.take_damage(ball.damages())
        self.check_boundary()
        self.balls.update()
        self.bricks.update()
        self.redraw()

    def gameoverloop(self):
        """
        Game over loop and displays 'Game Over'
        """
        self.screen.fill("black")
        font = pygame.font.SysFont(None, 48)
        text = font.render("Game Over", True, "white")
        self.screen.blit(text, (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))
        pygame.display.flip()

    def setup(self):
        self.start = False
        self.lives = 3
        self.level = 1
        self.board_setup(self.level)
        self.pre_launch()

    def board_setup(self, level):
        """
        Creates the initial board
        """
        levels = [
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
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
        for i, row in enumerate(levels[level - 1]):
            for j, b in enumerate(row):
                board[i][j] = Brick(j * 80 + 24, (i + 1) * 20, b)
                self.bricks.add(board[i][j])

    def pre_launch(self):
        self.vauses = pygame.sprite.Group()
        self.vaus = Vaus(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT - 100, 10)
        self.vauses.add(self.vaus)
        self.balls = pygame.sprite.Group()
        ball = Ball()
        self.balls.add(ball)

    def events(self):
        """
        Checks for any events during the main game phase
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close the game
                raise SystemExit
            elif event.type == pygame.KEYDOWN:  # close the game
                if event.key == pygame.K_q:
                    raise SystemExit
            elif (
                event.type == pygame.MOUSEMOTION
            ):  # change position of vauses depending on mouse location
                self.vauses.update(event.pos[0])

    def game_over_events(self):
        """
        Checks for any events during the game over phase
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    raise SystemExit

    def check_boundary(self):
        """
        Determine if ball touches the edges of the window and change direction
        accordingly
        """
        for ball in self.balls:
            if ball.rect.bottom >= DISPLAY_HEIGHT:
                ball.kill()
                self.lives -= 1
                self.start = False
                self.pre_launch()
            elif ball.rect.top <= 0:
                ball.bounce(0)
            elif ball.rect.left <= 0 or ball.rect.right >= DISPLAY_WIDTH:
                ball.bounce(1)

    def x_or_y(self, rect1, rect2):
        """
        Returns 0 or 1 based on if the collision is right/left or top/bottom
        args: rect rect1, rect rect2
        """
        dr = abs(rect1.right - rect2.left)
        dl = abs(rect1.left - rect2.right)
        db = abs(rect1.bottom - rect2.top)
        dt = abs(rect1.top - rect2.bottom)
        if min(dl, dr) < min(dt, db):
            return 0
        else:
            return 1

    def redraw(self):
        """
        Redraws all updates to the game
        """
        self.screen.fill("white")
        self.vauses.draw(self.screen)
        self.balls.draw(self.screen)
        self.bricks.draw(self.screen)
        pygame.display.flip()
