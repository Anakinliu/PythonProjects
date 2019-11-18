import sys  # handle the exit status of the application.

from PyQt5.QtWidgets import (QApplication,
                             QLabel,
                             QWidget,
                             )

# create an instance of QApplication
app = QApplication(sys.argv)  # does so much initialization
# if you are not going to accept any command
# line arguments, replace sys.argv with []

# create an instance of application's GUI
window = QWidget()
window.setWindowTitle('My First PyQt5 App')
# x, y position and width, height size
window.setGeometry(600, 600, 300, 350)

# any QWidget except top-level windows has a parent
helloMsg = QLabel('<h1>Hello World!</h1>',
                  parent=window)
helloMsg.move(70, 50)

# show GUI
window.show()  # schedules a paint event

# run application's event loop
sys.exit(app.exec_())
# wrapped in a call to sys.exit(), which allows you to cleanly exit Python
# and release memory resource when app terminates



