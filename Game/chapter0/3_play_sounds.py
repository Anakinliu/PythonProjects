import pyglet

# 短音使用False，大的使用True
music = pyglet.media.load('resource/media/glass.wav',
                          streaming=True)
music.play()
pyglet.app.run()
