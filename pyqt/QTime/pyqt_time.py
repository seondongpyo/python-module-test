import sys

from PyQt5.QtCore import Qt, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow


class TestApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.time = QTime.currentTime()  # 현재 시간 가져오기
        self.initialize_ui()

    def initialize_ui(self):
        self.statusBar().showMessage(self.time.toString(Qt.DefaultLocaleLongDate))  # 오전/오후 시:분:초
        # self.statusBar().showMessage(self.time.toString(Qt.DefaultLocaleShortDate))  # 오전/오후 시:분
        # print(self.time.toString('hh:mm:ss'))  # toString()에 포맷 형식을 지정할 수 있다 (시(h), 분(m), 초(s))

        self.setWindowTitle('QTime')
        self.setGeometry(600, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    sys.exit(app.exec_())
