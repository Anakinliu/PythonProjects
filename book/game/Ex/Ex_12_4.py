"""
AUTHOR: Anakinliu
DATE: 17.12.10
TIME: 10:25
DO TOUR BEST
"""
import pygame
import sys


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ex_12")

    # 主循环
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEY

        pygame.display.flip()


run_game()