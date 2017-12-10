"""
AUTHOR: Anakinliu
DATE: 17.11.29
TIME: 19:18
DO TOUR BEST
"""
import pygame
import random


class Ship:

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""

        self.screen = screen  # 得到screen对象

        self.ai_settings = ai_settings

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load(r'images\ship.png')  # 返回表示飞船的surface
        self.rect = self.image.get_rect()  # 得到相应surface的rect属性
        print(type(self.image))  # <class 'pygame.Surface'>
        print(type(self.screen))  # <class 'pygame.Surface'>
        self.screen_rect = screen.get_rect()  # 得到相应surface的rect属性
        print(type(self.screen_rect))  # <class 'pygame.Rect'>
        """像处理矩形一样处理矩形元素, 虽然飞船并非矩形, 
        但是矩形形状简单, 处理效率高, 而且玩家感受不到
        矩形与真实图形区别"""

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        """
        rect对象经常用的属性:
        居中: center, centerx , centery
        屏幕边缘: top, bottom, left, right
        座标: ｘ，　ｙ
        Python的0, 0在左上角
        """

        # 移动的标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 在飞船center属性中存储小数, center是小数, 因为rect.centerx不能是小数
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

    def build_self(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        # print("ship.update()")
        """根据移动的标志调整飞船位置, 不能移到窗口外"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # print("right")
            self.center_x += self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center_x
        if self.moving_left and self.rect.left > 0:  # 注意不要使用elif, 影响左右键同时按下时的动作
            # print("left")
            self.center_x -= self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center_x

        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
            self.rect.centery = self.center_y
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:  # 注意不要使用elif, 影响左右键同时按下时的动作
            self.center_y += self.ai_settings.ship_speed_factor
            self.rect.centery = self.center_y

        # 根据self.center更新rect对象的centerx
        # self.rect.centerx = self.center  # 注意, centerx会舍弃任何小数部分
        # print(self.center)

    def change_position(self):
        """
        闪瞎你的狗眼
        :return: pass
        """
        rand_int = random.randint(0, 3)
        if rand_int == 0:
            self.rect.centerx = self.screen_rect.centerx
            self.rect.top = self.screen_rect.top
        if rand_int == 1:
            self.rect.centery = self.screen_rect.centery
            self.rect.left = self.screen_rect.left
        if rand_int == 2:
            self.rect.centery = self.screen_rect.centery
            self.rect.right = self.screen_rect.right
        if rand_int == 3:
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom
