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
                MainWindow.resize(950, 800)
                font = QtGui.QFont()
                font.setFamily("Arial")
                MainWindow.setFont(font)                       
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                                              
                self.bt1_1 = QtWidgets.QSpinBox(self.centralwidget)
                self.bt1_1.setEnabled(True)
                self.bt1_1.setGeometry(QtCore.QRect(270, 100, 48, 26))
                self.bt1_1.setMaximum(999)
                self.bt1_1.setObjectName("bt1_1")
                self.bt1_1.setValue(1)

                self.at_1 = QtWidgets.QSpinBox(self.centralwidget)
                self.at_1.setGeometry(QtCore.QRect(200, 100, 48, 26))
                self.at_1.setMaximum(999)
                self.at_1.setObjectName("at_1")
                self.at_1.setValue(0)
              
                self.bt1_2 = QtWidgets.QSpinBox(self.centralwidget)
                self.bt1_2.setEnabled(True)
                self.bt1_2.setGeometry(QtCore.QRect(270, 150, 48, 26))
                self.bt1_2.setMaximum(999)
                self.bt1_2.setObjectName("bt1_2")
                self.bt1_2.setValue(2)
                                
                self.at_2 = QtWidgets.QSpinBox(self.centralwidget)
                self.at_2.setGeometry(QtCore.QRect(200, 150, 48, 26))
                self.at_2.setMaximum(999)
                self.at_2.setObjectName("at_2")
                self.at_2.setValue(2)

                self.at_3 = QtWidgets.QSpinBox(self.centralwidget)
                self.at_3.setGeometry(QtCore.QRect(200, 200, 48, 26))
                self.at_3.setMaximum(999)
                self.at_3.setObjectName("at_3")
                self.at_3.setValue(3)

                self.bt1_3 = QtWidgets.QSpinBox(self.centralwidget)
                self.bt1_3.setEnabled(True)
                self.bt1_3.setGeometry(QtCore.QRect(270, 200, 48, 26))
                self.bt1_3.setMaximum(999)
                self.bt1_3.setObjectName("bt1_3")
                self.bt1_3.setValue(3)
                                                           
                self.at_4 = QtWidgets.QSpinBox(self.centralwidget)
                self.at_4.setGeometry(QtCore.QRect(200, 250, 48, 26))
                self.at_4.setMaximum(999)
                self.at_4.setObjectName("at_4")
                self.at_4.setValue(4)

                self.at_5 = QtWidgets.QSpinBox(self.centralwidget)
                self.at_5.setEnabled(True)
                self.at_5.setGeometry(QtCore.QRect(200, 300, 48, 26))
                self.at_5.setMaximum(999)
                self.at_5.setObjectName("at_5")
                self.at_5.setValue(5)
                                
                self.bt1_4 = QtWidgets.QSpinBox(self.centralwidget)
                self.bt1_4.setEnabled(True)
                self.bt1_4.setGeometry(QtCore.QRect(270, 250, 48, 26))
                self.bt1_4.setMaximum(999)
                self.bt1_4.setObjectName("bt1_4")
                self.bt1_4.setValue(4)
               
                self.bt1_5 = QtWidgets.QSpinBox(self.centralwidget)
                self.bt1_5.setEnabled(True)
                self.bt1_5.setGeometry(QtCore.QRect(270, 300, 48, 26))
                self.bt1_5.setMaximum(999)
                self.bt1_5.setObjectName("bt1_5")
                self.bt1_5.setValue(5)
                              
                self.label_arr = QtWidgets.QLabel(self.centralwidget)
                self.label_arr.setGeometry(QtCore.QRect(200, 60, 51, 31))
                self.label_arr.setAlignment(QtCore.Qt.AlignCenter)
                self.label_arr.setObjectName("label_arr")

                self.label_cpu_burst = QtWidgets.QLabel(self.centralwidget)
                self.label_cpu_burst.setGeometry(QtCore.QRect(270, 60, 51, 31))
                self.label_cpu_burst.setAlignment(QtCore.Qt.AlignCenter)
                self.label_cpu_burst.setObjectName("label_cpu_burst")

                self.prsId1 = QtWidgets.QLabel(self.centralwidget)
                self.prsId1.setGeometry(QtCore.QRect(110, 100, 71, 25))
                self.prsId1.setFont(font)
                
                self.prsId1.setObjectName("prsId1")
                self.prsId2 = QtWidgets.QLabel(self.centralwidget)
                self.prsId2.setGeometry(QtCore.QRect(110, 150, 71, 25))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.prsId2.setFont(font)
                
                self.prsId2.setObjectName("prsId2")
                self.prsId3 = QtWidgets.QLabel(self.centralwidget)
                self.prsId3.setGeometry(QtCore.QRect(110, 200, 71, 25))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.prsId3.setFont(font)
                
                self.prsId3.setObjectName("prsId3")
                self.prsId4 = QtWidgets.QLabel(self.centralwidget)
                self.prsId4.setGeometry(QtCore.QRect(110, 250, 71, 25))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.prsId4.setFont(font)
                self.prsId4.setObjectName("prsId4")

                self.prsId5 = QtWidgets.QLabel(self.centralwidget)
                self.prsId5.setEnabled(True)
                self.prsId5.setGeometry(QtCore.QRect(110, 300, 71, 25))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.prsId5.setFont(font)
                self.prsId5.setObjectName("prsId5")

                self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
                self.checkBox_1.setEnabled(True)
                self.checkBox_1.setChecked(True)
                self.checkBox_1.setGeometry(QtCore.QRect(70, 100, 41, 23))
                self.checkBox_1.setTabletTracking(False)
                self.checkBox_1.setText("")

                self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
                self.checkBox_2.setEnabled(True)
                self.checkBox_2.setCheckable(True)
                self.checkBox_2.setGeometry(QtCore.QRect(70, 150, 41, 23))
                self.checkBox_2.setTabletTracking(False)
                self.checkBox_2.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("ui/green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.checkBox_2.setIcon(icon1)
                self.checkBox_2.setCheckable(True)
                self.checkBox_2.setChecked(True)
                self.checkBox_2.setObjectName("checkBox_2")
                self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
                self.checkBox_3.setEnabled(True)
                self.checkBox_3.setGeometry(QtCore.QRect(70, 200, 41, 23))
                self.checkBox_3.setTabletTracking(False)
                self.checkBox_3.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("ui/blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.checkBox_3.setIcon(icon2)
                self.checkBox_3.setCheckable(True)
                self.checkBox_3.setChecked(True)
                self.checkBox_3.setObjectName("checkBox_3")
                self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
                self.checkBox_4.setEnabled(True)
                self.checkBox_4.setGeometry(QtCore.QRect(70, 250, 41, 23))
                self.checkBox_4.setTabletTracking(False)
                self.checkBox_4.setText("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("ui/yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.checkBox_4.setIcon(icon3)
                self.checkBox_4.setCheckable(True)
                self.checkBox_4.setChecked(True)
                self.checkBox_4.setObjectName("checkBox_4")
                self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
                self.checkBox_5.setEnabled(True)
                self.checkBox_5.setGeometry(QtCore.QRect(70, 300, 41, 23))
                self.checkBox_5.setTabletTracking(False)
                self.checkBox_5.setText("")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("ui/orange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.checkBox_5.setIcon(icon4)
                self.checkBox_5.setCheckable(True)
                self.checkBox_5.setChecked(True)
                self.checkBox_5.setObjectName("checkBox_5")

                self.fcfs = QtWidgets.QPushButton(self.centralwidget)
                self.fcfs.setGeometry(QtCore.QRect(10, 10, 61, 25))
                self.fcfs.setObjectName("fcfs_b")

                self.preemptive = QtWidgets.QPushButton(self.centralwidget)
                self.preemptive.setGeometry(QtCore.QRect(80, 10, 140, 25))
                self.preemptive.setObjectName("preemptive")

                self.reset = QtWidgets.QPushButton(self.centralwidget)
                self.reset.setGeometry(QtCore.QRect(220, 10, 80, 25))
                self.reset.setObjectName("reset")

                #self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
                #self.pushButton_4.setGeometry(QtCore.QRect(220, 10, 76, 41))
                #self.pushButton_4.setObjectName("pushButton_4")


                #simulation side
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(350, 70, 41, 41))
                self.label.setStyleSheet("background-color: rgb(255, 64, 0);\n"
        "border-radius:20px;")
                self.label.setText("P1")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(350, 150, 41, 41))
                self.label_2.setStyleSheet("background-color: rgb(255, 128, 0);\n"
        "border-radius:20px;")
                self.label_2.setText("P2")
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(350, 230, 41, 41))
                self.label_3.setStyleSheet("background-color: rgb(255, 191, 0);\n"
        "border-radius:20px;")
                self.label_3.setText("P3")
                self.label_3.setObjectName("label_3")
                self.label_3.setAlignment(QtCore.Qt.AlignCenter)
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(350, 310, 41, 41))
                self.label_4.setStyleSheet("background-color: rgb(255, 255, 0);\n"
        "border-radius:20px;")
                self.label_4.setText("P4")
                self.label_4.setObjectName("label_4")
                self.label_4.setAlignment(QtCore.Qt.AlignCenter)

                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(350, 390, 41, 41))
                self.label_5.setStyleSheet("background-color: rgb(128, 255, 0);\n"
                                           "border-radius:20px;")
                self.label_5.setText("P5")
                self.label_5.setObjectName("label_5")
                self.label_5.setAlignment(QtCore.Qt.AlignCenter)

                #the bridge
                self.label_51 = QtWidgets.QLabel(self.centralwidget)
                self.label_51.setGeometry(QtCore.QRect(560, 60, 16, 375))
                self.label_51.setStyleSheet("background-color: rgb(170, 170, 127);")
                self.label_51.setText("")
                self.label_51.setObjectName("label_51")

                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(780, 130, 151, 171))
                self.label_6.setStyleSheet("image: url(cpu.png);")
                self.label_6.setText("")
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(420, 40, 61, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
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

                #self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                #self.pushButton.setGeometry(QtCore.QRect(30, 380, 76, 41))
                #font = QtGui.QFont()
                #font.setFamily("Arial")
                #font.setPointSize(10)
                #self.pushButton.setFont(font)
                #self.pushButton.setObjectName("pushButton")
               

                MainWindow.setCentralWidget(self.centralwidget)
        
                self.tableView = QtWidgets.QTableView(self.centralwidget)
                self.tableView.setGeometry(QtCore.QRect(30, 580, 307, 178))
                self.tableView.setObjectName("tableView")

                self.labelchart = QtWidgets.QLabel(self.centralwidget)
                self.labelchart.setGeometry(QtCore.QRect(30, 470, 800, 100))
                canvas = QtGui.QPixmap(800, 100)
                self.labelchart.setPixmap(canvas)

                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Process Simulation - Group 1"))
                #self.pushButton.setText(_translate("MainWindow", "Start"))
                self.reset.setText(_translate("MainWindow", "Reset"))
                self.label_arr.setText(_translate("MainWindow", "Arrival\n"
                                                    "time"))
                self.label_cpu_burst.setText(_translate("MainWindow", "CPU\n"
                                                      "burst"))

                self.prsId1.setText(_translate("MainWindow", "P1"))
                self.prsId2.setText(_translate("MainWindow", "P2"))
                self.prsId3.setText(_translate("MainWindow", "P3"))
                self.prsId4.setText(_translate("MainWindow", "P4"))
                self.prsId5.setText(_translate("MainWindow", "P5"))
                self.fcfs.setText(_translate("MainWindow", "FCFS"))
                self.preemptive.setText(_translate("MainWindow", "Preemptive Priority"))
                #self.labelchart.setText(_translate("MainWindow", "but butt"))



                MainWindow.setWindowOpacity(0.96)         
                #MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                #pe = QPalette()
                MainWindow.setAutoFillBackground(True)
                #MainWindow.setPalette(pe)

                