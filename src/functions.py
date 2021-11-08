import pygame
from pygame.color import THECOLORS
from random import randint

from src.objects import BLOCK

def Write(text, x, y, color, size, screen, center=True):
    font = pygame.font.SysFont("Comis sans MS", size)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)


# making a function for transitioning animations
def transition(initial, final, time):
    """ This is a function will help in transitioning animations """

    # initializing the variables
    current = initial
    change = final - initial
    step = change / time

    # making the loop
    for i in range(time-1):
        current += step
        yield current
    
    yield final

def make_pattern(count : int, size:int) -> list:
    """ This function will tell the position of different blocks in the block group """

    patterns = [(200,-80)]
    for i in range(count-1):
        block = patterns[-1]

        while block in patterns:
            curr = randint(1, 4)
            if curr == 1:
                block = (block[0], block[1] -size)
            elif curr == 2:
                block = (block[0] + size, block[1])
            elif curr == 3:
                block == (block[0], block[1] + size)
            elif curr == 4:
                block = (block[0] - size, block[1])
        
        patterns.append(block)

    return patterns

def random_color():
    """ This function will return a random color """
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def make_block(pos, color) -> BLOCK:
    block = BLOCK.copy()
    block['x'] = pos[0]
    block['y'] = pos[1]
    block['color'] = color

    return block