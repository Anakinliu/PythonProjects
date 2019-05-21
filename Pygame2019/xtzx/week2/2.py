import simpleguitk as gui
import pyttsx3


def tts(text):
    global engine
    engine.say(text)
    engine.runAndWait()


def key_down(key):
    if key == gui.KEY_MAP['up']:
        tts('滚蛋')


base = gui.create_frame("--小玩意--", 400, 300)
base.set_keydown_handler(key_down)
engine = pyttsx3.init()
base.start()