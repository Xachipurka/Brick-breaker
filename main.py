import pygame
import sys
import random

from ball import Ball
from block import Block

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простое приложение Pygame")

# Цвета
BLACK = (0, 0, 0)
BLUE = (170, 0, 0)

# Параметры квадрата
square_size_x = 50
square_size_y = 10
square_x = WIDTH // 2 - square_size_x // 2
square_y = HEIGHT - 50
square_speed = 5

blocks = [Block(50 * i, 100) for i in range(20)]
ball = Ball()

gameOver = False


while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed

    # Ограничение движения квадрата в пределах окна
    square_x = max(0, min(WIDTH - square_size_x, square_x))

    # Заполнение фона черным цветом
    screen.fill(BLACK)

    ball.update(square_x, square_y, square_size_x, square_size_y, blocks)
    ball.draw(screen)

    if ball.y >= HEIGHT:
        gameOver = True

    # Рисование квадрата
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size_x, square_size_y))
    for i in range(len(blocks)):
        blocks[i].draw(screen)
    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    pygame.time.Clock().tick(120)
pygame.quit()
sys.exit()