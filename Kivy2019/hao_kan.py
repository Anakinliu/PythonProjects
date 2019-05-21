import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
kivy.require('1.10.1')
class M3App(App):

    def build(self):
        """
        初始化ROot weight
        :return: root weight
        """
        return Label(text="你好 zz!")


if __name__ == '__main__':
    M3App().run()
