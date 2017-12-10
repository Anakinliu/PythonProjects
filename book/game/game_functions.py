"""
AUTHOR: Anakinliu
DATE: 17.12.5
TIME: 18:52
DO TOUR BEST

将事件管理与游戏的其他方面(例如更新屏幕)分割开
"""
import sys
import pygame


def check_events(ship):
    """
    响应按键与鼠标事件
    用户的输入都将在Pygame中注册一个事件, 事件通过pygame.event.get()获取
    pygame.event模块用于Python与事件和队列进行交互
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 事件类型是某个按键被按下
            check_key_down_events(event, ship)

        elif event.type == pygame.KEYUP:  # 按键被松开那一刻触发
            check_key_up_events(event, ship)


def check_key_down_events(event, ship):
    """处理按键按下事件"""
    if event.key == pygame.K_RIGHT:
        # 玩家想要向右移动飞船
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # 玩家想要向右移动飞船
        ship.moving_left = True
    if event.key == pygame.K_UP:
        # 玩家想要向上移动飞船
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        # 玩家想要向下移动飞船
        ship.moving_down = True


def check_key_up_events(event, ship):
    """处理按键松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        #
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        # 玩家想要向上移动飞船
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        # 玩家想要向下移动飞船
        ship.moving_down = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像, 并切换屏幕"""
    # 每次循环时重绘屏幕
    screen.fill(ai_settings.bg_color)

    ship.build_self()
    ship.update()
    # ship.change_position()

    """
    命令pygame, 将最近绘制的屏幕设为可见
    每次循环就绘制一个屏幕, 擦去上次绘制的屏幕
    因此角色平滑移动
    """
    pygame.display.flip()

