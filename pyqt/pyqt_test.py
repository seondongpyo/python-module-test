import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class TestApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.add_quit_button()  # 종료 버튼 추가

        self.setWindowTitle('Test Application')  # 타이틀 설정
        self.move(300, 300)  # 위치 지정
        self.resize(400, 400)  # 크기 지정
        self.show()  # 화면 표시

    def add_quit_button(self):
        btn = QPushButton('종료', self)  # QPushButton('버튼에 표시될 텍스트', '버튼이 위치할 부모 위젯')
        btn.move(150, 150)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)  # 클릭 시 어플리케이션을 종료하도록 이벤트 설정


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    sys.exit(app.exec_())
