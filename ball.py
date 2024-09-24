import pygame
from block import Block

#from block import *
#from block import Block as B

class Ball:
    def __init__(self):
        self.y = 300
        self.x = 400
        self.r = 10
        self.sy = -2.
        self.sx = -2
    def draw(self, screen):
        pygame.draw.circle(screen, (200, 90, 25), (self.x, self.y), self.r, 0)

    def update(self, rect_x, rect_y, rect_width, rect_height, blocks):
        self.y += self.sy
        self.x += self.sx
        if self.y <= self.r // 2:
            self.sy = -self.sy
        elif self.x >= 800 - self.r // 2 or self.x <= self.r // 2:
            self.sx = -self.sx
        elif self.circle_intersects_rectangle(rect_x, rect_y, rect_width, rect_height):
            self.y -= self.sy
            self.sy = -self.sy
            self.y += self.sy
        for i in range(len(blocks) - 1, -1, -1):
            if self.circle_intersects_rectangle(blocks[i].x, blocks[i].y, blocks[i].rx, blocks[i].ry):
                self.y -= self.sy
                self.sy = -self.sy
                del blocks[i]
                self.y += self.sy

    def circle_intersects_rectangle(self, rect_x, rect_y, rect_width, rect_height):
        # Находим ближайшую точку к центру круга на прямоугольнике
        nearest_x = max(rect_x, min(self.x, rect_x + rect_width))
        nearest_y = max(rect_y, min(self.y, rect_y + rect_height))

        # Вычисляем расстояние от центра круга до ближайшей точки прямоугольника
        distance_x = self.x - nearest_x
        distance_y = self.y - nearest_y

        # Проверяем, пересекается ли круг с прямоугольником
        return (distance_x ** 2 + distance_y ** 2) <= (self.r ** 2)