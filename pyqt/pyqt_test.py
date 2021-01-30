import sys

from PyQt5.QtWidgets import QApplication, QWidget


class TestApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle('Test Application')  # 타이틀 설정
        self.move(300, 300)  # 위치 지정
        self.resize(400, 400)  # 크기 지정
        self.show()  # 화면 표시


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    sys.exit(app.exec_())
