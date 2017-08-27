# coding: utf-8
import os
from flask import Flask, request, jsonify


import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")

app = Flask(__name__)
project_root = os.path.abspath(".")
music_controller = open(os.path.join(project_root, "templates/index.html"), "r").read()


class MusicBox(object):

    @classmethod
    def next_song(cls):
        shell.SendKeys("%^+{RIGHT}")

    @classmethod
    def prev_song(cls):
        shell.SendKeys("%^+{LEFT}")

    @classmethod
    def pause_play(cls):
        shell.SendKeys("%^+{P}")

    @classmethod
    def volume_up(cls):
        shell.SendKeys("%^+{UP}")

    @classmethod
    def volume_down(cls):
        shell.SendKeys("%^+{DOWN}")

    @classmethod
    def shutdown(cls):
        os.system("shutdown -s -t 60")

    @classmethod
    def shutdown_cancel(cls):
        os.system("shutdown -a")

    @classmethod
    def open_music(cls):
        shell.SendKeys("%^+{M}")

    @classmethod
    def close_switcher(cls):
        os.system("tskill music_switcher")

    @classmethod
    def close_music(cls):
        os.system("tskill cloudmusic")


@app.route('/')
def hello_world():
    key_word = request.args.get("action")
    if key_word:
        getattr(MusicBox, key_word)()

    return music_controller


# 移动端连接服务器校验
@app.route('/mobile_connect')
def mobile_connect():
    response = jsonify(code=200, message="Connected", platform="win", status=1, version="0.0.1")
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

