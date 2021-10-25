import pygame
from pygame import scrap
from pygame.constants import KEYDOWN, QUIT
from pygame.color import THECOLORS
from pattern import make_pattern
from random import randint

pygame.init()

# width and height of the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

# setting up display
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Constant which checks if the game is over or not
GAME_OVER = False
# constant to keep the current game state
GAME_STATE = "play"

# setting up clock
clock = pygame.time.Clock()

# block class
class Block:

    def __init__(self, row, col, color):

        self.x = col * 40
        self.y = row * 40

        self.surf = pygame.Surface([40, 40])
        self.rect = pygame.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.color = color
        
        self.surf.fill(self.color)

    def render(self):
        
        SCREEN.blit(self.surf, self.rect)

All_blocks = []

# game loop
while not GAME_OVER:

    #event handling for our game
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_OVER = True

    # filling the screen with black color
    SCREEN.fill(THECOLORS["black"])

    if GAME_STATE == 'play':
        
        curr_arr = make_pattern(randint(1, 5))
        curr_blocks = []

        color = randint(0, len(THECOLORS)-1)
        block_color = (123, 123, 123)
        for key in THECOLORS:
            color -= 1
            if (color == 0):
                block_color = THECOLORS[key]

        for e in curr_arr:
            curr_blocks.append(Block(e//10, e%10, block_color))

        cols = WINDOW_HEIGHT // 40
        rows = WINDOW_WIDTH // 40
        
        for blocks in All_blocks:
            for block in blocks:
                pygame.draw.rect(SCREEN, block.color, [block.row*40, block.col*40, 40, 40], 2)

    #u pdating the screen
    pygame.display.flip()

    # running the game at 60 fps
    clock.tick(60)