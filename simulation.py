import os, sys, time
import subprocess,threading
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPainter,QBrush,QPen
from PyQt5.QtCore import *
from PyQt5 import *
from ui1 import *
from PyQt5.QtWidgets import * 



from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


headers = ["Process", "Turnaround", "Avg. Wait-Time"]
data =    [("P1", "12", "45"),
           ("P2", "13", "23"),
           ("P3", "23", "34"),
           ("P4", "21", "98"),
           ("P5", "34", "56")]

button_style = ''' 
                     QPushButton
                     {text-align : center;
                     background-color : white;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 20px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 16px;}

                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 18px;
                     padding: 16px;
                     height : 14px;
                     border-style: outset;
                     font : 14px;}

                     QPushButton:hover
                     {
                     background:#C0C0C0;}
                     '''


class mywindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.setStyleSheet(button_style)
                
        self.pushButton_4.setStyleSheet(button_style)
        

        self.thread1 = threading.Thread(target=self.label_move)
        self.thread2 = threading.Thread(target=self.label2_move)
        self.thread3 = threading.Thread(target=self.label3_move)
        self.thread4 = threading.Thread(target=self.label4_move)
        self.pushButton.clicked.connect(self.start_threads)                
        self.pushButton_4.clicked.connect(self.restart)        
                
        model = TableModel()      
        self.tableView.setModel(model)
            

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
             
    '''dynamic now'''         
    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        
        v_width_fixed=560
        x_fixed = 345
        y_axis_and_heigth_1 = 65
        y_axis_and_heigth_2 = 115
        for i in range(5):
            qp.setPen(pen)
            qp.drawLine(x_fixed, y_axis_and_heigth_1, v_width_fixed, y_axis_and_heigth_1)
            qp.setPen(pen)
            qp.drawLine(x_fixed, y_axis_and_heigth_2, v_width_fixed, y_axis_and_heigth_2)
            qp.setPen(pen)
            qp.drawLine(x_fixed, y_axis_and_heigth_1, x_fixed, y_axis_and_heigth_2)

            y_axis_and_heigth_1 = y_axis_and_heigth_1 + 80
            y_axis_and_heigth_2 = y_axis_and_heigth_2 + 80

            i+=1

        qp.setPen(pen)
        qp.drawLine(800, 185, 560, 185)
        qp.setPen(pen)
        qp.drawLine(800, 235, 560, 235)

    def start_threads(self):
        self.pushButton.hide()
        print("Threads num: {}".format(threading.activeCount()))
        if threading.activeCount() >= 2:
            pass
        else:
            self.thread1.suspended = threading.Event()
            self.thread1.suspended.set()
            self.thread2.suspended = threading.Event()
            self.thread2.suspended.set()
            self.thread3.suspended = threading.Event()
            self.thread3.suspended.set()
            self.thread4.suspended = threading.Event()
            self.thread4.suspended.set()
            self.thread1.start()
            self.thread2.start()
            self.thread3.start()
            self.thread4.start()

    def suspend_threads(self):
        for i in range(1,5):
            self.thread_suspend(eval("self.thread" + str(i)))

    def resume_threads(self):
        for i in range(1,5):
            self.thread_resume(eval("self.thread" + str(i)))

    def label_move(self): 
        for i in range(350,380,10):
            self.thread1.suspended.wait()
            self.label.move(i,70)
            time.sleep(0.18)
        self.thread_suspend(self.thread1)
        self.label.setGeometry(QtCore.QRect(600, 190, 41, 41))
        
    
    def label2_move(self):
        for i in range(350,380,5):
            self.thread2.suspended.wait()
            self.label_2.move(i,150)
            time.sleep(0.28)
        self.thread_suspend(self.thread2)
        self.label_2.setGeometry(QtCore.QRect(560, 190, 41, 41))
        self.InStack()
        
    def label3_move(self):
        for i in range(350,380,5):
            self.thread3.suspended.wait()
            self.label_3.move(i,230)            
            time.sleep(0.25)
        self.thread_suspend(self.thread3)
        self.label_3.setGeometry(QtCore.QRect(520, 190, 41, 41))
    
    def label4_move(self):
        for i in range(350,380,5):
            self.thread4.suspended.wait()
            self.label_4.move(i,310)
            time.sleep(0.20)
        self.thread_suspend(self.thread4)
        self.label_4.setGeometry(QtCore.QRect(480, 190, 41, 41))

    def thread_suspend(self,thread):
        if not thread.suspended.is_set():
            return
        thread.suspended.clear()
    
    def thread_resume(self,thread):
        if thread.suspended.is_set():
            return
        thread.suspended.set()

    #1,4,3,2el
    def InStack(self):
        i1, i4, i3, i2 = 600, 560, 520, 480 
        while i2 <= 780 :
            if i1>780:
                self.label.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label.setText("")
            if i2>=780:
                self.label_2.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_2.setText("")
            if i3>780:
                self.label_3.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_3.setText("")
            if i4>780:
                self.label_4.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_4.setText("")
            self.label.move(i1,190)
            self.label_2.move(i2,190)
            self.label_3.move(i3,190)
            self.label_4.move(i4,190)
            i1 += 10
            i2 += 10
            i3 += 10
            i4 += 10
            time.sleep(0.3)
    
    def restart(self):
        os.system("python simulation.py")
        self.close()

class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        # How many rows are there?
        return len(data)
    def columnCount(self, parent):
        # How many columns?
        return len(headers)
    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        # What's the value of the cell at the given index?
        return data[index.row()][index.column()]
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        # What's the header for the given column?
        return headers[section]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()    
    sys.exit(app.exec_())
