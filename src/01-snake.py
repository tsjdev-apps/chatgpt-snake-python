import pygame
import sys

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((600, 400))

# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Game logic (e.g., move the snake)

    # Drawing code (draw the snake, food, etc.)

    # Update screen
    pygame.display.flip()

    #Frame rate
    pygame.time.Clock().tick(10)