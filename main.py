import pygame
import sys
import random

from ball import Ball
from block import Block


def generate_level():
    global blocks, ball
    blocks = [Block(150 + 100 * i, 200 - 80 * j) for i in range(5) for j in range(level)]
    ball.x = 300
    ball.y = 400


# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простое приложение Pygame")

# Цвета
BLACK = (0, 0, 0)
BLUE = (170, 0, 0)
level = 4
# Параметры квадрата
square_size_x = 100
square_size_y = 20
square_x = WIDTH // 2 - square_size_x // 2
square_y = HEIGHT - 50
square_speed = 7

ball = Ball()
font = pygame.font.Font(None, 45)

generate_level()

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

    if len(blocks) == 0:
        level += 1
        generate_level()

    block_s = font.render(str(len(blocks)), True, (255, 255, 255))
    level_text = font.render(f"level: {level}", True, (255, 255, 255))
    screen.blit(block_s, (20, 300))
    screen.blit(level_text, (0, 10))
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