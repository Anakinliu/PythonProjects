import pyglet

window = pyglet.window.Window()

# 显示字的label
label = pyglet.text.Label('Hello != world',
                          font_name='Fira Code',
                          font_size=36,
                          x=window.width//2,
                          y=window.height//2,
                          anchor_x='center',
                          anchor_y='center')

# attach event handlers to objects
@window.event
def on_draw():
    window.clear()
    label.draw()


"""
This will enter pyglet’s default event loop, 
and let pyglet respond to application events 
such as the mouse and keyboard. 
Your event handlers will now be called as required,
 and the run() method will return only when 
 all application windows have been closed.
"""
pyglet.app.run()