import pygame
from src.functions import Write
from src.states.base import Base

class Play(Base):

    def __init__(self) -> None:
        super().__init__()

    def render(self) -> None:
        
        Write("Playstate", 50, 50, (255, 255, 255), 24, self.screen)

    def update(self, params) -> None:
        
        self.render()

    def enter(self, **param) -> None:
        self.screen = param['screen']