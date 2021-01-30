import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip


class TestApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        font = QFont('Times', 13)  # QFont('폰트', '크기')
        QToolTip.setFont(font)  # 툴팁에 사용할 폰트 설정

        btn = QPushButton('button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')  # 툴팁에 나타낼 메시지 설정
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('QToolTip')
        self.move(300, 300)
        self.resize(400, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    sys.exit(app.exec_())
