import pygame
from src.ball import Ball
from src.brick import Brick
from src.vaus import Vaus
from src.gui import GUI

DISPLAY_WIDTH = 793
DISPLAY_HEIGHT = 1024

LEVELS = [
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    ],
    [
        [0, 6, 6, 6, 0, 6, 6, 6, 0, 6, 6, 6, 0],
        [0, 5, 5, 5, 0, 5, 5, 5, 0, 5, 5, 5, 0],
        [0, 4, 4, 4, 0, 4, 4, 4, 0, 4, 4, 4, 0],
        [0, 3, 3, 3, 0, 3, 3, 3, 0, 3, 3, 3, 0],
        [0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    ],
    [
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0, 0],
        [0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0],
        [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0],
        [0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0],
        [0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 4, 4, 0, 0, 6, 0, 0, 5, 5, 5, 0],
        [0, 4, 4, 4, 0, 0, 0, 0, 0, 5, 5, 5, 0],
        [0, 4, 4, 4, 0, 0, 0, 0, 0, 5, 5, 5, 0],
        [0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 3, 3, 3, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0],
        [0, 1, 1, 1, 0, 0, 6, 0, 0, 2, 2, 2, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0],
    ],
]


class Controller:
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        clock.tick(30)
        pygame.display.set_caption("Arkanoid")
        pygame.mouse.set_visible(False)
        self.gui = GUI()
        self.setup()

    def mainloop(self):
        """
        Loop to create each frame of game
        """
        while True:
            if not self.start:
                self.menuloop()
            elif self.lives > 0 and self.bricks_left > 0:
                self.gameloop()
            else:
                if self.score > self.high_score:
                    self.high_score = self.score
                    f = open("high_score.txt", "w")
                    f.write(str(self.high_score))
                    f.close()
                if self.bricks_left == 0:
                    self.gui.win_screen(self.score)
                else:
                    self.gui.lose_screen(self.score, self.high_score)
                self.game_over_events()

    def menuloop(self):
        """
        Menu / Start loop
        """
        self.menu_events()
        self.redraw()

    def gameloop(self):
        """
        Main game loop
        """
        self.game_events()
        self.check_boundary()
        for ball in self.balls:
            if pygame.sprite.spritecollideany(ball, self.vauses):
                ball.hit_vaus()
        self.break_bricks()
        if self.level != 4 and self.bricks_left == 0:
            self.next_level()
        self.balls.update()
        self.redraw()

    def setup(self):
        """
        Setup the game
        """
        self.start = False
        self.lives = 3
        self.level = 1
        self.speed = 2
        self.score = 0
        with open("high_score.txt") as f:
            self.high_score = int(f.readline())
        self.board_setup(self.level)
        self.pre_launch()

    def board_setup(self, l):
        """
        Creates bricks according to the current level
        args: level
        """
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.bricks_left = 0
        self.bricks = pygame.sprite.Group()
        for i, row in enumerate(LEVELS[l]):
            for j, b in enumerate(row):
                if b != 0:
                    board[i][j] = Brick(j * 61, (i + 2) * 31, b)
                    self.bricks.add(board[i][j])
                    self.bricks_left += 1

    def pre_launch(self):
        """
        Create the vaus and balls
        """
        self.vauses = pygame.sprite.Group()
        self.vaus = Vaus(0, DISPLAY_HEIGHT - 100)
        self.vaus.rect.centerx = DISPLAY_WIDTH // 2
        self.vauses.add(self.vaus)
        self.balls = pygame.sprite.Group()
        ball = Ball(self.speed)
        ball.rect.bottom = self.vaus.rect.top
        ball.follow_mouse(DISPLAY_WIDTH // 2)
        self.balls.add(ball)

    def next_level(self):
        """
        Setup the next level
        """
        self.level += 1
        self.speed_up()
        self.start = False
        self.board_setup(self.level)
        self.pre_launch()

    def menu_events(self):
        """
        Checks for any events(input) during the menu phase
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    raise SystemExit
                elif event.key == pygame.K_r:
                    self.setup()
            elif event.type == pygame.MOUSEMOTION:
                self.vauses.update(event.pos[0])
                for ball in self.balls:
                    ball.rect.bottom = self.vaus.rect.top
                    ball.follow_mouse(event.pos[0])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.start = True

    def game_events(self):
        """
        Checks for any events(input) during the main game phase
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    raise SystemExit
                elif event.key == pygame.K_r:
                    self.setup()
            elif event.type == pygame.MOUSEMOTION:
                self.vauses.update(event.pos[0])

    def game_over_events(self):
        """
        Checks for any events(input) during the game over phase
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    raise SystemExit
                elif event.key == pygame.K_r:
                    self.setup()

    def break_bricks(self):
        """
        Check for brick and ball collision
        Destory brick and make ball bounce if it has no hp
        """
        if pygame.sprite.groupcollide(
            self.bricks, self.balls, False, False
        ):  # break bricks
            for ball in self.balls:
                for brick in self.bricks:
                    if pygame.sprite.collide_rect(brick, ball):
                        ball.bounce()
                        brick.take_damage(ball.damages())
                        if brick.get_hp() <= 0:
                            self.bricks_left -= 1
                            self.score += brick.get_type() * 100
                            brick.kill()

    def check_boundary(self):
        """
        Determine if ball touches the edges of the window and change direction accordingly
        """
        for ball in self.balls:
            if ball.rect.bottom >= DISPLAY_HEIGHT:
                ball.kill()
                self.lives -= 1
                if self.lives > 0:
                    self.start = False
                    self.pre_launch()
            elif ball.rect.top <= 0:
                ball.hit_walls("topbottom")
            elif ball.rect.left <= 0 or ball.rect.right >= DISPLAY_WIDTH:
                ball.hit_walls("leftright")

    def speed_up(self):
        """
        Speeds up the ball speed
        """
        self.speed *= 1.2

    def redraw(self):
        """
        Redraws all updates to the game
        """
        self.gui.draw_background()
        self.gui.draw_vauses(self.vauses)
        self.gui.draw_balls(self.balls)
        self.gui.draw_bricks(self.bricks)
        if self.start == False:
            self.gui.instructions()
        self.gui.draw_score(self.score)
        self.gui.draw_lives(self.lives)
        self.gui.draw_level(self.level)
        self.gui.keybinds()
        pygame.display.flip()
