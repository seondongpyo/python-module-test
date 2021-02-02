import sys

from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow


class TestApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.datetime = QDateTime.currentDateTime()  # 현재 날짜와 시간 가져오기
        self.initialize_ui()

    def initialize_ui(self):
        self.statusBar().showMessage(self.datetime.toString(Qt.DefaultLocaleLongDate))  # 연-월-일 요일 오전/오후 시:분:초
        # self.statusBar().showMessage(self.datetime.toString(Qt.DefaultLocaleShortDate))  # 연-월-일 오전/오후 시:분

        # toString()에 포맷 형식을 지정할 수 있다 (QDate, QTime과 동일한 방식)
        # print(self.datetime.toString('yyyy-MM-dd hh:mm:ss'))

        self.setWindowTitle('QDateTime')
        self.setGeometry(600, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    sys.exit(app.exec_())
