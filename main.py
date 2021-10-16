import pygame
from pygame.constants import KEYDOWN, QUIT
from pygame.color import THECOLORS

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
    """ This will define every block of the game """

    def __init__(self, row, col) -> None:
        
        # giving row and column to the block
        self.row = row
        self.col = col

        # Dimension
        self.size = 40

        # some extra properties
        self.color = THECOLORS['white']

def find_block(row, col, blocks):

    for bls in blocks:
        for bl in bls:
            if bl.row == row and bl.col == col:
                return bl
    return None


# game loop
while not GAME_OVER:

    #event handling for our game
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_OVER = True

    # filling the screen with black color
    SCREEN.fill(THECOLORS["black"])

    if GAME_STATE == 'play':
        
        All_blocks = []

        cols = WINDOW_HEIGHT // 40
        rows = WINDOW_WIDTH // 40

        for row in range(rows):
            temp = []
            for col in range(cols):
                block = Block(row, col)
                temp.append(block)
            All_blocks.append(temp)
        
        for blocks in All_blocks:
            for block in blocks:
                pygame.draw.rect(SCREEN, block.color, [block.row*40, block.col*40, 40, 40], 2)

    #u pdating the screen
    pygame.display.flip()

    # running the game at 60 fps
    clock.tick(60)