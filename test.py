import sys
import time
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import *
#import QColor, QPainter
from PyQt5.QtCore import Qt, QRect, QPoint, QTimer, Q


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.color = QColor(Qt.red)
        self.rect_circle = QRect(0, 0, 100, 50)
        #self.rect_circle.moveBottomLeft(QPoint(self.width() / 2, self.rect_circle.height() / 2))



        self.step = QPoint(50, 100)
        self.y_direction = 1



        timer = QTimer(self, interval=10)
        timer.timeout.connect(self.update_position)
        timer.start()

    def paintEvent(self, event):
        bounce = QPainter(self)
        bounce.setPen(Qt.black)
        bounce.setBrush(Qt.red)
        bounce.drawRect(self.rect_circle)

    def update_position(self):
        #if self.rect_circle.right() > self.width() and self.y_direction == 1:
        #    self.y_direction = -1
        #if self.rect_circle.left() < 0 and self.y_direction == -1:
        #    self.y_direction = 1

        i = 1
        n = 5
        x = 50
        y = 50
        while i <= n:
            j = 1
            while j <= i:
                self.rect_circle = QRect(0, 0, x, 50)
                j += 1
                x += 10
                y += 10
                self.rect_circle.translate(self.step * self.y_direction)
                self.update()
                time.sleep(0.5)
            print(self.rect_circle)
            i += 1

        #print(self.step * self.y_direction)
        #self.rect_circle.translate(self.step * self.y_direction)
        #self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())
