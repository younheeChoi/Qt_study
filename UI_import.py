# 다른 file에 있는 클래스 불러오기.
from Qt.test_UI import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


# 만들어둔 UI 불러
class MyWindow(QMainWindow):
    def __init__(self):
        # super 붙임으로써 상속
        super().__init__()
        # self.ui를 적어서 ui라는 변수에 넣어둠
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 보여주기_함수 안에 있으므로 뒤에 어떤걸 보여주기는 안붙여도됨
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()