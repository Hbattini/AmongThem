import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Table Tennis Game")

# Initialize game variables
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

paddle_left_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle_right_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle_speed = 5

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_right_y > 0:
        paddle_right_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_right_y < HEIGHT - PADDLE_HEIGHT:
        paddle_right_y += paddle_speed

    # Update game elements
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collisions with walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Ball collisions with paddles
    if (
        ball_x <= PADDLE_WIDTH
        and paddle_left_y <= ball_y <= paddle_left_y + PADDLE_HEIGHT
    ) or (
        ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE
        and paddle_right_y <= ball_y <= paddle_right_y + PADDLE_HEIGHT
    ):
        ball_speed_x = -ball_speed_x

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (5, paddle_left_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(
        screen, WHITE, (WIDTH - PADDLE_WIDTH - 5, paddle_right_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    )
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
