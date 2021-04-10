import pygame
import random
import config
import player
import sys

# config
WIDTH, HEIGHT, FPS = config.WIDTH, config.HEIGHT, config.FPS
RED, BLACK, GREEN, LIGHT_YELLOW = config.RED, config.BLACK, config.GREEN, config.LIGHT_YELLOW
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
# / config

# player
RIGHT, LEFT, UP, DOWN, STOP = player.RIGHT, player.LEFT, player.UP, player.DOWN, player.STOP
motion = STOP  # начальное состояние
speed = player.speed  # 10
# / player


# Цикл игры
def game_loop():
    global motion
    running = True
    userX = 300
    userY = 300
    while running:
        clock.tick(FPS)  # держим цикл на правильной скорости
        for event in pygame.event.get():  # обработка событий
            if event.type == pygame.QUIT:
                pygame.quit()  # завершить pygame
                quit()  # выйти
            '''elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    motion = LEFT
                elif event.key == pygame.K_RIGHT:
                    motion = RIGHT
                elif event.key == pygame.K_UP:
                    motion = UP
                elif event.key == pygame.K_DOWN:
                    motion = DOWN
            else:
                motion = STOP'''

        '''if motion == LEFT:
            userX -= speed
        elif motion == RIGHT:
            userX += speed
        elif motion == UP:
            userY -= speed
        elif motion == DOWN:
            userY += speed
        else:
            pass'''

        # клавиатура
        # перейти на векторы
        keys = pygame.key.get_pressed()  # снимает "маску" зажатых клавиш. 1 - зажата, 0 - нет
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            userX -= speed
            userY -= speed
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            userX -= speed
            userY += speed
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            userX += speed
            userY -= speed
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            userX += speed
            userY += speed
        elif keys[pygame.K_LEFT]:
            userX -= speed
        elif keys[pygame.K_RIGHT]:
            userX += speed
        elif keys[pygame.K_UP]:
            userY -= speed
        elif keys[pygame.K_DOWN]:
            userY += speed
        else:
            pass
        # / клавиатура

        # мышь
        pressed = pygame.mouse.get_pressed(num_buttons=3)  # (False, False, False)
        pos = pygame.mouse.get_pos()
        if pressed[0]:
            print(pos)
        # / мышь

        display.fill(LIGHT_YELLOW)
        pygame.draw.circle(display, RED, (userX, userY), 70)
        pygame.display.update()


game_loop()
