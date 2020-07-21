from PySide2.QtWidgets import QApplication, QMainWindow
import sys
from PySide2.QtCharts import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('test')
        self.NewLinechart()
        self.show()

    def NewLinechart(self):
        self.chart_view = QtCharts.QChartView()
        self.setCentralWidget(self.chart_view)

        self.chart_ = QtCharts.QChart()
        data = QtCharts.QLineSeries()
        data.append(-1, 0)
        data.append(1, 1)
        data.append(1, 5)
        data.append(3, 3)

        self.chart_.addSeries(data)
        self.chart_view.setChart(self.chart_)
        # chart 제목 상단
        self.chart_.setTitle('chart제목')

        # chart grid 넣기(point순서가 아닌(순서연결은 되어있음)) -> x,y (0,0)이 고정되지 않음 -> 수정 예정
        self.chart_.createDefaultAxes()

        # chart 배경색 바꾸기, Qcolor 이용 -> RGB로도 변경가능한지 확인 예정
        self.chart_.setBackgroundBrush(QColor("black"))

# class 생성한거 창으로 띄워주는것
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # class 이름 으로 찾기
    myWindow = Window()
    # 코드 실행시 창 보여주는 크기
    myWindow.resize(500,500)
    app.exec_()
