#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Import and initialize the pygame library
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
pygame.font.init()


# Set up the drawing window
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Blue Circle')
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# Run until the user asks to quit
running = True
ctr = 0
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, BLUE, (250, 250), 75)
    myText = str(ctr)
    ctr += 1
    text_surface = my_font.render(myText, False, GREEN)

    screen.blit(text_surface, (200,350))
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
