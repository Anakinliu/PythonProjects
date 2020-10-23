from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

import grid

if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)
    # 创建QMainWindow
    main_win = QMainWindow()
    # 创建UI
    main_win_ui = grid.Ui_MainWindow()
    # 绑定UI和QMainWindow
    main_win_ui.setupUi(main_win)
    # 设置窗口title
    main_win.setWindowTitle("网格布局")
    # 显示窗口
    main_win.show()
    # 退出
    print('exit')
    sys.exit(app.exec_())
