import pygame
from src.ball import Ball
from src.brick import Brick
from src.vaus import Vaus


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
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Arkanoid")
        pygame.mouse.set_visible(False)
        with open("high_score.txt") as f:
            self.high_score = int(f.readline())
        self.setup()

    def mainloop(self):
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
                    self.win()
                else:
                    self.gameoverloop()
                self.game_over_events()
        # select state loop

    def menuloop(self):
        self.menu_events()
        # update data
        self.redraw()

    def gameloop(self):
        """
        Main game loop
        """
        self.game_events()  # checks for events
        self.check_boundary()
        for ball in self.balls:  # bounces from vauses
            if pygame.sprite.spritecollideany(ball, self.vauses):
                ball.hit_vaus()
        self.break_bricks()
        if self.level != 4 and self.bricks_left == 0:
            self.next_level()
        self.balls.update()
        self.redraw()

    def win(self):
        """
        Win loop and displays 'You Win'
        """
        self.screen.fill("green")
        big_font = pygame.font.SysFont(None, 96)
        font = pygame.font.SysFont(None, 48)
        text = big_font.render("You Win!", True, "black")
        text_rect = text.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 - 96))
        self.screen.blit(text, text_rect)
        score = font.render(f"Your score was {self.score}", True, "black")
        score_rect = score.get_rect(
            center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + 48)
        )
        self.screen.blit(score, score_rect)
        self.keybinds()
        pygame.display.flip()

    def gameoverloop(self):
        """
        Game over loop and displays 'Game Over'
        """
        self.screen.fill("red")
        big_font = pygame.font.SysFont(None, 96)
        font = pygame.font.SysFont(None, 48)
        text = big_font.render("Game Over", True, "black")
        text_rect = text.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 - 96))
        self.screen.blit(text, text_rect)
        score = font.render(f"Your score was {self.score}", True, "black")
        score_rect = score.get_rect(
            center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + 48)
        )
        self.screen.blit(score, score_rect)
        high_score = font.render(
            f"Your high score was {self.high_score}", True, "black"
        )
        high_score_rect = high_score.get_rect(
            center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + 96)
        )
        self.screen.blit(high_score, high_score_rect)
        self.keybinds()
        pygame.display.flip()

    def setup(self):
        self.start = False
        self.lives = 3
        self.level = 1
        self.score = 0
        self.speed = 2
        self.bg = pygame.image.load("assets/background.png")
        self.board_setup(self.level)
        self.pre_launch()

    def board_setup(self, level):
        """
        Creates the initial board
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
        for i, row in enumerate(LEVELS[level]):
            for j, b in enumerate(row):
                if b != 0:
                    board[i][j] = Brick(j * 61, (i + 2) * 31, b)
                    self.bricks.add(board[i][j])
                    self.bricks_left += 1

    def pre_launch(self):
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
        self.level += 1
        self.speed_up()
        self.start = False
        self.board_setup(self.level)
        self.pre_launch()

    def menu_events(self):
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
        Checks for any events during the main game phase
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close the game
                raise SystemExit
            elif event.type == pygame.KEYDOWN:  # close the game
                if event.key == pygame.K_q:
                    raise SystemExit
                elif event.key == pygame.K_r:
                    self.setup()
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
                elif event.key == pygame.K_r:
                    self.setup()

    def break_bricks(self):
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
        Determine if ball touches the edges of the window and change direction
        accordingly
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
        self.speed *= 1.2

    def instructions(self):
        """
        Displays instructions on how to start
        """
        font = pygame.font.SysFont(None, 48)
        start = font.render("Left Click to Start", True, "white")
        start_rect = start.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))
        self.screen.blit(start, start_rect)

    def keybinds(self):
        """
        Displays keybinds on the bottom of the screen
        """
        font = pygame.font.SysFont(None, 36)
        restart = font.render("Press R to Restart", True, "white")
        restart_rect = restart.get_rect(left=0, bottom=(DISPLAY_HEIGHT))
        self.screen.blit(restart, restart_rect)
        quit = font.render("Press Q to Quit", True, "white")
        quit_rect = quit.get_rect(right=DISPLAY_WIDTH, bottom=(DISPLAY_HEIGHT))
        self.screen.blit(quit, quit_rect)

    def show_level(self):
        """
        Displays the level
        """
        font = pygame.font.SysFont(None, 48)
        text = font.render(f"Level: {self.level}/4", True, "white")
        self.screen.blit(text, (0, 0))

    def show_score(self):
        """
        Displays the score
        """
        font = pygame.font.SysFont(None, 48)
        text = font.render(f"Score: {self.score}", True, "white")
        text_rect = text.get_rect(center=(DISPLAY_WIDTH // 2, 24))
        self.screen.blit(text, text_rect)

    def show_lives(self):
        """
        Displays lives left
        """
        font = pygame.font.SysFont(None, 48)
        text = font.render(f"Lives: {self.lives}", True, "white")
        text_rect = text.get_rect(right=DISPLAY_WIDTH)
        self.screen.blit(text, text_rect)

    def redraw(self):
        """
        Redraws all updates to the game
        """
        self.screen.blit(self.bg, (0, 0))
        self.vauses.draw(self.screen)
        self.balls.draw(self.screen)
        self.bricks.draw(self.screen)
        if self.start == False:
            self.instructions()
        self.show_score()
        self.show_lives()
        self.show_level()
        self.keybinds()
        pygame.display.flip()
