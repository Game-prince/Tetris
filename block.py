import pygame
from pygame.color import THECOLORS

class Block:
    """
    This is a block class. 
    It is the building block of our game
    """

    def __init__(self) -> None:
        """ constructor function """

        self.surf = pygame.Surface([50,50])
        self.rect = self.surf.get_rect()
        self.border_radius = 15

    def render(self, screen=None) -> None:
        """ Renders the blocks. Takes screen as the argument """
        pygame.draw.rect(self.surf, THECOLORS['white'], (0, 0, 50, 50), border_radius=self.border_radius)
        screen.blit(self.surf, self.rect)