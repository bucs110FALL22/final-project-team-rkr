LEVELS = [
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


class Board:
    def __init__(self):
        """
        Creates the GUI class which draws everything
        """
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.bg = pygame.image.load("assets/background.png")
        self.font = pygame.font.SysFont(None, 48)
        self.big_font = pygame.font.SysFont(None, 96)
        self.small_font = pygame.font.SysFont(None, 36)

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