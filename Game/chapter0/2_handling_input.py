import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window()


@window.event
def on_key_press(symbol, modifiers):
    """
    :param symbol: defined in pyglet.window.key
    :param modifiers: a bitwise combination of any
      modifiers that are present (for example,
      the CTRL and SHIFT keys).
    :return:
    """
    print('A key was pressed')
    if symbol == key.S:
        print('S ')
    if modifiers & key.LCTRL:  # 使用按位或运算判断
        print('LCTRL')
    if symbol == key.S and modifiers & key.LCTRL:
        print('saved')


@window.event
def on_mouse_press(x, y, button, modifiers):
    """

    :param x: the position of the mouse when
     the button was pressed, relative to the lower-left corner of the window.
    :param y:
    :param button:
    :param modifiers:
    :return:
    """
    if button == mouse.LEFT:
        print('the lmt was pressed')


@window.event
def on_draw():
    window.clear()


# 显示事件log
window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()
