from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("calculator_of_physical_quantities")
        MainWindow.setFixedSize(940, 765)
        MainWindow.setStyleSheet("background-color: rgb(34, 34, 46);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 160, 300, 50))
        self.comboBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(251, 91, 93)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 400, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(251, 91, 93)")
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 320, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(530, 400, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color: rgb(251, 91, 93)")
        self.comboBox_3.setObjectName("comboBox_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 80, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(251, 91, 93);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 500, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(251, 91, 93);\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(250, 66, 68);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 240, 340, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(251, 91, 93);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 240, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(251, 91, 93);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 320, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 500, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(251, 91, 93);\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(250, 66, 68);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 20, 380, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(251, 91, 93);")
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(728, 30, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("background-color: rgb(251, 91, 93)")
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(750, 0, 100, 20))
        self.label_5.setStyleSheet("color: rgb(251, 91, 93);")
        self.label_5.setObjectName("label_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 600, 700, 140))
        self.label_6.setStyleSheet("color: rgb(251, 91, 93);")
        self.label_6.setObjectName("label_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_6.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("calculator_of_physical_quantities")
        self.label.setText(_translate("MainWindow", "Единицы измерения"))
        self.pushButton.setText(_translate("MainWindow", "Перевести"))
        self.label_2.setText(_translate("MainWindow", "Полученная величина"))
        self.label_3.setText(_translate("MainWindow", "Исходная величина"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))
        self.label_4.setText(_translate("MainWindow", "Калькулятор физических величин"))
        self.label_5.setText(_translate("MainWindow", "Сменить тему"))

        # иконка
        app.setWindowIcon(QtGui.QIcon('icon.png'))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))

        list_of_physical_quantities = ['------', 'Скорость', 'Масса', 'Длина', 'Время', 'Ускорение', 'Сила', 'Объем'] 
        self.comboBox.addItems(list_of_physical_quantities) 
        self.comboBox.currentTextChanged.connect(self.make) 
        self.pushButton.clicked.connect(self.button)
        self.pushButton_2.clicked.connect(self.clear)
        
        list_2 = ['По умолчанию', 'Светлая', 'Темная']
        self.comboBox_4.addItems(list_2)
        self.comboBox_4.currentTextChanged.connect(self.theme)

    def theme(self, text):
        if text == 'По умолчанию':
            MainWindow.setStyleSheet("background-color: rgb(34, 34, 46);")
            self.comboBox.setStyleSheet("background-color: rgb(251, 91, 93)")
            self.comboBox_2.setStyleSheet("background-color: rgb(251, 91, 93)")
            self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.comboBox_3.setStyleSheet("background-color: rgb(251, 91, 93)")
            self.label.setStyleSheet("color: rgb(251, 91, 93);")
            self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(251, 91, 93);\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(250, 66, 68);\n"
"}")
            self.label_2.setStyleSheet("color: rgb(251, 91, 93);")
            self.label_3.setStyleSheet("color: rgb(251, 91, 93);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(251, 91, 93);\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(250, 66, 68);\n"
"}")
            self.label_4.setStyleSheet("color: rgb(251, 91, 93);")
            self.comboBox_4.setStyleSheet("background-color: rgb(251, 91, 93)")
            self.label_5.setStyleSheet("color: rgb(251, 91, 93);")
            self.label_6.setStyleSheet("color: rgb(251, 91, 93);")

        if text == 'Светлая':
            MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.comboBox.setStyleSheet("background-color: rgb(1, 135, 134)")
            self.comboBox_2.setStyleSheet("background-color: rgb(1, 135, 134)")
            self.lineEdit.setStyleSheet("background-color: rgb(208, 208, 208);;")
            self.comboBox_3.setStyleSheet("background-color: rgb(1, 135, 134)")
            self.label.setStyleSheet("color: rgb(1, 135, 134);")
            self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(1, 135, 134);\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 109, 107);\n"
"}")
            self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(1, 135, 134);\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 109, 107);\n"
"}")
            self.label_2.setStyleSheet("color: rgb(1, 135, 134);")
            self.label_3.setStyleSheet("color: rgb(1, 135, 134);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(208, 208, 208);;")
            self.label_4.setStyleSheet("color: rgb(1, 135, 134);")
            self.comboBox_4.setStyleSheet("background-color: rgb(1, 135, 134)")
            self.label_5.setStyleSheet("color: rgb(1, 135, 134);")
            self.label_6.setStyleSheet("color: rgb(1, 135, 134);")

        if text == 'Темная':
            MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.comboBox.setStyleSheet("background-color: rgb(113, 171, 235)")
            self.comboBox_2.setStyleSheet("background-color: rgb(113, 171, 235)")
            self.lineEdit.setStyleSheet("background-color: rgb(208, 208, 208);")
            self.comboBox_3.setStyleSheet("background-color: rgb(113, 171, 235)")
            self.label.setStyleSheet("color: rgb(113, 171, 235);")
            self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(113, 171, 235);\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(98, 150, 204);\n"
"}")
            self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(113, 171, 235);\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(98, 150, 204);\n"
"}")
            self.label_2.setStyleSheet("color: rgb(113, 171, 235);")
            self.label_3.setStyleSheet("color: rgb(113, 171, 235);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(208, 208, 208);")
            self.label_4.setStyleSheet("color: rgb(113, 171, 235);")
            self.comboBox_4.setStyleSheet("background-color: rgb(113, 171, 235)")
            self.label_5.setStyleSheet("color: rgb(113, 171, 235);")
            self.label_6.setStyleSheet("color: rgb(113, 171, 235);")

    # кнопка очистки
    def clear(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')


    def button(self):
        # если строка пустая и нажали перевести то программа не свернется
        if self.lineEdit.text() != '':
            # проверка есть ли буквы в вводе
            if self.lineEdit.text().isdigit():
                # скорость 
                if self.comboBox_2.currentText() == 'км/ч':
                    if self.comboBox_3.currentText() == 'км/ч':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'км/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 60, 8)))
                    if self.comboBox_3.currentText() == 'км/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 3600, 8))) 
                    if self.comboBox_3.currentText() == 'м/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))
                    if self.comboBox_3.currentText() == 'м/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000 / 60, 8))) 
                    if self.comboBox_3.currentText() == 'м/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 3.6, 8)))
                    if self.comboBox_3.currentText() == 'см/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000, 8)))
                    if self.comboBox_3.currentText() == 'см/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000 / 60, 8)))
                    if self.comboBox_3.currentText() == 'см/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000 / 3600, 8)))

                if self.comboBox_2.currentText() == 'км/мин':
                    if self.comboBox_3.currentText() == 'км/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 60, 8)))
                    if self.comboBox_3.currentText() == 'км/мин':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'км/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 60, 8))) 
                    if self.comboBox_3.currentText() == 'м/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000 * 60, 8)))
                    if self.comboBox_3.currentText() == 'м/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8))) 
                    if self.comboBox_3.currentText() == 'м/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000 / 60, 8)))
                    if self.comboBox_3.currentText() == 'см/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000 * 60, 8)))
                    if self.comboBox_3.currentText() == 'см/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000, 8)))
                    if self.comboBox_3.currentText() == 'см/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000 / 60, 8)))
                
                if self.comboBox_2.currentText() == 'км/с':
                    if self.comboBox_3.currentText() == 'км/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 3600, 8)))
                    if self.comboBox_3.currentText() == 'км/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 60, 8)))
                    if self.comboBox_3.currentText() == 'км/с':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'м/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000 * 3600, 8)))
                    if self.comboBox_3.currentText() == 'м/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000 * 60, 8))) 
                    if self.comboBox_3.currentText() == 'м/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))
                    if self.comboBox_3.currentText() == 'см/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000 * 3600, 8)))
                    if self.comboBox_3.currentText() == 'см/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000 * 60, 8)))
                    if self.comboBox_3.currentText() == 'см/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000, 8)))
                
                if self.comboBox_2.currentText() == 'м/ч':
                    if self.comboBox_3.currentText() == 'км/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000, 8)))
                    if self.comboBox_3.currentText() == 'км/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000 / 60, 8))) 
                    if self.comboBox_3.currentText() == 'км/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000 / 3600, 8)))
                    if self.comboBox_3.currentText() == 'м/ч':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'м/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 60, 8))) 
                    if self.comboBox_3.currentText() == 'м/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 3600, 8)))
                    if self.comboBox_3.currentText() == 'см/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100, 8)))
                    if self.comboBox_3.currentText() == 'см/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100 / 60, 8)))
                    if self.comboBox_3.currentText() == 'см/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100 / 3600, 8)))

                if self.comboBox_2.currentText() == 'м/мин':
                    if self.comboBox_3.currentText() == 'км/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000 * 60, 8)))
                    if self.comboBox_3.currentText() == 'км/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000, 8))) 
                    if self.comboBox_3.currentText() == 'км/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000 / 60, 8)))
                    if self.comboBox_3.currentText() == 'м/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 60, 8)))
                    if self.comboBox_3.currentText() == 'м/мин':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text())))) 
                    if self.comboBox_3.currentText() == 'м/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 60, 8)))
                    if self.comboBox_3.currentText() == 'см/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100 * 60, 8)))
                    if self.comboBox_3.currentText() == 'см/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100, 8)))
                    if self.comboBox_3.currentText() == 'см/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100 / 60, 8)))
                
                if self.comboBox_2.currentText() == 'м/с':
                    if self.comboBox_3.currentText() == 'км/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000 * 3600, 8)))
                    if self.comboBox_3.currentText() == 'км/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000 * 60, 8))) 
                    if self.comboBox_3.currentText() == 'км/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000, 8)))
                    if self.comboBox_3.currentText() == 'м/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 3600, 8))) 
                    if self.comboBox_3.currentText() == 'м/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 60, 8)))
                    if self.comboBox_3.currentText() == 'м/с':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text())))) 
                    if self.comboBox_3.currentText() == 'см/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100 * 3600, 8)))
                    if self.comboBox_3.currentText() == 'см/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100 * 60, 8)))
                    if self.comboBox_3.currentText() == 'см/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100, 8)))

                if self.comboBox_2.currentText() == 'см/ч':
                    if self.comboBox_3.currentText() == 'км/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000, 8)))
                    if self.comboBox_3.currentText() == 'км/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000 / 60, 8))) 
                    if self.comboBox_3.currentText() == 'км/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000 / 3600, 8)))
                    if self.comboBox_3.currentText() == 'м/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100, 8))) 
                    if self.comboBox_3.currentText() == 'м/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100 / 60, 8)))
                    if self.comboBox_3.currentText() == 'м/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100 / 3600, 8)))
                    if self.comboBox_3.currentText() == 'см/ч':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'см/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 60, 8)))
                    if self.comboBox_3.currentText() == 'см/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 3600, 8)))
                
                if self.comboBox_2.currentText() == 'см/мин':
                    if self.comboBox_3.currentText() == 'км/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000 * 60, 8)))
                    if self.comboBox_3.currentText() == 'км/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000, 8))) 
                    if self.comboBox_3.currentText() == 'км/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000 / 60, 8)))
                    if self.comboBox_3.currentText() == 'м/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100 * 60, 8))) 
                    if self.comboBox_3.currentText() == 'м/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100, 8)))
                    if self.comboBox_3.currentText() == 'м/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100 / 60, 8)))
                    if self.comboBox_3.currentText() == 'см/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 60, 8)))
                    if self.comboBox_3.currentText() == 'см/мин':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'см/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 60, 8)))

                if self.comboBox_2.currentText() == 'см/с':
                    if self.comboBox_3.currentText() == 'км/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000 * 3600, 8)))
                    if self.comboBox_3.currentText() == 'км/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000 * 60, 8))) 
                    if self.comboBox_3.currentText() == 'км/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000, 8)))
                    if self.comboBox_3.currentText() == 'м/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100 * 3600, 8))) 
                    if self.comboBox_3.currentText() == 'м/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100 * 60, 8)))
                    if self.comboBox_3.currentText() == 'м/с':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100, 8)))
                    if self.comboBox_3.currentText() == 'см/ч':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 3600, 8)))
                    if self.comboBox_3.currentText() == 'см/мин':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 60, 8)))
                    if self.comboBox_3.currentText() == 'см/с':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))

                # масса
                if self.comboBox_2.currentText() == 'кт':
                    if self.comboBox_3.currentText() == 'кт':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'т':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))
                    if self.comboBox_3.currentText() == 'ц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 10000, 8)))
                    if self.comboBox_3.currentText() == 'кг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000, 8)))
                    if self.comboBox_3.currentText() == 'г':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000000, 8)))
                    if self.comboBox_3.currentText() == 'мг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000000000, 8)))

                if self.comboBox_2.currentText() == 'т':
                    if self.comboBox_3.currentText() == 'кт':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000, 8)))
                    if self.comboBox_3.currentText() == 'т':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'ц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 10, 8)))
                    if self.comboBox_3.currentText() == 'кг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))
                    if self.comboBox_3.currentText() == 'г':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000, 8)))
                    if self.comboBox_3.currentText() == 'мг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000000, 8)))
                    
                if self.comboBox_2.currentText() == 'ц':
                    if self.comboBox_3.currentText() == 'кт':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 10000, 8)))
                    if self.comboBox_3.currentText() == 'т':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 10, 8)))
                    if self.comboBox_3.currentText() == 'ц':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'кг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100, 8)))
                    if self.comboBox_3.currentText() == 'г':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000, 8)))
                    if self.comboBox_3.currentText() == 'мг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000000, 8)))

                if self.comboBox_2.currentText() == 'кг':
                    if self.comboBox_3.currentText() == 'кт':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000000, 8)))
                    if self.comboBox_3.currentText() == 'т':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000, 8)))
                    if self.comboBox_3.currentText() == 'ц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100, 8)))
                    if self.comboBox_3.currentText() == 'кг':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'г':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))
                    if self.comboBox_3.currentText() == 'мг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000, 8)))

                if self.comboBox_2.currentText() == 'г':
                    if self.comboBox_3.currentText() == 'кт':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000000000, 8)))
                    if self.comboBox_3.currentText() == 'т':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000000, 8)))
                    if self.comboBox_3.currentText() == 'ц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000, 8)))
                    if self.comboBox_3.currentText() == 'кг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000, 8)))
                    if self.comboBox_3.currentText() == 'г':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'мг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))

                if self.comboBox_2.currentText() == 'мг':
                    if self.comboBox_3.currentText() == 'кт':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000000000000, 8)))
                    if self.comboBox_3.currentText() == 'т':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000000000, 8)))
                    if self.comboBox_3.currentText() == 'ц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 100000000, 8)))
                    if self.comboBox_3.currentText() == 'кг':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000000, 8)))
                    if self.comboBox_3.currentText() == 'г':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000, 8)))
                    if self.comboBox_3.currentText() == 'мг':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                
                # длина
                if self.comboBox_2.currentText() == 'км':
                    if self.comboBox_3.currentText() == 'км':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if  self.comboBox_3.currentText() == 'м':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))
                    if  self.comboBox_3.currentText() == 'дм':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 10000, 8)))
                    if  self.comboBox_3.currentText() == 'см':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100000, 8)))
                    if  self.comboBox_3.currentText() == 'мм':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000, 8)))

                if self.comboBox_2.currentText() == 'м':
                    if self.comboBox_3.currentText() == 'км':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.001, 8)))
                    if self.comboBox_3.currentText() == 'м':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'дм':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 10, 8)))
                    if self.comboBox_3.currentText() == 'см':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100, 8)))
                    if self.comboBox_3.currentText() == 'мм':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))

                if self.comboBox_2.currentText() == 'дм':
                    if self.comboBox_3.currentText() == 'км':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.0001, 15)))
                    if self.comboBox_3.currentText() == 'м':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.1, 15)))
                    if self.comboBox_3.currentText() == 'дм':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'см':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 10, 15)))
                    if self.comboBox_3.currentText() == 'мм':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 100, 15)))
                
                if self.comboBox_2.currentText() == 'см':
                    if self.comboBox_3.currentText() == 'км':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.00001, 15)))
                    if self.comboBox_3.currentText() == 'м':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.01, 15)))
                    if self.comboBox_3.currentText() == 'дм':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.1, 15)))
                    if self.comboBox_3.currentText() == 'см':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'мм':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 10, 15)))

                if self.comboBox_2.currentText() == 'мм':
                    if self.comboBox_3.currentText() == 'км':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000001, 15)))
                    if self.comboBox_3.currentText() == 'м':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.001, 15)))
                    if self.comboBox_3.currentText() == 'дм':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.01, 15)))
                    if self.comboBox_3.currentText() == 'см':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.1, 15)))
                    if self.comboBox_3.currentText() == 'мм':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                # ускорение
                if self.comboBox_2.currentText() == 'км/c^2':
                    if self.comboBox_3.currentText() == 'км/c^2':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'м/с^2':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))
                    if self.comboBox_3.currentText() == 'мм/с^2':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000, 8)))
                
                if self.comboBox_2.currentText() == 'м/с^2':
                    if self.comboBox_3.currentText() == 'км/c^2':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000, 8)))
                    if self.comboBox_3.currentText() == 'м/с^2':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'мм/с^2':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 8)))

                if self.comboBox_2.currentText() == 'мм/с^2':
                    if self.comboBox_3.currentText() == 'км/c^2':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000000, 8)))
                    if self.comboBox_3.currentText() == 'м/с^2':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) / 1000, 8)))
                    if self.comboBox_3.currentText() == 'мм/с^2':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                # время
                if self.comboBox_2.currentText() == 'Год(365 дней)':
                    if self.comboBox_3.currentText() == 'Год(365 дней)':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'Високосный год':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.997, 8)))
                    if self.comboBox_3.currentText() == 'Месяц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 12, 8)))
                    if self.comboBox_3.currentText() == 'Неделя':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 52.13, 8)))
                    if self.comboBox_3.currentText() == 'Сутки':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 364.91, 8)))
                    if self.comboBox_3.currentText() == 'Часы':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 8757.84, 8)))
                    if self.comboBox_3.currentText() == 'Минуты':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 525470.4, 8)))
                    if self.comboBox_3.currentText() == 'Секунды':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 31528224, 8)))

                if self.comboBox_2.currentText() == 'Високосный год':
                    if self.comboBox_3.currentText() == 'Год(365 дней)':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1.003, 8)))
                    if self.comboBox_3.currentText() == 'Високосный год':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'Месяц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 12, 8)))
                    if self.comboBox_3.currentText() == 'Неделя':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 52.299, 8)))
                    if self.comboBox_3.currentText() == 'Сутки':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 366.093, 8)))
                    if self.comboBox_3.currentText() == 'Часы':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 8786.232, 8)))
                    if self.comboBox_3.currentText() == 'Минуты':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 527173.92, 8)))
                    if self.comboBox_3.currentText() == 'Секунды':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 31630435.2, 8)))

                if self.comboBox_2.currentText() == 'Месяц':
                    if self.comboBox_3.currentText() == 'Год(365 дней)':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.08322, 8)))
                    if self.comboBox_3.currentText() == 'Високосный год':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.083, 8)))
                    if self.comboBox_3.currentText() == 'Месяц':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'Неделя':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 4.3397142, 8)))
                    if self.comboBox_3.currentText() == 'Сутки':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 30.37, 8)))
                    if self.comboBox_3.currentText() == 'Часы':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 729.0719, 8)))
                    if self.comboBox_3.currentText() == 'Минуты':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 43744.319, 8)))
                    if self.comboBox_3.currentText() == 'Секунды':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 2624659.19, 8)))

                if self.comboBox_2.currentText() == 'Неделя':
                    if self.comboBox_3.currentText() == 'Год(365 дней)':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.019178, 8)))
                    if self.comboBox_3.currentText() == 'Високосный год':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.01912, 8)))
                    if self.comboBox_3.currentText() == 'Месяц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.2299841, 8)))
                    if self.comboBox_3.currentText() == 'Неделя':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'Сутки':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 7, 8)))
                    if self.comboBox_3.currentText() == 'Часы':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 168, 8)))
                    if self.comboBox_3.currentText() == 'Минуты':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 10079.9, 8)))
                    if self.comboBox_3.currentText() == 'Секунды':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 604800, 8)))

                if self.comboBox_2.currentText() == 'Сутки':
                    if self.comboBox_3.currentText() == 'Год(365 дней)':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.002739, 15)))
                    if self.comboBox_3.currentText() == 'Високосный год':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.002732, 15)))
                    if self.comboBox_3.currentText() == 'Месяц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.032854, 15)))
                    if self.comboBox_3.currentText() == 'Неделя':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.14285714, 15)))
                    if self.comboBox_3.currentText() == 'Сутки':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'Часы':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 24, 15)))
                    if self.comboBox_3.currentText() == 'Минуты':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1440, 15)))
                    if self.comboBox_3.currentText() == 'Секунды':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 86400, 15)))

                if self.comboBox_2.currentText() == 'Часы':
                    if self.comboBox_3.currentText() == 'Год(365 дней)':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.0001141552, 15)))
                    if self.comboBox_3.currentText() == 'Високосный год':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.00011384, 15)))
                    if self.comboBox_3.currentText() == 'Месяц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.00136895, 15)))
                    if self.comboBox_3.currentText() == 'Неделя':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.00595238014, 15)))
                    if self.comboBox_3.currentText() == 'Сутки':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.0416, 15)))
                    if self.comboBox_3.currentText() == 'Часы':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'Минуты':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 60, 15)))
                    if self.comboBox_3.currentText() == 'Секунды':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 3600, 15)))

                if self.comboBox_2.currentText() == 'Минуты':
                    if self.comboBox_3.currentText() == 'Год(365 дней)':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.00000190, 15)))
                    if self.comboBox_3.currentText() == 'Високосный год':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.0000018, 15)))
                    if self.comboBox_3.currentText() == 'Месяц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000022, 15)))
                    if self.comboBox_3.currentText() == 'Неделя':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000099, 15)))
                    if self.comboBox_3.currentText() == 'Сутки':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000694, 15)))
                    if self.comboBox_3.currentText() == 'Часы':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.016, 15)))
                    if self.comboBox_3.currentText() == 'Минуты':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'Секунды':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 60, 15)))

                if self.comboBox_2.currentText() == 'Секунды':
                    if self.comboBox_3.currentText() == 'Год(365 дней)':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.00000003, 15)))
                    if self.comboBox_3.currentText() == 'Високосный год':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.0000000316, 15)))
                    if self.comboBox_3.currentText() == 'Месяц':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.00000038, 15)))
                    if self.comboBox_3.currentText() == 'Неделя':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.00001, 15)))
                    if self.comboBox_3.currentText() == 'Сутки':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000694, 15)))
                    if self.comboBox_3.currentText() == 'Часы':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.00027, 15)))
                    if self.comboBox_3.currentText() == 'Минуты':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.016, 15)))
                    if self.comboBox_3.currentText() == 'Секунды':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))

                # сила
                if self.comboBox_2.currentText() == 'МН':
                    if self.comboBox_3.currentText() == 'МН':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'кН':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 15)))
                    if self.comboBox_3.currentText() == 'Н':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000, 15)))
                    if self.comboBox_3.currentText() == 'мН':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000000, 15)))

                if self.comboBox_2.currentText() == 'кН':
                    if self.comboBox_3.currentText() == 'МН':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.001, 15)))
                    if self.comboBox_3.currentText() == 'кН':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'Н':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 15)))
                    if self.comboBox_3.currentText() == 'мН':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000, 15)))

                if self.comboBox_2.currentText() == 'Н':
                    if self.comboBox_3.currentText() == 'МН':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000001, 15)))
                    if self.comboBox_3.currentText() == 'кН':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.001, 15)))
                    if self.comboBox_3.currentText() == 'Н':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'мН':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 15)))

                if self.comboBox_2.currentText() == 'мН':
                    if self.comboBox_3.currentText() == 'МН':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000000001, 15)))
                    if self.comboBox_3.currentText() == 'кН':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000001, 15)))
                    if self.comboBox_3.currentText() == 'Н':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.001, 15)))
                    if self.comboBox_3.currentText() == 'мН':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))

                # объем
                if self.comboBox_2.currentText() == 'км^3':
                    if self.comboBox_3.currentText() == 'км^3':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'м^3':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000000, 25)))
                    if self.comboBox_3.currentText() == 'см^3':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000000000000, 25)))
                    if self.comboBox_3.currentText() == 'литр':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000000000, 25)))

                if self.comboBox_2.currentText() == 'м^3':
                    if self.comboBox_3.currentText() == 'км^3':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000000001, 25)))
                    if self.comboBox_3.currentText() == 'м^3':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'см^3':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000000, 25)))
                    if self.comboBox_3.currentText() == 'литр':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 25)))

                if self.comboBox_2.currentText() == 'см^3':
                    if self.comboBox_3.currentText() == 'км^3':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000000000000001, 25)))
                    if self.comboBox_3.currentText() == 'м^3':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000001, 25)))
                    if self.comboBox_3.currentText() == 'см^3':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))
                    if self.comboBox_3.currentText() == 'литр':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.001, 25)))

                if self.comboBox_2.currentText() == 'литр':
                    if self.comboBox_3.currentText() == 'км^3':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.000000000001, 25)))
                    if self.comboBox_3.currentText() == 'м^3':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 0.001, 25)))
                    if self.comboBox_3.currentText() == 'см^3':
                        self.lineEdit_2.setText(str(round(int(self.lineEdit.text()) * 1000, 25)))
                    if self.comboBox_3.currentText() == 'литр':
                        self.lineEdit_2.setText(str((int(self.lineEdit.text()))))

    def make(self, text): 
        if text == '------': 
            self.comboBox_2.clear() 
            self.comboBox_3.clear()
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.label_6.setText('')
        
        if text == 'Время':
            self.comboBox_2.clear() 
            list_for_time = ['Год(365 дней)', 'Високосный год', 'Месяц', 'Неделя', 'Сутки', 'Часы', 'Минуты', 'Секунды']
            self.comboBox_2.addItems(list_for_time) 
            self.comboBox_3.clear() 
            self.comboBox_3.addItems(list_for_time)
            self.label_6.setText('Время - мера длительности существования всех объектов.\nНеобратимое течение (протекающее лишь в\nодном направлении — из прошлого через настоящее\nв будущее).')
 
        if text == 'Скорость': 
            self.comboBox_2.clear() 
            list_for_speed = ['км/ч', 'км/мин', 'км/с', 'м/ч', 'м/мин', 'м/с', 'см/ч', 'см/мин', 'см/с']
            self.comboBox_2.addItems(list_for_speed) 
            self.comboBox_3.clear() 
            self.comboBox_3.addItems(list_for_speed)
            self.label_6.setText('Скорость– это физическая величина, показывающая,\nкакой путь проходит тело за единицу времени.')     

        if text == 'Масса': 
            self.comboBox_2.clear() 
            list_for_weight = ['кт', 'т', 'ц', 'кг', 'г', 'мг'] 
            self.comboBox_2.addItems(list_for_weight) 
            self.comboBox_3.clear() 
            self.comboBox_3.addItems(list_for_weight)
            self.label_6.setText('Масса — физическая величина, определяющая инерционные\nи гравитационные свойства тела.')

        if text == 'Длина': 
            self.comboBox_2.clear() 
            self.list_for_length = ['км', 'м', 'дм','см', 'мм']
            self.list_for_length_2 = ['км', 'м', 'дм','см', 'мм']
            self.comboBox_2.addItems(self.list_for_length) 
            self.comboBox_3.clear() 
            self.comboBox_3.addItems(self.list_for_length_2)
            self.label_6.setText('Длина — физическая величина, числовая характеристика\nпротяжённости линий.')
        
        if text == 'Ускорение':
            self.comboBox_2.clear() 
            self.list_for_acceleration = ['км/c^2', 'м/с^2', 'мм/с^2']
            self.list_for_acceleration_2 = ['км/c^2', 'м/с^2', 'мм/с^2']
            self.comboBox_2.addItems(self.list_for_acceleration) 
            self.comboBox_3.clear() 
            self.comboBox_3.addItems(self.list_for_acceleration_2)
            self.label_6.setText('Ускорение — физическая величина, определяющая быстроту\nизменения скорости тела, то есть первая производная\nот скорости по времени.')

        if text == 'Сила':
            self.comboBox_2.clear() 
            self.list_for_strange = ['МН', 'кН', 'Н', 'мН']
            self.comboBox_2.addItems(self.list_for_strange) 
            self.comboBox_3.clear() 
            self.comboBox_3.addItems(self.list_for_strange)
            self.label_6.setText('Сила — физическая векторная величина, являющаяся мерой\nвоздействия на данное тело со стороны других тел\nили полей')

        if text == 'Объем':
            self.comboBox_2.clear() 
            self.list_for_volume = ['км^3', 'м^3', 'см^3', 'литр']
            self.comboBox_2.addItems(self.list_for_volume) 
            self.comboBox_3.clear() 
            self.comboBox_3.addItems(self.list_for_volume)
            self.label_6.setText('Объём — количественная характеристика пространства,\nзанимаемого телом или веществом. Объём тела\nопределяется его формой и линейными размерами.')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())