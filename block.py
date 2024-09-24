import pygame

class Block:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.rx = 10
        self.ry = 10

    def draw(self, screen):
        pygame.draw.rect(screen, (225, 200, 0), (self.x, self.y, self.rx, self.ry))
