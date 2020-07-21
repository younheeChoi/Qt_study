from PySide2.QtWidgets import QApplication,QMainWindow
import sys
from PySide2.QtCharts import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('test')
        self.setGeometry(100,100,400,400)

        self.show()


# class 생성한거 창으로 띄워주는것
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # class 이름 으로 찾기
    myWindow = Window()
    app.exec_()