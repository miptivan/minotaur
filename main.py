import pygame
import random
import config
import player
import sys
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, player_img):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((200, 200))
        self.image = player_img
        # self.image.fill((123, 12, 123))
        self.rect = self.image.get_rect()  # оценивает изображение и высчитывает прямоугольник, способный окружить его
        self.rect.center = (config.WIDTH/2, config.HEIGHT/2)

    def update(self):
        '''self.rect.x += 2
        if self.rect.left > config.WIDTH:
            self.rect.right = 0'''
        pass

    def toLeft(self, speed):
        self.rect.x -= speed

    def toRight(self, speed):
        self.rect.x += speed

    def toUp(self, speed):
        self.rect.y -= speed

    def toDown(self, speed):
        self.rect.y += speed


class RectPlayer():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(display, player):
    display.fill(LIGHT_YELLOW)
    player.draw(display)
    all_sprites.update()
    all_sprites.draw(display)
    pygame.display.update()


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

rect_player = RectPlayer(100, 100, 100, 100, RED)


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
            player.toLeft(speed)
            player.toUp(speed)
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            player.toLeft(speed)
            player.toDown(speed)
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            player.toRight(speed)
            player.toUp(speed)
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            player.toRight(speed)
            player.toDown(speed)
        elif keys[pygame.K_LEFT]:
            player.toLeft(speed)
        elif keys[pygame.K_RIGHT]:
            player.toRight(speed)
        elif keys[pygame.K_UP]:
            player.toUp(speed)
        elif keys[pygame.K_DOWN]:
            player.toDown(speed)
        else:
            pass
        # / клавиатура

        # мышь
        pressed = pygame.mouse.get_pressed(num_buttons=3)  # (False, False, False)
        pos = pygame.mouse.get_pos()
        if pressed[0]:
            print(pos)
        # / мышь

        rect_player.move()
        redrawWindow(display, rect_player)


game_loop()
