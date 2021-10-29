from random import randint
import pygame
from pygame import cursors
from pygame.color import THECOLORS
from pattern import make_pattern

pygame.init()

# Game window constants
WIDTH = 400
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# clock to manage time
clock = pygame.time.Clock()

# Properties of the block
Block_size = 40

# Number of rows and columns
ROWS = HEIGHT // Block_size
COLUMNS = WIDTH // Block_size

# Block dictioinary which defines the properties of the block
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

    # extracting with and height of the object
    width = height = object['size']

    # Making a surface to render on screen
    surf = pygame.Surface([width, height])
    rect = surf.get_rect()
    rect.x = object['x']
    rect.y = object['y']

    surf.fill(object['background'])
    pygame.draw.rect(surf, object['color'], [0, 0, width, height], border_radius= 5 if object['border'] else 0)

    # rendering the surface on screen
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
Time_passed = 0

while True:

    # Handling the input events
    events = pygame.event.get();
    for event in events:

        # if user clickes on the red cross sign on the top-right corner
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        # if any key is pressed
        if event.type == pygame.KEYDOWN:

            # input handling for playstate
            if GAMESTATE == "play":

                # moving the pattern block if left or right key is pressed
                for patterns in All_Pattern:
                    for i in range(len(Current_pattern)):
                        if pattern.__contains__(Current_pattern[i]):
                            print("Already a block there")
                if event.key == pygame.K_LEFT:
                    if min(Current_pattern) % COLUMNS > 0:
                        for i in range(len(Current_pattern)):
                            Current_pattern[i] -= 1

                if event.key == pygame.K_RIGHT:
                    if max(Current_pattern) % COLUMNS < COLUMNS - 1:
                        for i in range(len(Current_pattern)):
                            Current_pattern[i] += 1
    
    # painting the screen with black color
    SCREEN.fill(THECOLORS['black'])

    # Renderin the game according to differnt gamestate
    if GAMESTATE == 'play':
        
        # All the blocks in the screen
        block_arr = []
        for row in range(ROWS):
            for col in range(COLUMNS):
                block = BLOCK.copy()
                block['id'] = row*COLUMNS + col
                block['x'] = col*Block_size
                block['y'] = row*Block_size
                block_arr.append(block)
        
        # Making a new pattern appear only if the MakePattern variable is set to True
        if MakePattern:

            # return a array on random length and random variables
            pattern = make_pattern(randint(1, 5))

            # minimun value in the pattern array
            min_height = min(pattern)
            
            # setting the pattern to current pattern
            Current_pattern = pattern

            # changing the MakePattern to False
            MakePattern = False
        
        # Rendering the block
        for block in block_arr:

            # rendering current blocks
            if Current_pattern.__contains__(block['id']):
                block['color'] = THECOLORS['green']
                block['border'] = True
            
            # rendering the landed blocks
            for patterns in All_Pattern:
                if patterns.__contains__(block['id']):
                    block['color'] = THECOLORS['green']
                    block['border'] = True
            render(block)

        # moving the block
        if (Time_passed ==5):
            for i in range(len(Current_pattern)):
                Current_pattern[i] += COLUMNS
                Time_passed = 0
                if Current_pattern[i] > COLUMNS*(ROWS-1): 
                    MakePattern = True
                    All_Pattern.append(Current_pattern)
                for pattern in All_Pattern:
                    if pattern.__contains__(Current_pattern[i] + COLUMNS):
                        MakePattern = True
                        All_Pattern.append(Current_pattern)
                        
        
    Time_passed += 1
    pygame.display.flip()

    clock.tick(10)
