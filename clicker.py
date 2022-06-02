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
        print("Move ", event.pos().x(), event.pos().y())

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
        #painter.drawLine(362, 344, 372, 466)
        if self.n_pts == 2:
            painter.drawLine(self.mx_pts[0], self.my_pts[0], self.mx_pts[1], self.my_pts[1])

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
