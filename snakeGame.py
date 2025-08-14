import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set the window dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
TILE_SIZE = 100

# Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Snake")


# 2D array for game board
gameBoard = [[0 for row in range(10)] for col in range(10)]

# Center of the array
startPosition = gameBoard[5][5]

# Find a random position for food
def getRandomPosition(gameBoard):
    row = random.randint(0, len(gameBoard) - 1)
    col = random.randint(0, len(gameBoard[0]) - 1)
    return row, col

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(10):
        for col in range(10):
            if gameBoard[row][col] == 2:  # Food is marked as '2'
                pygame.draw.rect(screen, (255, 0, 0), 
                                 pygame.Rect(col *  TILE_SIZE, row *  TILE_SIZE,  TILE_SIZE,  TILE_SIZE))
                
    # Update the display
    pygame.display.flip()

pygame.quit()
