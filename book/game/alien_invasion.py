import sys
import pygame
from book.game.settings import Settings
from book.game.ship import Ship

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

    # 设置背景色
    bg_color = (130, 130, 230)  # 只需指定一次
    bg_color_2 = (30, 230, 30)

    # 创建飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监视键盘与鼠标, 去掉本段会无法正常退出游戏!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 单击窗口的X就可以关闭
                sys.exit()

        # 每次循环时重绘屏幕
        screen.fill(ai_settings.bg_color)

        ship.build_self()
        ship.change_position()

        """
        命令pygame, 将最近绘制的屏幕设为可见
        每次循环就绘制一个屏幕, 擦去上次绘制的屏幕
        因此角色平滑移动
        """
        pygame.display.flip()


run_game()
