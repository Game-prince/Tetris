import pygame
from pygame.color import THECOLORS
from src.functions import Write, transition
from src.states.base import Base

class Play(Base):

    def __init__(self) -> None:
        super().__init__()

        self.just_started = True

    def render(self) -> None:
        
        if not self.just_started : Write("Level 1", self.levelDisplayer_rect.width // 2, self.levelDisplayer_rect.height // 2, (255, 255, 255), 48,  self.levelDisplayer)
        self.screen.blit(self.levelDisplayer, self.levelDisplayer_rect)


    def update(self, params) -> None:

        if self.just_started:
            try:
                self.levelDisplayer_rect.y = next(self.cordy)
                if (self.levelDisplayer_rect.y == self.screen_width // 2 - 50):
                    pygame.time.wait(2)
            except StopIteration:
                self.just_started = False


        self.render()

    def enter(self, **param) -> None:
        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']

        self.levelDisplayer =  pygame.Surface([self.screen_width, 100])
        self.levelDisplayer.fill(THECOLORS['skyblue'])
        self.levelDisplayer_rect  =  self.levelDisplayer.get_rect()
        self.levelDisplayer_rect.x = 0
        self.levelDisplayer_rect.y = -100
        
        self.cordy = transition(-100, self.screen_height + 50, 120)