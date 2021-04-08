import pygame
import random

WIDTH = 500  # ширина игрового окна
HEIGHT = 500  # высота игрового окна
FPS = 30  # частота кадров в секунду
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (252, 250, 184)

'''pygame.init()  # запускает pygame
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()'''

display = pygame.display.set_mode((WIDTH, HEIGHT))


# Цикл игры
def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # завершить pygame
                quit()  # выйти
        display.fill(YELLOW)
        pygame.display.update()


game_loop()
