'''
Author : Napsa Usman
MIT 201 CPU Scheduling
Western Mindanao State University, Philippines
SY: 2020-2021
Prof: Engineer Odon Maravillas Jr.
'''
import os, sys, time
import subprocess, threading
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPen
from PyQt5.QtCore import *
# from PyQt5 import *
from ui import *
from PyQt5.QtWidgets import *
from itertools import groupby
import process
import cpu_sched

# todo : input process order to be as per the no of checked box. both for fcfs and preemptive
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

        self.thread5 = threading.Thread(target=self.label5_move)
        self.thread1 = threading.Thread(target=self.label_move)
        self.thread2 = threading.Thread(target=self.label2_move)
        self.thread3 = threading.Thread(target=self.label3_move)
        self.thread4 = threading.Thread(target=self.label4_move)

        self.flag = False
        self.reset.pressed.connect(self.restart)
        self.fcfs.clicked.connect(self.start_fcfs)
        #self.preemptive.clicked.connect(self.start_preemptive_priority)
        self.color = [(255, 64, 0), (255, 128, 0), (255, 191, 0),
                      (255, 255, 0), (128, 255, 0), (128, 255, 0)]

        self.threadPool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadPool.maxThreadCount())

        self.algo = None
        self.data = None
        self.label_sequence = []

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        v_width_fixed = 560
        x_fixed = 345
        y_axis_and_heigth_1 = 95
        y_axis_and_heigth_2 = 145
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

    def update_table(self, progress):
        if progress == 99:
            headers = ["Process", "Turnaround", "Wait-Time"]
            model = TableModel(self, self.data, headers)
            self.tableView.setModel(model)

    def action_table(self):
        if self.flag is True:
            worker = Worker()
            worker.signals.progress.connect(self.update_table)
            self.threadPool.start(worker)

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
        self.timeForEachProcess = self.algo.tat
        self.trueSequence = self.algo.trueSequence
        self.trueBurstTime = self.algo.tat
        if self.flag:
            painter = QtGui.QPainter(self.labelchart.pixmap())

        # color bars.
        tailPos_by_arrival = self.algo.arrival_time[0] * 20
        tailPos = 10 + tailPos_by_arrival
        j = 0

        for i, k in zip(self.trueBurstTime, self.trueSequence):
            if k == "P1":
                r = self.color[0][0]
                g = self.color[0][1]
                b = self.color[0][2]
                painter.setBrush(QColor(r, g, b))

            if k == "P2":
                r = self.color[1][0]
                g = self.color[1][1]
                b = self.color[1][2]
                painter.setBrush(QColor(r, g, b))

            if k == "P3":
                r = self.color[2][0]
                g = self.color[2][1]
                b = self.color[2][2]
                painter.setBrush(QColor(r, g, b))

            if k == "P4":
                r = self.color[3][0]
                g = self.color[3][1]
                b = self.color[3][2]
                painter.setBrush(QColor(r, g, b))

            if k == "P5":
                r = self.color[4][0]
                g = self.color[4][1]
                b = self.color[4][2]
                painter.setBrush(QColor(r, g, b))

            # Process label
            p = str(self.trueSequence[j])
            chartRect = QRect(tailPos, 30, i + progress + 10, 30)
            self.update_progress(painter, chartRect, p, tailPos, i + 45)
            tailPos += i * 20
            j += 1

        # Ruler
        rulerPos = 10
        sumTime = sum(self.timeForEachProcess)
        for i in range(sumTime+1):
            painter.setBrush(QColor(0, 0, 0))
            painter.drawRect(rulerPos, 77, 1, 10)
            pen = QtGui.QPen()
            pen.setWidth(3)
            pen.setColor(QtGui.QColor('black'))
            painter.setPen(pen)
            painter.drawText(rulerPos, 75,str(i))
            rulerPos += 23
            if i == 100:
                break
        self.update()
        painter.end()

    def start_fcfs(self):
        if threading.activeCount() >= 2:
            pass
        else:
            # validation
            self.preemptive.hide()
            self.fcfs.hide()
            self.validate_input()
            if self.flag is True:
                processes = []
                if self.bt1_1.value() > 0:
                    p = process.Process()
                    p.p_id = "P1"
                    p.arrival_time = self.at_1.value()
                    p.burst_time = self.bt1_1.value()
                    processes.append(p)

                if self.bt1_2.value() > 0:
                    p = process.Process()
                    p.p_id = "P2"
                    p.arrival_time = self.at_2.value()
                    p.burst_time = self.bt1_2.value()
                    processes.append(p)

                if self.bt1_3.value() > 0:
                    p = process.Process()
                    p.p_id = "P3"
                    p.arrival_time = self.at_3.value()
                    p.burst_time = self.bt1_3.value()
                    processes.append(p)

                if self.bt1_4.value() > 0:
                    p = process.Process()
                    p.p_id = "P4"
                    p.arrival_time = self.at_4.value()
                    p.burst_time = self.bt1_4.value()
                    processes.append(p)

                if self.bt1_5.value() > 0:
                    p = process.Process()
                    p.p_id = "P5"
                    p.arrival_time = self.at_5.value()
                    p.burst_time = self.bt1_5.value()
                    processes.append(p)

                self.algo = cpu_sched.Algo()
                self.algo.FCFS(processes)

                temp_row = ()
                rows = []
                for i in range(len(processes)):
                    temp_row = ((processes[i].p_id, self.algo.tat[i], self.algo.wait_time[i]))
                    rows.append(temp_row)

                self.data = rows
                self.start_thread()

    def validate_input(self):
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
        else:
            self.flag = True

    def start_thread(self):
        if self.flag is True:

            self.thread1.suspended = threading.Event()
            self.thread1.suspended.set()

            self.thread2.suspended = threading.Event()
            self.thread2.suspended.set()

            self.thread3.suspended = threading.Event()
            self.thread3.suspended.set()

            self.thread4.suspended = threading.Event()
            self.thread4.suspended.set()

            self.thread5.suspended = threading.Event()
            self.thread5.suspended.set()

            self.thread5.start()
            self.thread1.start()
            self.thread2.start()
            self.thread3.start()
            self.thread4.start()

            self.action_table()
            self.action_chart()

    def suspend_threads(self):
        for i in range(1, 5):
            self.thread_suspend(eval("self.thread" + str(i)))

    def resume_threads(self):
        for i in range(1, 5):
            self.thread_resume(eval("self.thread" + str(i)))

    def label_move(self):
        index_for_sleep = 0
        initial_position = [600, 560, 520, 480, 440]
        label_position = 0
        for i in range(len(self.algo.trueSequence)):
            if self.algo.trueSequence[i] == "P1":
                index_for_sleep = i + 1
                label_position = initial_position[i]
                break

        for i in range(350, 380, 10):
            self.thread1.suspended.wait()
            self.label.move(i, 70)
            time.sleep(index_for_sleep / 10)
        self.thread_suspend(self.thread1)

        self.label.setGeometry(QtCore.QRect(label_position, 190, 41, 41))
        self.move_01(label_position, 780, index_for_sleep/10)

    def label2_move(self):
        index_for_sleep = 0
        initial_position = [600, 560, 520, 480, 440]
        label_position = 0
        for i in range(len(self.algo.trueSequence)):
            if self.algo.trueSequence[i] == "P2":
                index_for_sleep = i + 1
                label_position = initial_position[i]
                break

        for i in range(350, 380, 5):
            self.thread2.suspended.wait()
            self.label_2.move(i, 150)
            time.sleep(index_for_sleep/ 10)
        self.thread_suspend(self.thread2)

        self.label_2.setGeometry(QtCore.QRect(label_position, 190, 41, 41))
        self.move_02(label_position, 780, index_for_sleep/10)

    def label3_move(self):
        index_for_sleep = 0
        initial_position = [600, 560, 520, 480, 440]
        label_position = 0
        for i in range(len(self.algo.trueSequence)):
            if self.algo.trueSequence[i] == "P3":
                index_for_sleep = i + 1
                label_position = initial_position[i]
                break

        for i in range(350, 380, 5):
            self.thread3.suspended.wait()
            self.label_3.move(i, 230)
            time.sleep(index_for_sleep / 10)
        self.thread_suspend(self.thread3)

        self.label_3.setGeometry(QtCore.QRect(label_position, 190, 41, 41))
        self.move_03(label_position, 780, index_for_sleep/10)

    def label4_move(self):
        index_for_sleep = 0
        initial_position = [600, 560, 520, 480, 440]
        label_position = 0
        for i in range(len(self.algo.trueSequence)):
            if self.algo.trueSequence[i] == "P4":
                index_for_sleep = i + 1
                label_position = initial_position[i]
                break

        for i in range(350, 380, 5):
            self.thread4.suspended.wait()
            self.label_4.move(i, 310)
            time.sleep(index_for_sleep / 10)
        self.thread_suspend(self.thread4)

        self.label_4.setGeometry(QtCore.QRect(label_position, 190, 41, 41))
        self.move_04(label_position, 780, index_for_sleep/10)

    def label5_move(self):
        index_for_sleep = 0
        initial_position = [600, 560, 520, 480, 440]
        label_position = 0
        for i in range(len(self.algo.trueSequence)):
            if self.algo.trueSequence[i] =="P5":
                index_for_sleep = i+1
                label_position = initial_position[i]
                break

        for i in range(350, 380, 5):
            self.thread5.suspended.wait()
            self.label_5.move(i, 350)
            time.sleep(index_for_sleep / 10)
        self.thread_suspend(self.thread5)

        self.label_5.setGeometry(QtCore.QRect(label_position, 190, 41, 41))
        self.move_05(label_position, 780, index_for_sleep/10)

    def move_05(self, initial, max, sleep):
        while initial <= max:
            if initial >= 780:
                self.label_5.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_5.setText("")
            self.label_5.move(initial, 190)
            initial +=10
            time.sleep(sleep)

    def move_04(self, initial, max, sleep):
        while initial <= max:
            if initial >= 780:
                self.label_4.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_4.setText("")
            self.label_4.move(initial, 190)
            initial +=10
            time.sleep(sleep)

    def move_03(self, initial, max, sleep):

        while initial <= max:
            if initial >= 780:
                self.label_3.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_3.setText("")
            self.label_3.move(initial, 190)
            initial +=10
            time.sleep(sleep)

    def move_02(self, initial, max, sleep):

        while initial <= max:
            if initial >= 780:
                self.label_2.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label_2.setText("")
            self.label_2.move(initial, 190)
            initial += 10
            time.sleep(sleep)

    def move_01(self, initial, max, sleep):

        while initial <= max:
            if initial >= 780:
                self.label.setStyleSheet("QLabel{background:#F0F0F0;}")
                self.label.setText("")
            self.label.move(initial, 190)
            initial += 10
            time.sleep(sleep)

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

    def restart(self):
        os.system("python simulation_fcfs.py")
        self.close()

# https://stackoverflow.com/questions/48928080/pyqt-signal-not-emitted-in-qabstracttablemodel
class TableModel(QAbstractTableModel):
    def __init__(self, parent, data, headers, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.data = data
        self.headers = headers

    def rowCount(self, parent):
        # How many rows are there?
        return len(self.data)

    def columnCount(self, parent):
        # How many columns?
        return len(self.headers)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        # What's the value of the cell at the given index?
        return self.data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        # What's the header for the given column?
        return self.headers[section]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()
    cpu_sched.sys.exit(app.exec_())
