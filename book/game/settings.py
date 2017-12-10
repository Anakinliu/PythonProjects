"""
AUTHOR: Anakinliu
DATE: 17.11.29
TIME: 18:56
DO TOUR BEST
"""


class Settings:
    """存储所有设置"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1200  # 宽度
        self.screen_height = 800  # 高度
        # self.bg_color = (30, 30, 30)  # 深色背景色, 红, 绿, 蓝, 0-255
        self.bg_color = (122, 218, 255)  # 天蓝色

        # 飞船设置
        self.ship_speed_factor = 1.50  # 便于将来更精确地控制飞船速度, 1, 3, 4, 6, 7, 9, 10
