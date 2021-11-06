import pygame
from pygame.color import THECOLORS

pygame.init()

# screen properties
screen_width = 400
screen_height = 600

# Making the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# clock 
clock = pygame.time.Clock()

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
            
    pygame.display.flip()
    clock.tick(60)
            
pygame.quit()
quit()