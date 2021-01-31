import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow


class TestApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        exit_action = QAction(QIcon('quit.png'), 'Quit', self)  # 아이콘(quit.png)과 라벨(Quit)을 갖는 하나의 동작을 생성
        exit_action.setShortcut('Ctrl+Q')  # 단축키 정의
        exit_action.setStatusTip('Quit application')  # 상태 바에 나타낼 팁 정의
        exit_action.triggered.connect(qApp.quit)  # 동작 선택 시 어플리케이션이 종료되도록 연결

        self.statusBar()

        menu_bar = self.menuBar()  # 메뉴 바 생성
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('&File')  # File 메뉴를 생성하고 단축키 설정 ('&'가 앞에 있으면 Alt, 즉 Alt + F)
        file_menu.addAction(exit_action)

        self.setWindowTitle('QMenuBar')
        self.move(300, 300)
        self.resize(400, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    sys.exit(app.exec_())
