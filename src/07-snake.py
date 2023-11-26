import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((600, 400))

# Set the title of the window
pygame.display.set_caption('Snake Game by tsjdev-apps')

# Indication for Game Over
game_over = False

# Initialize the score
score = 0

# Create a font object
font = pygame.font.SysFont(None, 35)

# Snake properties
snake_pos = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50]]  # List of segments' positions
snake_size = (10, 10)  # Width and height of each snake segment
snake_speed = 10  # How many pixels the snake moves per frame
direction = "RIGHT"  # Initial direction of the snake

food_pos = [random.randrange(1, 60) * 10, random.randrange(1, 40) * 10]
food_size = (10, 10)
food_color = (255, 0, 0)  # Red color

# Function to reset the game
def reset_game():
    global snake_pos, direction
    snake_pos = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50]]
    direction = "RIGHT"

# Game loop
while True:
    if not game_over:

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

        # Collision detection
        head_pos = snake_pos[0]
        if head_pos in snake_pos[1:] or head_pos[0] < 0 or head_pos[0] > 600 - snake_size[0] or head_pos[1] < 0 or head_pos[1] > 400 - snake_size[1]:
            game_over = True

        # Detect collision with food
        if head_pos == food_pos:
            # Increase the length of the snake
            snake_pos.append(snake_pos[-1])

            # Generate new food position
            food_pos = [random.randrange(1, 60) * 10, random.randrange(1, 40) * 10]

            # Update the score
            score += 10

        # Drawing code (draw the snake, food, etc.)
        for pos in snake_pos:
            pygame.draw.rect(screen, (0, 0, 0), [pos[0], pos[1], snake_size[0], snake_size[1]])

        # Draw food
        pygame.draw.rect(screen, food_color, [food_pos[0], food_pos[1], food_size[0], food_size[1]])

        # Render the score text
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Update screen
        pygame.display.flip()

        #Frame rate
        pygame.time.Clock().tick(10)

    elif game_over:
        # Display game over message
        game_over_text = font.render('Game Over! Press any key to restart', True, (0, 0, 0))
        screen.blit(game_over_text, (100, 200))
        pygame.display.flip()

        # Wait for key press to restart
        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    waiting_for_key = False
                    game_over = False
                    reset_game()
                    score = 0