import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow


class TestApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        exit_action = QAction(QIcon('quit.png'), 'Quit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Quit application')
        exit_action.triggered.connect(qApp.quit)

        self.statusBar()

        self.tool_bar = self.addToolBar('Exit')  # 툴바 생성
        self.tool_bar.addAction(exit_action)  # 툴바에 exit_action 추가

        self.setWindowTitle('QToolBar')
        self.move(300, 300)
        self.resize(400, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    sys.exit(app.exec_())
