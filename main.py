import pygame
import random
import config

WIDTH, HEIGHT, FPS = config.WIDTH, config.HEIGHT, config.FPS
RED, BLACK, GREEN, LIGHT_YELLOW = config.RED, config.BLACK, config.GREEN, config.LIGHT_YELLOW
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))


# Цикл игры
def game_loop():
    running = True
    x = 0
    while running:
        clock.tick(FPS)  # держим цикл на правильной скорости
        for event in pygame.event.get():  # обработка событий
            if event.type == pygame.QUIT:
                pygame.quit()  # завершить pygame
                quit()  # выйти
        display.fill(LIGHT_YELLOW)

        pygame.draw.rect(display, RED, (x, 20, 100, 100))
        pygame.draw.rect(display, BLACK, (50, 50, 150, 150))
        pygame.draw.circle(display, RED, (100, 200), 70)
        pygame.draw.ellipse(display, GREEN, (300, 50, 280, 100))
        pygame.display.update()
        if x <= WIDTH:
            x += 10
        else:
            x = -100


game_loop()
