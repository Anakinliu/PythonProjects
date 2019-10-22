# template
import pygame
import random
import os
import pathlib

FPS = 60
HEIGHT = 600
WIDTH = 480
# colors
BLACK = (0, 0, 0)
Pink = (255, 111, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_path = pathlib.Path().cwd()
img_path = game_path.joinpath('imgs')



class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self, *groups):
        super().__init__(*groups)
        # self.image = pygame.Surface((50, 40))
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        self.rect.x += self.speedx

        #  border movement limit
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(x=self.rect.centerx, y=self.rect.y)
        bullets.add(bullet)
        all_sprites.add(bullet)




class Mob(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self, *args):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.right < 0 \
                or self.rect.left > WIDTH:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, *groups, x=0, y=0):
        super().__init__(*groups)
        self.image = pygame.Surface((10, 20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self, *args):
        self.rect.y += self.speedy
        # kill if bullet out of screen
        if self.rect.bottom < 0:
            self.kill()

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # 播放音乐需要初始化
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("我的游戏")
clock = pygame.time.Clock()


background = pygame.image.load(
    str(img_path.joinpath('bg.png'))
).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(
    str(img_path.joinpath('playerShip1_blue.png'))
).convert()
meteor_img = pygame.image.load(
    str(img_path.joinpath('meteorBrown_med1.png'))
).convert()
enemy_img = pygame.image.load(
    str(img_path.joinpath('enemyRed1.png'))
).convert()

bullet_img = pygame.image.load(
    str(img_path.joinpath('laserBlue01.png'))
).convert()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

mobs = pygame.sprite.Group()
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

bullets = pygame.sprite.Group()



# Game loop
running = True
while running:
    # FPS
    clock.tick(FPS)
    # process input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    # update
    all_sprites.update()
    # check if bullet hit mob, whether kill
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for e in hits:  # respawn mob
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    # hits not empty means hit player
    if hits:
        running = False
    # draw
    window.fill(Pink)  # 首先draw背景
    # Draws a source Surface onto this Surface.
    # The draw can be positioned with the dest argument.
    # The size of the destination rectangle does not effect the blit.
    window.blit(background, background_rect)
    all_sprites.draw(window)

    mobs.draw(window)
    # after draw everything, flip
    pygame.display.flip()


def show():
    pass


pygame.quit()