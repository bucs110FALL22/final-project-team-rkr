import pygame

DISPLAY_WIDTH = 793
DISPLAY_HEIGHT = 1024


class GUI:
    def __init__(self):
        """
        Creates the GUI class which draws everything
        """
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.bg = pygame.image.load("assets/background.png")
        self.font = pygame.font.SysFont(None, 48)
        self.big_font = pygame.font.SysFont(None, 96)
        self.small_font = pygame.font.SysFont(None, 36)

    def instructions(self):
        """
        Displays instructions on how to start
        """
        start = self.font.render("Left Click to Start", True, "white")
        start_rect = start.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))
        self.screen.blit(start, start_rect)

    def keybinds(self):
        """
        Displays keybinds on the bottom of the screen
        """
        restart = self.small_font.render("Press R to Restart", True, "white")
        restart_rect = restart.get_rect(left=0, bottom=(DISPLAY_HEIGHT))
        self.screen.blit(restart, restart_rect)
        quit = self.small_font.render("Press Q to Quit", True, "white")
        quit_rect = quit.get_rect(right=DISPLAY_WIDTH, bottom=(DISPLAY_HEIGHT))
        self.screen.blit(quit, quit_rect)

    def draw_vauses(self, vaus):
        """
        Draws the vaus(paddle)
        args: vaus
        """
        vaus.draw(self.screen)

    def draw_balls(self, balls):
        """
        Draws the balls
        args: balls
        """
        balls.draw(self.screen)

    def draw_bricks(self, bricks):
        """
        Draws the bricks
        args: bricks
        """
        bricks.draw(self.screen)

    def draw_level(self, level):
        """
        Displays the level
        args: level
        """
        text = self.font.render(f"Level: {level}/4", True, "white")
        self.screen.blit(text, (0, 0))

    def draw_score(self, score):
        """
        Displays the score
        args: score
        """
        text = self.font.render(f"Score: {score}", True, "white")
        text_rect = text.get_rect(center=(DISPLAY_WIDTH // 2, 24))
        self.screen.blit(text, text_rect)

    def draw_lives(self, lives):
        """
        Displays lives left
        args: lives
        """
        text = self.font.render(f"Lives: {lives}", True, "white")
        text_rect = text.get_rect(right=DISPLAY_WIDTH)
        self.screen.blit(text, text_rect)

    def draw_background(self):
        """
        Draws the background
        """
        self.screen.blit(self.bg, (0, 0))

    def win_screen(self, score):
        """
        Displays the winning screen with 'You Win' and your score
        args: score
        """
        self.screen.fill("green")
        text = self.big_font.render("You Win", True, "black")
        text_rect = text.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 - 96))
        self.screen.blit(text, text_rect)
        score = self.font.render(f"Your score was {score}", True, "black")
        score_rect = score.get_rect(
            center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + 48)
        )
        self.screen.blit(score, score_rect)
        self.keybinds()
        pygame.display.flip()

    def lose_screen(self, score, high_score):
        """
        Displays the losing screen with 'You Lose' and your score and the high score
        args: score, high_score
        """
        self.screen.fill("red")
        text = self.big_font.render("Game Over", True, "black")
        text_rect = text.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 - 96))
        self.screen.blit(text, text_rect)
        score = self.font.render(f"Your score was {score}", True, "black")
        score_rect = score.get_rect(
            center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + 48)
        )
        self.screen.blit(score, score_rect)
        high_score = self.font.render(
            f"Your high score was {high_score}", True, "black"
        )
        high_score_rect = high_score.get_rect(
            center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + 96)
        )
        self.screen.blit(high_score, high_score_rect)
        self.keybinds()
        pygame.display.flip()
