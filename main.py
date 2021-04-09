import pygame
import random
import config

WIDTH, HEIGHT, FPS = config.WIDTH, config.HEIGHT, config.FPS
RED, BLACK, GREEN, LIGHT_YELLOW = config.RED, config.BLACK, config.GREEN, config.LIGHT_YELLOW
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))

# движение
RIGHT = "r"  # r - right
LEFT = "l"  # l - left
UP = "u"  # u - up
DOWN = "d"  # d - down
STOP = "s"  # s - stop
motion = STOP
# /движение


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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    motion = LEFT
                elif event.key == pygame.K_RIGHT:
                    motion = RIGHT
                elif event.key == pygame.K_UP:
                    motion = UP
                elif event.key == pygame.K_DOWN:
                    motion = DOWN
            else:
                motion = STOP

        if motion == LEFT:
            userX -= 3
        elif motion == RIGHT:
            userX += 3
        elif motion == UP:
            userY -= 3
        elif motion == DOWN:
            userY += 3
        else:
            pass

        display.fill(LIGHT_YELLOW)
        pygame.draw.circle(display, RED, (userX, userY), 70)
        pygame.display.update()


game_loop()
