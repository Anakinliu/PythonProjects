from kivy.app import App
from kivy.uix.gridlayout import GridLayout  # as base for Root Weight
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        # 不要忘了调用super进行父类初始化
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='User name'))

        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="password"))

        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class Login(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    Login().run()
