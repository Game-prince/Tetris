import pygame
from pygame.constants import KEYDOWN, QUIT
from pygame.color import THECOLORS

from block import Block

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


# game loop
while not GAME_OVER:

    #event handling for our game
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_OVER = True

    # filling the screen with black color
    SCREEN.fill(THECOLORS["black"])

    if GAME_STATE == 'play':
        block = Block()
        block.render(SCREEN)

    #u pdating the screen
    pygame.display.flip()

    # running the game at 60 fps
    clock.tick(60)