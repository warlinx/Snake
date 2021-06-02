# Подключение модулей
import pygame
from random import randrange
# Константы
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (300, 300)
OBJECT_SIZE = 10
# переменные и инициализация
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
x = randrange(0, WINDOW_WIDTH, OBJECT_SIZE)
y = randrange(0, WINDOW_HEIGHT, OBJECT_SIZE)
body_snake = [(x, y)]
body_snake = [(x, y)]
dx, dy = 0, 0
fps = 7
# Цикл программы
while True:
    # Показ экрана и закраска его в черный цвет
    screen.fill(pygame.Color('black'))
    # Отрисовка змейки
    for i, j in body_snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, OBJECT_SIZE, OBJECT_SIZE))
    # Изменение координат змейки
    x += dx * OBJECT_SIZE
    y += dy * OBJECT_SIZE
    # Условие закрытия программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # Обновление экрана
    pygame.display.flip()
    # Управление частотой кадров
    clock = pygame.time.Clock()