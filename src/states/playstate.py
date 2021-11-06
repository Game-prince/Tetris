import pygame
from src.states.base import Base

class Play(Base):

    def __init__(self) -> None:
        super().__init__()

    def render(self) -> None:
        pass

    def update(self, params) -> None:
        pass

    def enter(self, **param) -> None:
        pass

    def leave(self) -> None:
        pass