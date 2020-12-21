import os, sys, time
import subprocess, threading
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPen
from PyQt5.QtCore import *
# from PyQt5 import *
from ui import *
from PyQt5.QtWidgets import *
import cpu_sched

#pending todo : hook up the other algo.
headers = ["Process", "Turnaround", "Wait-Time"]

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
            time.sleep(0.01)

class mywindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.thread1 = threading.Thread(target=self.label_move)
        self.thread2 = threading.Thread(target=self.label2_move)
        self.thread3 = threading.Thread(target=self.label3_move)
        self.thread4 = threading.Thread(target=self.label4_move)
        self.thread5 = threading.Thread(target=self.label_5)

        self.flag = False

        #self.pushButton.clicked.connect(self.start_threads)
        self.reset.pressed.connect(self.restart)
        self.fcfs.clicked.connect(self.start_threads)

        self.timeForEachProcess = None  #[5, 6, 6, 1, 4]
        self.trueSequence = None #[1, 2, 3, 4, 5]
        self.trueBurstTime = None #[5, 6, 6, 1, 4]

        self.color = [(255, 64, 0), (255, 128, 0), (255, 191, 0),
                      (255, 255, 0), (128, 255, 0)]

        self.threadPool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadPool.maxThreadCount())

        self.algo = None

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

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
        if self.flag is True:
            worker = Worker()
            worker.signals.progress.connect(self.draw_chart)
            self.threadPool.start(worker)

    def update_progress(self, painter, chartrect, pname, tail, txtpos):
        painter.drawRect(chartrect)
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('black'))
        painter.setPen(pen)
        painter.drawText(tail, txtpos, pname)
        self.update()

    def draw_chart(self, progress):

        self.timeForEachProcess = self.algo.tat  # [5, 6, 6, 1, 4]
        self.trueSequence = [1, 2, 3, 4, 5]
        self.trueBurstTime = self.algo.tat  # [5, 6, 6, 1, 4]
        if self.flag:
            painter = QtGui.QPainter(self.labelchart.pixmap())
            mapColor = {}
            uniqueTrueSequence = set(self.trueSequence)
            colorIndex = 0

        for i in uniqueTrueSequence:
            mapColor[i] = colorIndex
            colorIndex += 1

        # color bars. todo : need to draw additional bar for 0-arrival time interval
        tailPos_by_arrival = self.algo.arrival_time[0] * 20
        tailPos = 10 + tailPos_by_arrival
        j = 0
        for i, k in zip(self.trueBurstTime, self.trueSequence):
            r = self.color[mapColor[k]][0]
            g = self.color[mapColor[k]][1]
            b = self.color[mapColor[k]][2]
            painter.setBrush(QColor(r, g, b))

            # Process label
            p = "P" + str(self.trueSequence[j])
            chartRect = QRect(tailPos, 30, i + progress + 15, 30)
            self.update_progress(painter, chartRect, p, tailPos, i + 45)
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
        painter.end()

    def start_threads(self):
        print("Threads num: {}".format(threading.activeCount()))
        if threading.activeCount() >= 2:
            pass
        else:
            # validation
            if self.checkBox_1.isChecked() and self.bt1_1.value() == 0:
                QMessageBox.question(self, 'ERROR', "CPU Burst time for P1 cannot be 0", QMessageBox.Ok)
                self.flag = False
            elif self.checkBox_2.isChecked() and self.bt1_2.value() == 0:
                QMessageBox.question(self, 'ERROR', "CPU Burst time for P2 cannot be 0", QMessageBox.Ok)
                self.flag = False
            elif self.checkBox_3.isChecked() and self.bt1_3.value() == 0:
                QMessageBox.question(self, 'ERROR', "CPU Burst time for P3 cannot be 0", QMessageBox.Ok)
                self.flag = False
            elif self.checkBox_4.isChecked() and self.bt1_4.value() == 0:
                QMessageBox.question(self, 'ERROR', "CPU Burst time for P4 cannot be 0", QMessageBox.Ok)
                self.flag = False
            elif self.checkBox_5.isChecked() and self.bt1_5.value() == 0:
                QMessageBox.question(self, 'ERROR', "CPU Burst time for P5 cannot be 0", QMessageBox.Ok)
                self.flag = False
            elif not self.checkBox_5.isChecked() and not self.checkBox_4.isChecked() and not self.checkBox_3.isChecked() \
                    and not self.checkBox_2.isChecked() and not self.checkBox_1.isChecked():
                QMessageBox.question(self, 'ERROR', "Nothing to simulate! Either No Process/CPU Burst time given.",
                                     QMessageBox.Ok)
                self.flag = False
            else:
                # {"p1": [5, 8], "p4": [4, 5], "p3": [3, 2], "p5": [2, 3], "p2": [1, 6]} => order by arrival time
                processes = {}
                if self.bt1_1.value() > 0:
                    processes["P1"] = [self.at_1.value(), self.bt1_1.value()]
                if self.bt1_2.value() > 0:
                    processes["P2"] = [self.at_2.value(), self.bt1_2.value()]
                if self.bt1_3.value() > 0:
                    processes["P3"] = [self.at_3.value(), self.bt1_3.value()]
                if self.bt1_4.value() > 0:
                    processes["P4"] = [self.at_4.value(), self.bt1_4.value()]
                if self.bt1_5.value() > 0:
                    processes["P5"] = [self.at_5.value(), self.bt1_5.value()]

                # sort according to arrival time using selection sort algo
                list_process = list(processes.items())
                #print(list_process[0][0])
                for i in range(len(list_process)):
                    min_idx = i
                    for j in range(i + 1, len(list_process)):
                        if list_process[i][1][0] > list_process[j][1][0]:
                            min_idx = j
                    list_process[i], list_process[min_idx] = list_process[min_idx], list_process[i]

                #print(list_process)
                self.algo = cpu_sched.Algo()
                self.algo.FCFS(list_process)

                temp_row = ()
                rows = []
                for i in range(len(list_process)):
                    temp_row = ((str(list_process[i][0]).upper()), self.algo.tat[i], self.algo.wait_time[i])
                    rows.append(temp_row)
                #todo : make this portion appears after the movement of process to cpu and the gantt chart have been rendered/drawn
                data=rows
                print(data)
                model = TableModel(self, data)
                self.tableView.setModel(model)

                #print(rows)
                self.flag = True

            if self.flag is True:
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
            self.label.move(i, 70)
            time.sleep(self.algo.arrival_time[0]/10)
        self.thread_suspend(self.thread1)
        self.label.setGeometry(QtCore.QRect(600, 190, 41, 41))

    def label2_move(self):
        for i in range(350, 380, 5):
            self.thread2.suspended.wait()
            self.label_2.move(i, 150)
            time.sleep(self.algo.arrival_time[1]/10)
        self.thread_suspend(self.thread2)
        self.label_2.setGeometry(QtCore.QRect(560, 190, 41, 41))
        self.instack()

    def label3_move(self):
        for i in range(350, 380, 5):
            self.thread3.suspended.wait()
            self.label_3.move(i, 230)
            time.sleep(self.algo.arrival_time[2]/10)
        self.thread_suspend(self.thread3)
        self.label_3.setGeometry(QtCore.QRect(520, 190, 41, 41))

    def label4_move(self):
        for i in range(350, 380, 5):
            self.thread4.suspended.wait()
            self.label_4.move(i, 310)
            time.sleep(self.algo.arrival_time[3]/10)
        self.thread_suspend(self.thread4)
        self.label_4.setGeometry(QtCore.QRect(480, 190, 41, 41))

    def label5_move(self):
        for i in range(350, 380, 5):
            self.thread5.suspended.wait()
            self.label_5.move(i, 370)
            time.sleep(self.algo.arrival_time[4] / 10)
        self.thread_suspend(self.thread5)
        self.label_5.setGeometry(QtCore.QRect(440, 190, 41, 41))

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

    def chartstack(self):
        i = 480
        while i <= 780:
            newp = QPoint(i, 530)
            self.chartRect.moveTo(newp)
            self.chartRect.translate(i)
            i += 10
            time.sleep(0.3)

    def instack(self):
        #todo : needs to order this as per arrival time
        i1, i4, i3, i2, i5 = 600, 560, 520, 480, 440
        while i5 <= 780:
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
            if i5 >= 780:
                self.label_5.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_5.setText("")
            self.label.move(i1, 190)
            self.label_2.move(i2, 190)
            self.label_3.move(i3, 190)
            self.label_4.move(i4, 190)
            self.label_5.move(i5, 190)
            i1 += 10
            i2 += 10
            i3 += 10
            i4 += 10
            i5 += 10
            time.sleep(0.3)

    def restart(self):
        os.system("python simulation.py")
        self.close()

#https://stackoverflow.com/questions/48928080/pyqt-signal-not-emitted-in-qabstracttablemodel
class TableModel(QAbstractTableModel):

    def __init__(self, parent, data, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.data = data
        #self.header = header

    def rowCount(self, parent):
        # How many rows are there?
        return len(self.data)

    def columnCount(self, parent):
        # How many columns?
        return len(headers)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        # What's the value of the cell at the given index?
        return self.data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        # What's the header for the given column?
        return headers[section]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()
    cpu_sched.sys.exit(app.exec_())
