import pygame, sys
from pygame.locals import *

# 在调用其他任何Pygame函数之前，总是调用该函数
pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Fool')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
