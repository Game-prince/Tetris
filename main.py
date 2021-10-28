# Making a tetrix game using pygame
from random import randint
import pygame
from pygame.color import THECOLORS
from pattern import make_pattern

pygame.init()

WIDTH = 400
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

# Properties of the block
Block_size = 40

# Number of rows and columns
ROWS = HEIGHT // Block_size
COLUMNS = WIDTH // Block_size

BLOCK = {
    'id' : 0,
    'size' : Block_size,
    'color' : THECOLORS["black"],
    'background' : THECOLORS['black'],
    'border' : False,
    'x' : 0,
    'y' : 0 
}

# function to display the object on screen
def render(object, screen=SCREEN) -> None:

    width = height = object['size']

    surf = pygame.Surface([width, height])
    rect = surf.get_rect()
    rect.x = object['x']
    rect.y = object['y']

    surf.fill(object['background'])
    pygame.draw.rect(surf, object['color'], [0, 0, width, height], border_radius= 5 if object['border'] else 0)

    screen.blit(surf, rect)

# for moving the blocks
def move(object, screen=SCREEN) -> None:

    object['y'] += COLUMNS

# Game State
GAMESTATE = "play"

# play state constants
MakePattern = True
Current_pattern = []
All_Pattern = []


while True:

    events = pygame.event.get();
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    SCREEN.fill(THECOLORS['black'])

    # Renderin the game according to differnt gamestate
    if GAMESTATE == 'play':
        
        block_arr = []
        for row in range(ROWS):
            for col in range(COLUMNS):
                block = BLOCK.copy()
                block['id'] = row*COLUMNS + col
                block['x'] = col*Block_size
                block['y'] = row*Block_size
                block_arr.append(block)
        
        if MakePattern:
            pattern = make_pattern(randint(1, 5))

            min_height = min(pattern)
            
            Current_pattern = pattern
            MakePattern = False
        
        for block in block_arr:
            if Current_pattern.__contains__(block['id']):
                block['color'] = THECOLORS['green']
                block['border'] = True
            for patterns in All_Pattern:
                if patterns.__contains__(block['id']):
                    block['color'] = THECOLORS['green']
                    block['border'] = True
            render(block)

        for i in range(len(Current_pattern)):
            Current_pattern[i] += COLUMNS
            if Current_pattern[i] > COLUMNS*(ROWS-1): 
                MakePattern = True
                All_Pattern.append(Current_pattern)
        

    pygame.display.flip()

    clock.tick(2)
