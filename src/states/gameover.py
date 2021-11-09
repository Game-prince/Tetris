import pygame
from pygame.color import THECOLORS

from src.functions import Write, transition
from src.states.base import Base

class Over(Base):

    def __init__(self):
        super().__init__()

        self.justentered = True
        self.background_color = transition(0, 255, 30)
        

    def enter(self, **param):
        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']
        self.score = param['score']

    def render(self):

        if not self.justentered:
            Write("Game Over", self.screen_width // 2, self.screen_height // 2, THECOLORS['darkred'], 80, self.screen)
            Write(f"score :{self.score}", self.screen_width // 2, self.screen_height // 2 + 100, THECOLORS['goldenrod'], 32, self.screen)

    def update(self, param):
        
        if self.justentered:
            try:
                color = next(self.background_color)
                self.screen.fill((color, color, color))
            except StopIteration:
                self.justentered = False

        
        self.render()
    
