import pygame
import sys

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((600, 400))

# Set the title of the window
pygame.display.set_caption('Snake Game by tsjdev-apps')

# Snake properties
snake_pos = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50]]  # List of segments' positions
snake_size = (10, 10)  # Width and height of each snake segment
snake_speed = 10  # How many pixels the snake moves per frame
direction = "RIGHT"  # Initial direction of the snake

# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a] and direction != "RIGHT":
                direction = "LEFT"
            elif event.key in [pygame.K_RIGHT, pygame.K_d] and direction != "LEFT":
                direction = "RIGHT"
            elif event.key in [pygame.K_UP, pygame.K_w] and direction != "DOWN":
                direction = "UP"
            elif event.key in [pygame.K_DOWN, pygame.K_s] and direction != "UP":
                direction = "DOWN"

    # Fill the background with light green color
    screen.fill((144, 238, 144))

    # Game logic (e.g., move the snake)
    # Calculate new head position
    if direction == "LEFT":
        new_head = [snake_pos[0][0] - snake_speed, snake_pos[0][1]]
    elif direction == "RIGHT":
        new_head = [snake_pos[0][0] + snake_speed, snake_pos[0][1]]
    elif direction == "UP":
        new_head = [snake_pos[0][0], snake_pos[0][1] - snake_speed]
    elif direction == "DOWN":
        new_head = [snake_pos[0][0], snake_pos[0][1] + snake_speed]

    # Insert new head and remove last segment to simulate movement
    snake_pos.insert(0, new_head)
    snake_pos.pop()

    # Drawing code (draw the snake, food, etc.)
    for pos in snake_pos:
        pygame.draw.rect(screen, (0, 0, 0), [pos[0], pos[1], snake_size[0], snake_size[1]])

    # Update screen
    pygame.display.flip()

    #Frame rate
    pygame.time.Clock().tick(10)