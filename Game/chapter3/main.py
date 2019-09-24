from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty, BooleanProperty)
from kivy.vector import Vector
from kivy.core.audio import SoundLoader

class Bg(Widget):

    def reset(self, x, y):
        self.pos = x, y
    def move(self, df, which):
        current_x = self.pos[0]
        current_y = self.pos[1]
        step_size = 150 * df
        now_x = current_x - step_size
        self.pos = now_x, current_y
        if which == 1:
            if now_x + self.parent.width <= 0:
                # print('bg1 rein')
                self.pos = 0, 0
        if which == 2:
            if now_x <= 0:
                # print('bg2 rein')
                self.pos = self.parent.width, 0
        pass
    pass

class Bullet(Widget):

    launched = BooleanProperty(False)
    hit = BooleanProperty(False)

    def update(self, keySet, pos, df, enemy):
        if self.launched is False:
            self.pos = pos
        if 'spacebar' in keySet and self.launched is False:
            sound = SoundLoader.load('resource/rlaunch.wav')
            sound.play()
            self.launched = True
            pass
        if self.launched:
            self.up(df)
            pass
        # 击中敌人或者飞出边界才能再次发射launched=false

        # 击中敌人
        if self.collide_widget(enemy):
            sound = SoundLoader.load('resource/explode.wav')
            sound.play()
            self.launched = False
            self.hit = True
        # 飞出边界
        if self.pos[1] >= self.parent.height:
            self.launched = False
            self.hit = False
        pass

    def up(self, df):
        step_size = 200 * df
        current_x, current_y = self.pos
        current_y += step_size
        self.pos = current_x, current_y
    pass


class Player(Widget):
    # v of the ball on x and y axis
    v_x = NumericProperty(0)
    v_y = NumericProperty(0)
    # shorcut like pos
    v = ReferenceListProperty(v_x, v_y)

    collide_sound = StringProperty('resource/flaunch.wav')
    can_jump = True

    def move(self, keySet, df):
        current_y = self.pos[1]
        current_x = self.pos[0]
        step_size = 400 * df
        if current_y >= 120:
            self.can_jump = False
            # current_y -= step_size
        if current_y > 25:
            current_y -= step_size
        if current_y <= 25:
            current_y = 25
            self.can_jump = True
        if keySet:
            if 'w' in keySet and self.can_jump:
                current_y += 3 * step_size
            # if 's' in keySet:
            #     current_y -= step_size
            if 'a' in keySet:
                current_x -= step_size
            if 'd' in keySet:
                current_x += step_size
            # print(current_x, current_y)
            pass
        self.pos = current_x, current_y
        pass

    def collide(self, keySet, enemy, df):
        if self.collide_widget(enemy):
            if keySet:
                current_y = self.pos[1]
                current_x = self.pos[0]

                step_size = 1500 * df
                # if 'w' in keySet:
                #     current_y -= step_size
                # if 's' in keySet:
                #     current_y += step_size
                if 'a' in keySet:
                    current_x += step_size
                if 'd' in keySet:
                    current_x -= step_size
                # print(current_x, current_y)
                self.pos = current_x, current_y
            print("-10 HP")
            sound = SoundLoader.load(self.collide_sound)
            if sound:
                print("Sound found at %s" % sound.source)
                print("Sound is %.3f seconds" % sound.length)
                sound.play()

    pass

class Enemy(Widget):
    def move(self, df):
        # print(self.parent.width)  # 800
        current_x, current_y = self.pos
        step_size = 200 * df
        current_x -= step_size
        self.pos = current_x, current_y
        if self.pos[0] <= -self.width:
            self.pos[0] = self.parent.width
        pass
    pass

class BoardListener(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed,
                                                 self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.keysPressed = set()

    def _on_keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        # print('The key', keycode, 'have been pressed')
        # print(' - text is %r' % text)
        # print(' - modifiers are %r' % modifiers)
        self.keysPressed.add(keycode[1])

    def _on_keyboard_up(self, keyboard, keycode):
        # print(keycode) # (119, 'w')
        text = keycode[1]
        # TODO 为什么还要判断？
        if text in self.keysPressed:
            self.keysPressed.remove(text)


class GameWidget(Widget):
    player = ObjectProperty(None)
    enemy = ObjectProperty(None)
    bullet = ObjectProperty(None)
    bg1 = ObjectProperty(None)
    bg2 = ObjectProperty(None)

    boardlistener = BoardListener()
    bgm = StringProperty('resource/Venus.wav')

    def serve_sth(self):
        # print(self.boardlistener.keysPressed)  # set()
        self.player.center_x = self.center_x
        self.sound = SoundLoader.load(self.bgm)

    def update_sth(self, df):
        """

        :param df: 两个帧之间的时间
        :return:
        """
        # print(df)
        # pos是一个tuple类型的(x, y)
        keySet = self.boardlistener.keysPressed

        self.player.move(keySet, df)
        self.player.collide(keySet ,self.enemy, df)
        self.bullet.update(keySet,
                         (self.player.center_x - self.bullet.width // 2,
                          self.player.center_y + self.bullet.height // 2),
                         df,
                           self.enemy)

        self.bg1.move(df, 1)
        self.bg2.move(df, 2)

        if self.sound.state == 'stop':
            self.sound.play()

        self.enemy.move(df)

class MyApp(App):
    def build(self):
        game = GameWidget()
        game.serve_sth()
        Clock.schedule_interval(game.update_sth, 1.0/60)
        return game


if __name__ == '__main__':
    app = MyApp()
    app.run()
