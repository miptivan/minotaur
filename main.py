import pygame
import random
import config
import player
import sys
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, player_img):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 100))
        self.image = player_img
        # self.image.fill((123, 12, 123))
        self.rect = self.image.get_rect()  # оценивает изображение и высчитывает прямоугольник, способный окружить его
        self.rect.center = (config.WIDTH/2, config.HEIGHT/2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > config.WIDTH:
            self.rect.right = 0


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

# bull-sprite
all_sprites = pygame.sprite.Group()

game_folder = os.path.dirname(__file__)
assets_folder = os.path.join(game_folder, 'assets')
# convert() ускорит прорисовку в Pygame, конвертируя изображение в тот формат,
# который будет быстрее появляться на экране
player_img = pygame.image.load(os.path.join(assets_folder, 'minotaur-S-stand.png')).convert()
player = Player(player_img)
all_sprites.add(player)
# / bull-sprite


# Цикл игры
def game_loop():
    global motion
    running = True
    user_x = random.randrange(0, WIDTH)
    user_y = random.randrange(0, HEIGHT)
    while running:
        clock.tick(FPS)  # держим цикл на правильной скорости
        for event in pygame.event.get():  # обработка событий
            if event.type == pygame.QUIT:
                pygame.quit()  # завершить pygame
                quit()  # выйти

        # клавиатура
        # перейти на векторы!!!
        keys = pygame.key.get_pressed()  # снимает "маску" зажатых клавиш. 1 - зажата, 0 - нет
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            user_x -= speed
            user_y -= speed
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            user_x -= speed
            user_y += speed
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            user_x += speed
            user_y -= speed
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            user_x += speed
            user_y += speed
        elif keys[pygame.K_LEFT]:
            user_x -= speed
        elif keys[pygame.K_RIGHT]:
            user_x += speed
        elif keys[pygame.K_UP]:
            user_y -= speed
        elif keys[pygame.K_DOWN]:
            user_y += speed
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
        all_sprites.update()
        all_sprites.draw(display)
        pygame.draw.circle(display, RED, (user_x, user_y), 70)
        pygame.display.update()


game_loop()
