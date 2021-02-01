import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class TestApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle('Locate on Center')
        self.resize(500, 350)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 창의 위치와 크기 정보를 가져온다
        cp = QDesktopWidget().availableGeometry().center()  # 현재 모니터의 가운데 위치를 확인
        qr.moveCenter(cp)  # 화면의 중심으로 이동
        self.move(qr.topLeft())  # 현재 창을 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    sys.exit(app.exec_())
