import pygame
import random
import config

WIDTH, HEIGHT, FPS, RED, YELLOW = config.WIDTH, config.HEIGHT, config.FPS, config.RED, config.YELLOW
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
        display.fill(YELLOW)
        pygame.draw.rect(display, RED, (20, 20, 100, 100))
        pygame.display.update()


game_loop()
