import pygame
from pygame.color import THECOLORS

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