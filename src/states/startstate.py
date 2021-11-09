import pygame
from pygame.color import THECOLORS
from src.functions import Write, transition
from src.states.base import Base

class Start(Base):

    def __init__(self) -> None:
        super().__init__()

        self.animate = False
        self.animation_time = 20
        self.change_background = transition(0, 255, self.animation_time)

    def render(self) -> None:
        
        Write("Tetris", self.screen_width // 2, self.screen_height // 2, THECOLORS["darkgoldenrod"], 100, self.screen)
        Write("Press Enter to play", self.screen_width // 2, self.screen_height // 2 + 100, THECOLORS["skyblue"], 24, self.screen)

    def update(self, params) -> None:

        for event in params:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.animate = True
        
        self.render()
        if self.animate :
            a = next(self.change_background)
            color = (a, a, a)
            self.screen.fill(color)
            self.animation_time -= 1

            if (self.animation_time == 0):
                self.gstatemachine.change("play", screen=self.screen, gstatemachine=self.gstatemachine)    

    def enter(self, **param) -> None:
        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']