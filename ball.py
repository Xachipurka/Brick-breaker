import time

import pygame


class Ball:
    def __init__(self):
        self.y = 300
        self.x = 400
        self.r = 10
        self.sy = -200
        self.sx = -200
        self.last_update = time.perf_counter()

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 90, 25), (self.x, self.y), self.r, 0)

    def update(self, rect_x, rect_y, rect_width, rect_height, blocks):
        self.y += self.sy * (time.perf_counter() - self.last_update)
        self.x += self.sx * (time.perf_counter() - self.last_update)
        self.last_update = time.perf_counter()
        if self.y <= self.r // 2:
            self.sy = -self.sy
        elif self.x >= 800 - self.r // 2 or self.x <= self.r // 2:
            self.sx = -self.sx
        self.bounce(pygame.Rect(rect_x, rect_y, rect_width, rect_height))

        for i in range(len(blocks) - 1, -1, -1):
            if self.circle_intersects_rectangle(blocks[i].x, blocks[i].y, blocks[i].rx, blocks[i].ry):
                self.bounce(pygame.Rect(blocks[i].x, blocks[i].y, blocks[i].rx, blocks[i].ry))

                del blocks[i]

    def bounce(self, rect):
          closest_x = max(rect.left, min(self.x, rect.right))
          closest_y = max(rect.top, min(self.y, rect.bottom))

          # Вектор от ближайшей точки до центра круга
          distance = pygame.math.Vector2(self.x - closest_x, self.y - closest_y)

          if distance.length_squared() < self.r ** 2:
              # Нормализуем вектор столкновения
              if distance.length() != 0:
                  collision_normal = distance.normalize()
              else:
                  # Если центр круга совпадает с ближайшей точкой, определим нормаль произвольно
                  collision_normal = pygame.math.Vector2(1, 0)

              # Отражаем скорость круга относительно нормали столкновения
              circle_vel = pygame.Vector2(self.sx, self.sy)
              circle_vel = circle_vel.reflect(collision_normal)
              self.sx, self.sy = circle_vel.x, circle_vel.y

              # Перемещаем круг вне прямоугольника, чтобы избежать застревания
              overlap = self.r - distance.length()
              self.x += (collision_normal * overlap).x
              self.y += (collision_normal * overlap).y

    def circle_intersects_rectangle(self, rect_x, rect_y, rect_width, rect_height):
        # Находим ближайшую точку к центру круга на прямоугольнике
        nearest_x = max(rect_x, min(self.x, rect_x + rect_width))
        nearest_y = max(rect_y, min(self.y, rect_y + rect_height))

        # Вычисляем расстояние от центра круга до ближайшей точки прямоугольника
        distance_x = self.x - nearest_x
        distance_y = self.y - nearest_y

        # Проверяем, пересекается ли круг с прямоугольником
        return (distance_x ** 2 + distance_y ** 2) <= (self.r ** 2)