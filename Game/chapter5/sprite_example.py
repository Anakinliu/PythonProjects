# template
import pygame
import pathlib
pass

import os

FPS = 60
HEIGHT = 800
WIDTH = 600
BLACK = (0, 0, 0)
WHITE = (255, 111, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(player_img_path).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5


# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # 播放音乐需要初始化
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("我的游戏")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # FPS
    clock.tick(FPS)
    # process input event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update()
    # draw
    window.fill(WHITE)
    all_sprites.draw(window)
    # after draw everything, flip
    pygame.display.flip()

pygame.quit()