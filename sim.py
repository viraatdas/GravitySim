import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 600)
screen_center = (window_size[0] // 2, window_size[1] // 2)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Bouncing Ball Simulation')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Initialize the ball at the center
ball_pos = list(screen_center)
ball_radius = 15
ball_speed_y = -5  # Start with an upward speed
gravity = 0.3
bounce_factor = -0.7  # Negative value for bounce back

# Define the rings as concentric circles with their positions (radii), colors, and associated chords
rings = [
    (50, WHITE, "F_C"),
    (100, RED, "F_Db"),
    (150, GREEN, "Eb_C"),
    (200, BLUE, "Eb_Bb"),
]

# Load the sound files for each chord
chords = {
    "F_C": pygame.mixer.Sound('sounds/F_3rd.mp3'),
    "F_Db": pygame.mixer.Sound('sounds/Db_3rd.mp3'),
    "Eb_C": pygame.mixer.Sound('sounds/Eb_3rd.mp3'),
    "Eb_Bb": pygame.mixer.Sound('sounds/Bb_3rd.mp3'),
}

# The main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the ball
    ball_speed_y += gravity
    ball_pos[1] += ball_speed_y

    # Check for collisions with the rings
    for ring_radius, color, chord in rings:
        distance_from_center = abs(screen_center[1] - ball_pos[1])
        if distance_from_center + ball_radius >= ring_radius >= distance_from_center - ball_radius:
            ball_speed_y *= bounce_factor  # Bounce back
            chords[chord].play()  # Play the chord sound
            break  # Exit the loop after playing the sound to prevent multiple sounds from playing

    # Draw everything
    screen.fill(BLACK)
    
    # Draw the rings as concentric circles
    for ring_radius, color, _ in rings:
        pygame.draw.circle(screen, color, screen_center, ring_radius, 2)  # Ring thickness of 2

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
