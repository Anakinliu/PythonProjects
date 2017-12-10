import sys
import pygame
from book.game.settings import Settings
from book.game.ship import Ship
import book.game.game_functions as g_f


def run_game():
    # 初始化游戏, 并创建一个屏幕 对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))  # 参数是一个 元组, 加括号的那种
    pygame.display.set_caption("Alien Invasion")
    """
    screen对象是一个surface, 属于屏幕的一部分
    游戏中的角色都属于surface
    """

    # 设置背景色 | 已放入settings.py中
    # bg_color = (130, 130, 230)  # 只需指定一次
    # bg_color_2 = (30, 230, 30)

    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏主循环
    while True:

        # 监视键盘与鼠标, 去掉本段会无法正常退出游戏!
        g_f.check_events(ship)

        g_f.update_screen(ai_settings, screen, ship)

        # print("==========")
        # print(ship.rect.x)
        # print(ship.rect.y)
        # print("==========")


run_game()
