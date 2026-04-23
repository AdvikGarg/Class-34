import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Game Screen")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font setup
font = pygame.font.SysFont(None, 48)
text = font.render("W Pygame!", True, BLACK)

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Fill background

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))

    # Draw text
    screen.blit(text, (250, 100))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
