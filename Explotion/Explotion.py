import pygame
import random

from SquareClass import Square
from Lable import Lable

def random_exculde(start, end, exclude):
    while True:
        num = random.randint(start, end)
        if num not in exclude:
            return num
        
def newBlowUp(grid, antiGrid):
    blowUpIndex = random_exculde(0, len(grid)-1, antiGrid)
    grid[blowUpIndex].blowUp()
    antiGrid.append(blowUpIndex)

def forAllisDefussed(squareList):
    baseCase = True
    for square in squareList:
        baseCase = square.isDefussed and baseCase
    return baseCase

def forAllisBlownUp(squareList):
    for square in squareList:
        if square.isBlownUp:
            return True      
    return False

def newDificulty(level):
    if level == 1:
        minInterval = 1000
        maxInterval = 2000
        blowUpTimer = 750
    elif level == 2:
        minInterval = 800
        maxInterval = 1500
        blowUpTimer = 600
    elif level == 3:
        minInterval = 700
        maxInterval = 1100
        blowUpTimer = 500
    elif level == 4:
        minInterval = 600
        maxInterval = 900
        blowUpTimer = 400
    else:
        minInterval = 400
        maxInterval = 700
        blowUpTimer = 250
    return minInterval, maxInterval, blowUpTimer


pygame.init()

# Set window dimensions
width, height = 500, 550
window_size = (width, height)

# Create the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Explotion")

# Set background color
background_color = (255, 255, 255)

#varibles
score = 0
level = 1
gridsize = 4


#game objects
scoreLable = Lable(xpos=10, ypos=505, size=70, color=(0, 0, 0), text="Score: " + str(score))
levelLable = Lable(xpos=290, ypos=505, size=70, color=(0, 0, 0), text="Level: " + str(level))

grid = []
for i in range(gridsize):
    for j in range(gridsize):
        grid.append(Square(xpos=(i*50 + 1), ypos=(j*50 + 1), size=48, color=(80,121,191)))

hasBlownUp = []


#random intervall på explosioner
minInterval = 0
maxInterval = 0

for square in grid:
    minInterval, maxInterval, square.blowUpTimer = newDificulty(level=level)

timeSinceLastBlowUp = pygame.time.get_ticks()
nextInterval = random.randint(minInterval, maxInterval)


# Main loop
running = True

while running:
        
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            for square in grid:
                if square.isClicked(pygame.mouse.get_pos()):
                    score = square.defussed(score)
                    scoreLable.newText("Score: " + str(score))
                    

    if len(hasBlownUp) != len(grid):
        if pygame.time.get_ticks() - timeSinceLastBlowUp >= nextInterval:
            newBlowUp(grid, hasBlownUp)
            timeSinceLastBlowUp = pygame.time.get_ticks()
            nextInterval = random.randint(minInterval, maxInterval)

    
    screen.fill(background_color)

    #draw game obj
    for square in grid:
        square.draw(screen)

    scoreLable.draw(screen)
    levelLable.draw(screen)
    
    if forAllisBlownUp(grid):
        running = False

    #when all squares filled
    if forAllisDefussed(grid):
        level += 1
        hasBlownUp = []
        levelLable.newText("Level: " + str(level))
        for square in grid:
            square.reset()
            minInterval, maxInterval, square.blowUpTimer = newDificulty(level=level)

    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()

print("Final Score: " + str(score))