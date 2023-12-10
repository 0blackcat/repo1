import sys
import io
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class File:
    def __init__(self):
        super().__init__()
        self.a = """<?xml version="1.0" encoding="UTF-8"?>
            <ui version="4.0">
            <class>MainWindow</class>
            <widget class="QMainWindow" name="MainWindow">
            <property name="geometry">
            <rect>
                <x>0</x>
                <y>0</y>
                <width>683</width>
                <height>489</height>
            </rect>
            </property>
            <property name="windowTitle">
            <string>MainWindow</string>
            </property>
            <widget class="QWidget" name="centralwidget">
            <widget class="QPushButton" name="pushButton">
                <property name="geometry">
                <rect>
                <x>430</x>
                <y>420</y>
                <width>241</width>
                <height>23</height>
                </rect>
                </property>
                <property name="text">
                <string>Показать жёлтый круг</string>
                </property>
            </widget>
            </widget>
            <widget class="QMenuBar" name="menubar">
            <property name="geometry">
                <rect>
                <x>0</x>
                <y>0</y>
                <width>683</width>
                <height>21</height>
                </rect>
            </property>
            </widget>
            <widget class="QStatusBar" name="statusbar"/>
            </widget>
            <resources/>
            <connections/>
            </ui>"""


class Example(QMainWindow, File):
    def __init__(self):
        super().__init__()
        f = io.StringIO(self.a)
        uic.loadUi(f, self)
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