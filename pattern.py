import pygame
from block import Block
from random import randint

class Pattern:
    """Pattern class"""

    def __init__(self) -> None:
        
        self.max_blocks = 5

        self.current = randint(1, self.max_blocks)
        self.p_arr = []

        while self.current:
            self.current -= 1
            block = Block()

            if (len(self.p_arr) == 0) :
                self.p_arr.append(block)
                continue
        
            side = randint(1, 4)
            prev = self.p_arr[-1]
            x = prev.rect.x
            y = prev.rect.y
            if side == 1:
                y -= prev.rect.height
            if side == 2:
                x += prev.rect.width
            if side == 3:
                y += prev.rect.height
            if side == 4:
                x -= prev.rect.width
            
            block.rect.x = x
            block.rect.y = y

            self.p_arr.append(block)
        
    def render(self, screen=None):

        top = max(self.p_arr, key= lambda a : a.rect.y)
        bottom = min(self.p_arr, key= lambda a : a.rect.y)
        right = max(self.p_arr, key= lambda a : a.rect.x)
        left = min(self.p_arr, key= lambda a : a.rect.x)

        min_block = None
        for block in self.p_arr:
            # if block.rect.x == left and block.rect.y == 
            pass