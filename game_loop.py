import pygame
import random
import config
import gui


WIDTH, HEIGHT, FPS = config.WIDTH, config.HEIGHT, config.FPS
RED, BLACK, GREEN, LIGHT_YELLOW = config.RED, config.BLACK, config.GREEN, config.LIGHT_YELLOW


class Player(pygame.sprite.Sprite):
    def __init__(self, player_imges, vel=3):
        pygame.sprite.Sprite.__init__(self)
        self.images = player_imges
        self.image = self.images['down_0']
        self.state = 'down'
        self.rect = self.image.get_rect()  # оценивает изображение и высчитывает прямоугольник, способный окружить его
        self.rect.center = (config.WIDTH/2, config.HEIGHT/2)
        self.vel = vel

    def change_img(self, img):
        self.image = self.images['face']
        # self.rect = self.image.get_rect()  # оценивает изображение и высчитывает прямоугольник, способный окружить его
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
        if keys[pygame.K_UP]:
            self.rect.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.rect.y += self.vel


# Цикл игры
def game_loop():

    clock = pygame.time.Clock()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    all_sprites = pygame.sprite.Group()

    player_images = {
        'down_0': pygame.image.load('assets/minotaur-S-stand.png').convert(),
        'up_0': pygame.image.load('assets/minotaur-N-stand.png').convert(),
        'right_0': pygame.image.load('assets/minotaur-W-stand.png').convert(),  # надо создать еще Е картники
        'right_1': pygame.image.load('assets/minotaur-W-step1.png').convert(),
        'right_2': pygame.image.load('assets/minotaur-W-step2.png').convert(),
        'left_0': pygame.image.load('assets/minotaur-W-stand.png').convert(),
        'left_1': pygame.image.load('assets/minotaur-W-step1.png').convert(),
        'left_2': pygame.image.load('assets/minotaur-W-step2.png').convert(),
        'up_1': pygame.image.load('assets/minotaur-N-step1.png').convert(),
        'up_2': pygame.image.load('assets/minotaur-N-step2.png').convert(),
        'down_1': pygame.image.load('assets/minotaur-S-step1.png').convert(),
        'down_2': pygame.image.load('assets/minotaur-S-step2.png').convert()
    }

    player = Player(player_images, 10)
    all_sprites.add(player)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # завершить pygame
                quit()  # выйти

        # мышь
        pressed = pygame.mouse.get_pressed(num_buttons=3)  # (False, False, False)
        pos = pygame.mouse.get_pos()
        if pressed[0]:
            print(pos)
        # / мышь

        player.move()
        display.fill(LIGHT_YELLOW)
        all_sprites.update()
        all_sprites.draw(display)
        pygame.display.update()
