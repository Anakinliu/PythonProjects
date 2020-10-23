import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import vertical

if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建窗口
    main_win = QMainWindow()
    # 创建UI
    main_win_ui = vertical.Ui_MainWindow()
    # 绑定UI与窗口
    main_win_ui.setupUi(main_win)
    # setTitle要在setuoUi地下设置
    main_win.setWindowTitle("垂直布局")
    # 显示窗口
    main_win.show()
    # 关闭
    sys.exit(app.exec_())

