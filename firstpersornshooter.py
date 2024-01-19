import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
BULLET_SPEED = 7
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic FPS Game")

# Load player image
player_image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(player_image, RED, (int(PLAYER_SIZE/2), int(PLAYER_SIZE/2)), int(PLAYER_SIZE/2))

# Set player initial position
player_pos = [WIDTH // 2, HEIGHT // 2]

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
bullets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_w]:
        player_pos[1] -= PLAYER_SPEED
    if keys[pygame.K_s]:
        player_pos[1] += PLAYER_SPEED
    if keys[pygame.K_a]:
        player_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_d]:
        player_pos[0] += PLAYER_SPEED

    # Bullet creation
    if keys[pygame.K_SPACE]:
        bullets.append([player_pos[0] + PLAYER_SIZE/2, player_pos[1] + PLAYER_SIZE/2])

    # Update bullets
    for bullet in bullets:
        angle = math.atan2(player_pos[1] + PLAYER_SIZE/2 - bullet[1], player_pos[0] + PLAYER_SIZE/2 - bullet[0])
        bullet[0] += BULLET_SPEED * math.cos(angle)
        bullet[1] += BULLET_SPEED * math.sin(angle)

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    for bullet in bullets:
        pygame.draw.circle(screen, RED, (int(bullet[0]), int(bullet[1])), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
