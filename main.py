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
length_snake = 1
dx, dy = 0, 0
fps = 7
# Словарь движения
traffic_dict = {"W": (0, -1), "S": (0,1), "A": (-1,0), "D": (1,0)}
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
    body_snake.append((x, y))
    body_snake = body_snake[-length_snake:]
    # Модуль для индетифицирования нажатой клавиши
    key = pygame.key.get_pressed()
    # Условия движения
    if key[pygame.K_w] and (dx, dy) != traffic_dict["S"]:
        dx, dy = traffic_dict["W"]
    if key[pygame.K_s] and (dx, dy) != traffic_dict["W"]:
        dx, dy = traffic_dict["S"]
    if key[pygame.K_a] and (dx, dy) != traffic_dict["D"]:
        dx, dy = traffic_dict["A"]
    if key[pygame.K_d] and (dx, dy) != traffic_dict["A"]:
        dx, dy = traffic_dict["D"]
    # Условие закрытия программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # Обновление экрана
    pygame.display.flip()
    # Управление частотой кадров
    clock = pygame.time.Clock()
    # Количество раз выполнения цикла в секунду
    clock.tick(2*fps)