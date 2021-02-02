import sys

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QMainWindow


class TestApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.now = QDate.currentDate()  # 현재 날짜 가져오기
        self.initialize_ui()

    def initialize_ui(self):
        self.statusBar().showMessage(self.now.toString(Qt.DefaultLocaleLongDate))  # 기본 locale 설정에 맞게 문자열로 변환
        # print(self.now.toString('yyyyMMdd'))  # toString()에 포맷 형식을 지정할 수 있다 (연(y), 월(M), 일(d))

        self.setWindowTitle('QDate')
        self.setGeometry(600, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestApp()
    sys.exit(app.exec_())
