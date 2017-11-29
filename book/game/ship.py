"""
AUTHOR: Anakinliu
DATE: 17.11.29
TIME: 19:18
DO TOUR BEST
"""
import pygame
import random


class Ship:

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""

        self.screen = screen  # 得到screen对象

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load(r'images\ship.png')  # 返回表示飞船的surface
        self.rect = self.image.get_rect()  # 得到相应surface的rect属性
        self.screen_rect = screen.get_rect()  # 得到相应surface的rect属性
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

    def build_self(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def change_position(self):
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
