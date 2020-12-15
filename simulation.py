import os, sys, time
import subprocess, threading
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPen
from PyQt5.QtCore import *
# from PyQt5 import *
from ui import *
from PyQt5.QtWidgets import *

headers = ["Process", "Turnaround", "Avg. Wait-Time"]
data = [("P1", "12", "45"),
        ("P2", "13", "23"),
        ("P3", "23", "34"),
        ("P4", "21", "98"),
        ("P5", "34", "56")]


class WorkerSignals(QObject):
    progress = pyqtSignal(int)

class Worker(QRunnable):
    def __init__(self):
        super(Worker, self).__init__()
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        total_n = 1000
        for n in range(total_n):
            progress_pc = int(100 * float(n) / total_n)
            self.signals.progress.emit(progress_pc)
            time.sleep(0.001)

class mywindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.thread1 = threading.Thread(target=self.label_move)
        self.thread2 = threading.Thread(target=self.label2_move)
        self.thread3 = threading.Thread(target=self.label3_move)
        self.thread4 = threading.Thread(target=self.label4_move)

        self.flag = False
        self.timeForEachProcess = [5, 6, 6, 1, 4]

        self.pushButton.clicked.connect(self.start_threads)
        self.pushButton_4.pressed.connect(self.restart)

        self.trueSequence = [0, 1, 2, 3, 4]
        self.trueBurstTime = [5, 6, 6, 1, 4]

        self.color = [(255, 64, 0), (255, 128, 0), (255, 191, 0),
                      (255, 255, 0), (128, 255, 0), (0, 255, 191),
                      (0, 191, 255), (0, 128, 255), (128, 0, 255), (255, 0, 255)]

        self.btnRun.clicked.connect(self.action_chart)

        model = TableModel()
        self.tableView.setModel(model)

        self.threadPool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadPool.maxThreadCount())

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    '''dynamic lines'''
    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        v_width_fixed = 560
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

            i += 1

        qp.setPen(pen)
        qp.drawLine(800, 185, 560, 185)
        qp.setPen(pen)
        qp.drawLine(800, 235, 560, 235)

    def action_chart(self):
        self.flag = True
        worker = Worker()
        worker.signals.progress.connect(self.draw_chart)
        self.threadPool.start(worker)

        print(self.bt1_1.value()) #burst
        print(self.at_1.value()) #arrival
        print(self.checkBox_1.isChecked()) #is checked?

    def update_progress(self,  painter, chartrect, pname, tail, txtpos):
        painter.drawRect(chartrect)
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('black'))
        painter.setPen(pen)
        painter.drawText(tail, txtpos, pname)
        self.update()

    def draw_chart(self, progress):
        if self.flag:
            painter = QtGui.QPainter(self.labelchart.pixmap())
            mapColor = {}
            uniqueTrueSequence = set(self.trueSequence)
            colorIndex = 0

        for i in uniqueTrueSequence:
            mapColor[i] = colorIndex
            colorIndex += 1

        #Color bars
        tailPos = 10
        j = 0
        for i, k in zip(self.trueBurstTime, self.trueSequence):
            r = self.color[mapColor[k]][0]
            g = self.color[mapColor[k]][1]
            b = self.color[mapColor[k]][2]
            print(r,g,b)
            painter.setBrush(QColor(r, g, b))

            # Process label
            p = "P" + str(self.trueSequence[j])
            chartRect = QRect(tailPos, 30, i+progress + 15,  30)


            self.update_progress( painter, chartRect, p, tailPos, i + 45 )

            tailPos += i * 20
            j += 1

        # Ruler
        rulerPos = 10
        sumTime = sum(self.timeForEachProcess)
        for i in range(sumTime + 1):
            painter.setBrush(QColor(0, 0, 0))
            painter.drawRect(rulerPos, 77, 1, 10)
            pen = QtGui.QPen()
            pen.setWidth(1)
            pen.setColor(QtGui.QColor('black'))
            painter.setPen(pen)
            painter.drawText(rulerPos, 75, str(i))
            rulerPos += 21
            if i == 61:
                 break
        self.update()

    # painter.drawRect(30, 262.5 + letsMovetogether, sumTime * 30, 1)
        painter.end()

    def run(self):
        self.flag = True
        self.update()

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

            self.action_chart()

    def suspend_threads(self):
        for i in range(1, 5):
            self.thread_suspend(eval("self.thread" + str(i)))

    def resume_threads(self):
        for i in range(1, 5):
            self.thread_resume(eval("self.thread" + str(i)))

    def label_move(self):
        for i in range(350, 380, 10):
            self.thread1.suspended.wait()
            self.label.move(i, 70)
            time.sleep(0.18)
        self.thread_suspend(self.thread1)
        self.label.setGeometry(QtCore.QRect(600, 190, 41, 41))

    def label2_move(self):
        for i in range(350, 380, 5):
            self.thread2.suspended.wait()
            self.label_2.move(i, 150)
            time.sleep(0.28)
        self.thread_suspend(self.thread2)
        self.label_2.setGeometry(QtCore.QRect(560, 190, 41, 41))
        self.InStack()

    def label3_move(self):
        for i in range(350, 380, 5):
            self.thread3.suspended.wait()
            self.label_3.move(i, 230)
            time.sleep(0.25)
        self.thread_suspend(self.thread3)
        self.label_3.setGeometry(QtCore.QRect(520, 190, 41, 41))

    def label4_move(self):
        for i in range(350, 380, 5):
            self.thread4.suspended.wait()
            self.label_4.move(i, 310)
            time.sleep(0.20)
        self.thread_suspend(self.thread4)
        self.label_4.setGeometry(QtCore.QRect(480, 190, 41, 41))

    def thread_suspend(self, thread):
        if not thread.suspended.is_set():
            return
        thread.suspended.clear()

    def thread_resume(self, thread):
        if thread.suspended.is_set():
            return
        thread.suspended.set()

    def update_position(self):
        for i in range(350, 380, 10):
            self.thread_chart.suspended.wait()
            # self.chartRect.translate(i)
            time.sleep(0.20)
        self.thread_suspend(self.thread_chart)


    def chartStack(self):
        i = 480
        while i <= 780:
            newp = QPoint(i, 530)
            self.chartRect.moveTo(newp)
            self.chartRect.translate(i)
            i += 10
            time.sleep(0.3)

    def InStack(self):
        i1, i4, i3, i2 = 600, 560, 520, 480
        while i2 <= 780:
            if i1 > 780:
                self.label.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label.setText("")
            if i2 >= 780:
                self.label_2.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_2.setText("")
            if i3 > 780:
                self.label_3.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_3.setText("")
            if i4 > 780:
                self.label_4.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_4.setText("")
            self.label.move(i1, 190)
            self.label_2.move(i2, 190)
            self.label_3.move(i3, 190)
            self.label_4.move(i4, 190)
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
