import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class StopwatchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.make)

    def make(self):
        self.flag = True
        self.update()

    def paintEvent(self, QPaintEvent):
        if self.flag:
            painter = QPainter()                    
            painter.begin(self)
            painter.setPen(QColor(255, 255, 0))
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(randint(0, 500), randint(0, 300), 100, 100)
            painter.setPen(QColor(255, 255, 0))
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(randint(0, 500), randint(0, 300), 100, 100)
            painter.end()
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StopwatchApp()
    window.show()
    sys.exit(app.exec_())