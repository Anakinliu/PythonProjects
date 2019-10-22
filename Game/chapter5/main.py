# template
import pygame
import random

FPS = 60
HEIGHT = 800
WIDTH = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # 播放音乐需要初始化
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("我的游戏")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

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
    window.fill(BLUE)
    all_sprites.draw(window)
    # after draw everything, flip
    pygame.display.flip()

pygame.quit()