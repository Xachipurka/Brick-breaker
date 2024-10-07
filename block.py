import pygame

class Block:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.rx = 40
        self.ry = 40

    def draw(self, screen):
        pygame.draw.rect(screen, (225, 200, 0), (self.x, self.y, self.rx, self.ry))
