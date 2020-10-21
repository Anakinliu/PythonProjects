import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # print(sys.argv)
    # 创建应用
    app = QApplication(sys.argv)
    # 创建窗口
    window = QWidget()
    # 窗口大小
    window.resize(300,400)
    # 窗口位置
    window.move(500,300)
    # 窗口标题
    window.setWindowTitle("第一个")
    # 显示窗口
    window.show()
    # 退出，释放资源
    sys.exit(app.exec_())
