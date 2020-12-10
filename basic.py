from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time

# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.resize(1200, 800)
        self.setWindowTitle("test App")
        self.color = QColor(Qt.red)
        self.rect_circle = QRect(10, 20, 0, 20)
        layout = QVBoxLayout()

        self.butt = QPushButton()
        self.butt.setObjectName("buttbutt")
        self.butt.setText("butt butt")
        self.butt.clicked.connect(self.update_position)
        layout.addWidget(self.butt)

        self.step = QPoint(50, 100)
        self.y_direction = 1

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def paintEvent(self, event):
        bounce = QPainter(self)
        bounce.setPen(Qt.black)
        bounce.setBrush(Qt.red)
        bounce.drawRect(self.rect_circle)

    def update_position(self):
        i = 1
        n = 5
        x = 50
        while i <= n:
            j = 1
            while j <= i:
                self.rect_circle = QRect(10, 20, x, 20)
                j += 1
                x += 10
                #self.rect_circle.translate(self.step * self.y_direction)
            print(self.rect_circle)
            self.update()
            time.sleep(0.5)
            i += 1


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped.