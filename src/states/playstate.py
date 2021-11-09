from random import randint
import pygame
from pygame.color import THECOLORS
from pygame.constants import K_LEFT, K_RIGHT, KEYDOWN
from src.functions import Write, big_small, closest, colliding, is_block_there, make_block, make_pattern, random_color, row_full, transition
from src.states.base import Base

class Play(Base):

    def __init__(self) -> None:
        super().__init__()

        # if the game is started
        self.just_started = True

        # current level
        self.level = 1

        # score
        self.score = 0

        # current pattern
        self.current_pattern = make_pattern(randint(1, 5), 40)
        self.moving_blocks = []
        self.current_block_color = random_color()
        self.ismoving = True

        for pattern in self.current_pattern:
            block = make_block(pattern, self.current_block_color)
            self.moving_blocks.append(block)

        
        # all blocks
        self.all_blocks = []

    def render(self) -> None:
        
        if self.just_started :
            Write("Level 1", self.levelDisplayer_rect.width // 2, self.levelDisplayer_rect.height // 2, THECOLORS['white'], 48,  self.levelDisplayer)
            self.screen.blit(self.levelDisplayer, self.levelDisplayer_rect)

        else:
            # renderng current blocks
            for block in self.moving_blocks:
                pygame.draw.rect(self.screen, self.current_block_color, (block['x'], block['y'], block['width'], block['height']), border_radius=block['radius'])

            # rendering the landed blocks
            for block in self.all_blocks:
                pygame.draw.rect(self.screen, block['color'], (block['x'], block['y'], block['width'], block['height']), border_radius=block['radius'])

            # rendering score
            Write(f"Score : {self.score}", 10, 5, THECOLORS['goldenrod'], 24, self.screen, False)


    def update(self, params) -> None:

        # event handling
        for event in params:
            if event.type == KEYDOWN:
                lst = big_small(self.moving_blocks)
                if event.key == K_LEFT:
                    if lst[0] > 0:
                        for block in self.moving_blocks:
                            if not is_block_there(block['x'] - block['width'], block['y'], self.all_blocks):
                                block['x'] -= block['width']
                if event.key == K_RIGHT:
                    if lst[2] < self.screen_width - 40:
                        for block in self.moving_blocks:
                            if not is_block_there(block['x'] - block['width'], block['y'], self.all_blocks):
                                block['x'] += block['width']

        # game started animation
        if self.just_started:
            try:
                self.levelDisplayer_rect.y = next(self.cordy)
            except StopIteration:
                if self.levelDisplayer_rect.y == self.screen_height // 2- 50:
                    pygame.time.delay(1000)
                    self.cordy = transition(self.levelDisplayer_rect.y, self.screen_height + 50, 30)
                else:
                    self.just_started = False
        
        else:

            # checking if the block should be moved
            for block in self.moving_blocks:
                if block['y'] + block['speed'] + block['height'] >= self.screen_height:
                    self.ismoving = False
                    break

            if not self.ismoving:

                for bl in self.moving_blocks:
                    bl['y'] = closest(bl['width'], bl['y'])
                    self.all_blocks.append(bl)

                self.current_pattern = make_pattern(randint(1, 5), 40)
                self.moving_blocks = []
                self.current_block_color = random_color()

                for pattern in self.current_pattern:
                    block = make_block(pattern, self.current_block_color)
                    self.moving_blocks.append(block)
                
                self.all_blocks = sorted(self.all_blocks, key=lambda x: x['y'])
                self.ismoving = True
                    

            for block in self.moving_blocks:
                block['y'] += block['speed']

            # collision between moving blocks and already landed blocks
            if colliding(self.all_blocks, self.moving_blocks):
                self.ismoving = False

            # checking if any row is full
            curr = row_full(self.all_blocks)
            if curr != False:
                self.all_blocks = list(filter(lambda x : x['y'] != curr, self.all_blocks))
                self.score += 150

                for block in self.all_blocks:
                    if block['y'] < curr:
                        block['y'] += block['height']

        # checking if the game is over
        for blocks in self.all_blocks:
            if blocks['y'] == 0:
                self.gstatemachine.change('gameover', screen=self.screen, gstatemachine=self.gstatemachine, score=self.score)

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
        
        self.cordy = transition(-100, self.screen_height // 2- 50, 30)