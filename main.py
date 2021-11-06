import pygame
from pygame.color import THECOLORS
from src.statemachine import Statemachine
from src.states.playstate import Play

from src.states.startstate import Start

pygame.init()

# screen properties
screen_width = 400
screen_height = 600

# Making the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# clock 
clock = pygame.time.Clock()

# states
states = {
    "start" : Start(),
    "play" : Play()
}

gstatemachine = Statemachine(states)
gstatemachine.change("start", screen=screen, gstatemachine=gstatemachine)
gstatemachine.render()

# custom events
current_event = 1
move = pygame.USEREVENT + current_event
current_event += 1

pygame.time.set_timer(move, 200)

# Main loop
running = True
while running:
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill(THECOLORS["black"])
    gstatemachine.update(events)
    pygame.display.flip()
    clock.tick(60)
            
pygame.quit()
quit()