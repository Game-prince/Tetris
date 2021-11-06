import pygame
from src.functions import Write
from src.states.base import Base

class Start(Base):

    def __init__(self) -> None:
        super().__init__()

    def render(self) -> None:
        
        Write("Tetris", self.screen_width // 2, self.screen_height // 2 - 100, (255, 255, 255), 72, self.screen)

    def update(self, params) -> None:
        pass

    def enter(self, **param) -> None:
        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']