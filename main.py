import pygame
import random
import config

WIDTH, HEIGHT, FPS = config.WIDTH, config.HEIGHT, config.FPS
RED, BLACK, LIGHT_YELLOW = config.RED, config.BLACK, config.LIGHT_YELLOW
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))


# Цикл игры
def game_loop():
    running = True
    while running:
        clock.tick(FPS)  # держим цикл на правильной скорости
        for event in pygame.event.get():  # обработка событий
            if event.type == pygame.QUIT:
                pygame.quit()  # завершить pygame
                quit()  # выйти
        display.fill(LIGHT_YELLOW)
        pygame.draw.rect(display, RED, (20, 20, 100, 100))
        pygame.draw.rect(display, BLACK, (50, 50, 150, 150))
        pygame.draw.circle(display, RED, (100, 100), 50)
        pygame.display.update()


game_loop()
