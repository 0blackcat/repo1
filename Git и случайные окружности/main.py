import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class File:
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)


class Example(QMainWindow, File):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.pushButton.clicked.connect(self.make)

    def make(self):
        self.flag = True
        self.update()

    def paintEvent(self, QPaintEvent):
        if self.flag:
            painter = QPainter()                    
            painter.begin(self)
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            painter.setPen(QColor(*self.color))
            painter.setBrush(QColor(*self.color))
            q = randint(10, 200)
            painter.drawEllipse(randint(0, 500), randint(0, 300), q, q)
            painter.setPen(QColor(255, 255, 0))
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(randint(0, 500), randint(0, 300), q, q)
            painter.end()
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(app.exec_())