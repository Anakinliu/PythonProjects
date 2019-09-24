from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.uix.label import Label
from kivy.uix.button import Button


class PongPaddle(Widget):
    """
    This algorithm for ball bouncing is very simple,
     but will have strange behavior
     if the ball hits the paddle from the side
     or bottom…this is something you could
     try to fix yourself if you like.
    """
    score = NumericProperty(0)

    def bounce_ball(self, ball):

        if self.collide_widget(ball):
            # print('collide bounced')
            speedup = 1.0
            offset = 0.02 * Vector(ball.center_x - self.center_x, ball.center_y - self.center_y)
            # print('offset: ', offset)
            ball.v = speedup * (offset - ball.v)


class PongBall(Widget):
    # v of the ball on x and y axis
    v_x = NumericProperty(0)
    v_y = NumericProperty(0)

    #
    v = ReferenceListProperty(v_x, v_y)

    # this will be called in equal
    # intervals to animate the ball
    def move(self):
        # 打散self.v
        # print(self.v, self.v_x, self.v_y)
        self.pos = Vector(*self.v) + self.pos

    def reset_all_v(self):
        self.v = Vector(30, 30).rotate(randint(0, 360))


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    win_text = Label()
    restart_button = Button()

    def serve_ball(self):
        # 只执行一次
        self.ball.center_x = self.center_x
        self.ball.center_y = self.center_y
        self.ball.reset_all_v()

    pass

    def update(self, dt):
        # call ball.move and oths
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            print('碰到上下边界')
            self.ball.v_y *= -1
        if (self.ball.x < 0) or (self.ball.right > self.width):
            print('碰到左右边界')
            self.ball.v_x *= -1

        # score
        if self.ball.x < self.x:
            self.player2.score += 1
        if self.ball.x + self.ball.size[0] > self.width:
            self.player1.score += 1

        # 游戏结束
        if self.win_just():
            if self.win_text not in self.children:
                self.add_widget(self.win_text)
            # If the callback returns False, the schedule will be canceled and won’t repeat.
            self.restart()
            return False
        pass

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    pass

    def win_just(self):
        if self.player1.score >= 1:
            self.win_text.text = "Player 1 win!"
            self.win_text.center_x = self.center_x
            self.win_text.center_y = self.center_y
            return True
        if self.player2.score >= 1:
            self.win_text.text = "Player 2 win!"
            self.win_text.center_x = self.center_x
            self.win_text.center_y = self.center_y
            return True

    pass

    def reset(self):
        self.remove_widget(self.win_text)
        # print("...remove win_text")
        self.remove_widget(self.restart_button)

        self.serve_ball()
        global event
        event()  # 再次执行

        self.player1.score = 0
        self.player2.score = 0
        pass

    def restart(self):
        global event
        event.cancel()

        def call(bt):
            self.reset()

        self.restart_button.text = "Again"
        if self.restart_button not in self.children:
            self.add_widget(self.restart_button)
        self.restart_button.bind(on_press=call)
        self.restart_button.center_x = self.center_x
        self.restart_button.center_y = self.center_y - self.restart_button.height
    pass


class PongApp(App):

    def build(self):
        game = PongGame()
        # 初始化ball
        game.serve_ball()
        # 每秒60次
        global event
        event = Clock.schedule_interval(game.update, 1.0/60)
        return game


if __name__ == '__main__':
    PongApp().run()
