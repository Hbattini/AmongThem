import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
BLOCK_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Block")

# Initialize game variables
block_x = (WIDTH - BLOCK_SIZE) // 2
block_y = (HEIGHT - BLOCK_SIZE) // 2
block_speed = 5

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move the block
    if keys[pygame.K_LEFT] and block_x > 0:
        block_x -= block_speed
    if keys[pygame.K_RIGHT] and block_x < WIDTH - BLOCK_SIZE:
        block_x += block_speed
    if keys[pygame.K_UP] and block_y > 0:
        block_y -= block_speed
    if keys[pygame.K_DOWN] and block_y < HEIGHT - BLOCK_SIZE:
        block_y += block_speed

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
