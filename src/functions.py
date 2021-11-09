import pygame
from pygame.color import THECOLORS
from random import randint

from src.objects import BLOCK

def Write(text, x, y, color, size, screen, center=True):
    font = pygame.font.SysFont("Comis sans MS", size)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    if center:text_rect.center = (x, y)
    else:
        text_rect.x = x
        text_rect.y = y
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
    color = (randint(0, 255), randint(0, 255), randint(0, 255))

    while color == (0, 0, 0):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))

    return color

def make_block(pos, color) -> BLOCK:
    block = BLOCK.copy()
    block['x'] = pos[0]
    block['y'] = pos[1]
    block['color'] = color

    return block

def closest(a:int, b:int) ->int:
    """ Return an integer which is closes to b and divisible by a """

    b = round(b/a) * a

    return b

def big_small(blocks) -> list:
    """ 
    Return a list of minimum and maximum cordinates in the blocks.
    Return Order:
        [min_x, min_y, max_x, max_y]
    """

    lst = [blocks[0]['x'], blocks[0]['y'], blocks[0]['x'], blocks[0]['y']]

    for block in blocks:
        if block['x'] < lst[0]:
            lst[0] = block['x']
        if block['y'] < lst[1]:
            lst[1] = block['y']
        if block['x'] > lst[2]:
            lst[2] = block['x']
        if block['y'] > lst[3]:
            lst[3] = block['y']
    return lst


def colliding(all_blocks, current_blocks):
    """ This function will check if the moving blocks are colliding with the current blocks """

    def block_collision(block1, block2):
        """ This function will check if two blocks are colliding """

        if block1['x'] == block2['x'] and block1['y'] + block1['height'] >= block2['y'] and block1['y'] + block1['height'] <= block2['y']:
            return True
        else:
            return False
    
    for block in current_blocks:
        for other in all_blocks:
            if block_collision(block, other):
                return True
    return False

def row_full(all_blocks) -> bool :
    """ checking if all the blocks int any row are full or not """
    if len(all_blocks) == 0:
        return False

    curr = all_blocks[0]['y']
    count = 0

    for block in all_blocks:
        if block['y'] == curr:
            count += 1

        else:
            if (count == 10): return curr
            count = 1
            curr = block['y']
    
    if count == 10:
        return curr

    return False

def is_block_there(x:int, y:int, all_blocks) -> bool:
    """ Checks if the block is present there or not in landed blocks """

    if len(all_blocks) == 0:
        return False

    for block in all_blocks:
        if block['x'] == x and block['y'] == 'y':
            return True
    
    return False

def rotate_blocks(blocks:list):
    """ This function will rotate the current moving blocks for better positioning. """

    pass