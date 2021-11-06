import pygame
from pygame.color import THECOLORS

def Write(text, x, y, color, size, screen, center=True):
    font = pygame.font.SysFont("Comic sans MS", size)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)