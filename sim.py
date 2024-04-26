import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Bouncing Ball Simulation')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock to control the frame rate
clock = pygame.time.Clock()


ball_pos = [400, 300]
ball_radius = 15
ball_speed_y = 0
gravity = 0.5
bounce_factor = -0.7  # Negative value for bounce back

# Define the rings positions and colors
rings = [(200, WHITE), (300, WHITE), (400, WHITE), (500, WHITE)]


bounce_sound = pygame.mixer.Sound('sounds/stone-dropping.mp3')


running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the ball
    ball_speed_y += gravity
    ball_pos[1] += ball_speed_y

    # Bounce off the rings
    for ring_y, _ in rings:
        if ball_pos[1] + ball_radius > ring_y > ball_pos[1] - ball_radius:
            ball_speed_y *= bounce_factor
            bounce_sound.play()  # Play the bounce sound

    # Draw everything
    screen.fill(BLACK)
    for ring_y, color in rings:
        pygame.draw.line(screen, color, (0, ring_y), (800, ring_y), 2)
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()


