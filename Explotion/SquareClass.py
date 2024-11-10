import pygame
import time

red = (230,71,71)
orange = (244,128,32)
yellow = (230,226,46)
green = (143,185,53)
blue = (80,121,191)
blowUpColors = [red, orange, yellow]

def isInInterval(number, lower, upperRelative):
    upper = lower + upperRelative
    return lower <= number <= upper

class Square:
    def __init__(self, xpos, ypos, size, color):
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.color = color
        self.blowUpColors = blowUpColors[:]
        self.isBlownUp = False
        self.blowUpInProgress = False
        self.blowUpStart = None
        self.blowUpTimer = None
        self.isDefussed = False


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.xpos, self.ypos, self.size, self.size))

        #Uppdatera färg under expoltion
        if self.blowUpInProgress:
            if self.blowUpTimer <= pygame.time.get_ticks() - self.blowUpStart:
                if len(self.blowUpColors) != 0:
                    self.color = self.blowUpColors.pop()
                    self.blowUpStart = pygame.time.get_ticks()
                else:
                    self.isBlownUp = True


    def blowUp(self):
        self.blowUpInProgress = True
        self.blowUpStart = pygame.time.get_ticks()
        self.color = self.blowUpColors.pop()


    def defussed(self, score):
        if self.blowUpInProgress:
            self.blowUpInProgress = False
            self.color = green
            self.isDefussed = True
            return score + 10
        else:
            return score

    def isClicked(self, mousePos):
        mouseXpos, mouseYpos = mousePos

        if isInInterval(mouseXpos, self.xpos, self.size): 
            if isInInterval(mouseYpos, self.ypos, self.size):
                return True
        else: 
            return False
    
    def reset(self):
        self.isDefussed = False
        self.color = blue
        self.blowUpColors = blowUpColors[:]

    