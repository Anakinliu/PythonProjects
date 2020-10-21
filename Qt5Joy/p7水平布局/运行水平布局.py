import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import demo

if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWin = QMainWindow()
    # 创建UI类
    ui = demo.Ui_MainWindow()
    # 设置ui
    ui.setupUi(mainWin)
    # 显示UI
    mainWin.show()
    # 退出
    sys.exit(app.exec_())