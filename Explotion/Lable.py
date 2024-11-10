import pygame

class Lable():
    def __init__(self, xpos: int, ypos: int, size: int, color: tuple[int, int, int], surface, text: str):
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.surface = surface
        self.text = text
        self.color = color
        self.fontObject = pygame.font.Font(None, self.size)
        self.object = None


    def draw(self):
        self.object = self.fontObject.render(self.text, True, self.color)
        self.fontObject.render(self.text, True, self.color)
        self.surface.blit(self.object, (self.xpos, self.ypos))

    def newText(self, newText):
        self.text = newText