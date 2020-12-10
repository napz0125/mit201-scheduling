from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
from ui import *
import sys

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


class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self, *args, **kwargs):
        #super(MainWindow, self).__init__(*args, **kwargs)
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btnRun.pressed.connect(self.action_chart)

        '''layout = QVBoxLayout()

        button1 = QPushButton("Run")
        button1.pressed.connect(self.action_chart)

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(200, 200)
        self.label.setPixmap(canvas)

        layout.addWidget(button1)
        layout.addWidget(self.label)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.show()'''

        self.threadPool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadPool.maxThreadCount())

    def draw_chart(self, progress):
        painter = QtGui.QPainter(self.labelchart.pixmap())
        painter.setBrush(QColor(20, 50, 80))
        painter.drawRect(30, 50, progress, 30)
        painter.end()
        self.update()
        print(progress)

    def action_chart(self):
        worker = Worker()
        worker.signals.progress.connect(self.draw_chart)
        self.threadPool.start(worker)

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        self.threadPool.start(worker)

    def update_progress(self, progress):
        self.bar.setValue(progress)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
