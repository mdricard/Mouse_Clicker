import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QVBoxLayout
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap, QPen, QColor, QPainter, QCursor
from PyQt5.QtCore import pyqtSlot, QRect, Qt, QPoint, QPointF


class MyLabelPixmap(QLabel):
    mx_pts = []
    my_pts = []
    n_pts = 0

    def __init__(self):
        QLabel.__init__(self)
        self.pixmap = QtGui.QPixmap('d:/heart.png')
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

    def mouseMoveEvent(self, event):
        pass
        #print("Move ", event.pos().x(), event.pos().y())

    def mousePressEvent(self, event):
        self.mx_pts.append(event.pos().x())
        self.my_pts.append(event.pos().y())
        self.n_pts += 1
        print("Mouse Press ", event.pos().x(), event.pos().y())
        print("Length ", len(self.mx_pts))
        self.update()                           # call update to update the drawing (paint event)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("d:/heart.png")
        painter.drawPixmap(self.rect(), pixmap)
        pen = QPen(Qt.red, 2)
        painter.setPen(pen)
        if self.n_pts == 2:
            painter.drawLine(self.mx_pts[0], self.my_pts[0], self.mx_pts[1], self.my_pts[1])
            pts = self.midPoints(0.25)
            painter.drawLine(int(pts[0]), int(pts[1]), int(pts[2]), int(pts[3]))
            pts = self.midPoints(0.50)
            painter.drawLine(int(pts[0]), int(pts[1]), int(pts[2]), int(pts[3]))
            pts = self.midPoints(0.75)
            painter.drawLine(int(pts[0]), int(pts[1]), int(pts[2]), int(pts[3]))

    def midPoints(self, percent):
        """
        https://www.varsitytutors.com/act_math-help/how-to-find-the-equation-of-a-perpendicular-line#:~:text=Perpendicular%20lines%20have%20opposite%2Dreciprocal,%2F2%20%2B%20y%20%3D%206.
        self.mx_pts[0] = 0.0
        self.my_pts[0] = 3.0
        self.mx_pts[1] = 1.0
        self.my_pts[1] = 2.4
        """
        x_percent = self.mx_pts[0] + (percent * (self.mx_pts[1] - self.mx_pts[0]))
        y_percent = self.my_pts[0] + (percent * (self.my_pts[1] - self.my_pts[0]))
        # below is the perpendicular slope to pts[0] and pts[1]
        m = (self.my_pts[1] - self.my_pts[0]) / (self.mx_pts[1] - self.mx_pts[0])
        slope = -1.0 / m
        b = (-slope * x_percent) + y_percent
        #b = (-slope * 3.0) + 2.0
        x_left = x_percent - 100.0
        y_left = (slope * x_left) + b
        x_right = x_percent + 200.0
        y_right = (slope * x_right) + b
        #print("slope = ", m)
        #print("b = ", b)
        #print("Per Slope: ", slope)
        return [x_left, y_left, x_right, y_right]

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.resize(900, 900)
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QLabel("Top"))
        heart_pic = MyLabelPixmap()
        layout.addWidget(heart_pic)
        # Set the layout on the application's window
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
