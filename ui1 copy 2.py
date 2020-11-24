# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\新建文件夹\顺序进程\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):

                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1300, 618)
                font = QtGui.QFont()
                font.setFamily("Arial")
                MainWindow.setFont(font)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(910, 380, 76, 41))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                self.pushButton.setFont(font)
                self.pushButton.setObjectName("pushButton")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(600, 70, 41, 41))
                self.label.setStyleSheet("background-color: #4EEE94;\n"
        "border-radius:20px;")
                self.label.setText("P1")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(600, 150, 41, 41))
                self.label_2.setStyleSheet("background-color: rgb(26, 183, 255);\n"
        "border-radius:20px;")
                self.label_2.setText("P2")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(600, 230, 41, 41))
                self.label_3.setStyleSheet("background-color: #6A5ACD;\n"
        "border-radius:20px;")
                self.label_3.setText("P3")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(600, 310, 41, 41))
                self.label_4.setStyleSheet("background-color: rgb(255, 25, 163);\n"
        "border-radius:20px;")
                self.label_4.setText("P4")
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(760, 60, 16, 321))
                self.label_5.setStyleSheet("background-color: rgb(170, 170, 127);")
                self.label_5.setText("")
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(990, 130, 151, 171))
                self.label_6.setStyleSheet("image: url(cpu.png);")
                self.label_6.setText("")
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(420, 40, 61, 31))
                font = QtGui.QFont()
                font.setFamily("Geneva")
                font.setPointSize(12)
                self.label_7.setFont(font)
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(420, 90, 31, 31))
                self.label_8.setStyleSheet("image: url(:/newPrefix/1.png);")
                self.label_8.setText("")
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(420, 170, 31, 31))
                self.label_9.setStyleSheet("image: url(:/newPrefix/2.png);")
                self.label_9.setText("")
                self.label_9.setObjectName("label_9")
                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(420, 250, 31, 31))
                self.label_10.setStyleSheet("\n"
        "image: url(:/newPrefix/3.png);")
                self.label_10.setText("")
                self.label_10.setObjectName("label_10")
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(420, 330, 31, 31))
                self.label_11.setStyleSheet("image: url(:/newPrefix/4.png);")
                self.label_11.setText("")
                self.label_11.setObjectName("label_11")
                self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_close.setGeometry(QtCore.QRect(1130, 20, 21, 21))
                self.pushButton_close.setText("")
                self.pushButton_close.setObjectName("pushButton_close")
                self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4.setGeometry(QtCore.QRect(990, 380, 76, 41))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                self.pushButton_4.setFont(font)
                self.pushButton_4.setObjectName("pushButton_4")
                MainWindow.setCentralWidget(self.centralwidget)
        
                #self.tableView = QtWidgets.QTableView(self.centralwidget)
                #self.tableView.setGeometry(QtCore.QRect(750, 100, 300, 192))
                #self.tableView.setObjectName("tableView")

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Process Simulation"))             
                #self.label_7.setText(_translate("MainWindow", ""))        
                self.pushButton.setText(_translate("MainWindow", "Start"))   
                self.pushButton_4.setText(_translate("MainWindow", "Reset"))

                MainWindow.setWindowOpacity(0.96)         
                MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                pe = QPalette()
                MainWindow.setAutoFillBackground(True)
                MainWindow.setPalette(pe)

                