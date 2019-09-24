import pyglet

window = pyglet.window.Window()
image = pyglet.image.load(
    r'resource/image/001.png')


@window.event
def on_draw():  # 改名导致无效
    window.clear()
    # draw image with args coord
    image.blit(9, 0)  # 左下角


pyglet.app.run()
