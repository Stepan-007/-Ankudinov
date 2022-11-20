import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random
from PyQt5.QtGui import QPainter, QColor


class MyEllipse:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def draw(self, qp):
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.x, self.y, self.d, self.d)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('#1.ui', self)
        self.pushButton.clicked.connect(self.draw)

        self.qp = QPainter()
        self.obj = []

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        for i in self.obj:
            i.draw(self.qp)
        self.qp.end()

    def draw(self):
        x = random.randint(50, 350)
        y = random.randint(50, 350)
        d = random.randint(10, 50)
        self.obj.append(MyEllipse(x, y, d))
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    app.exec_()
    sys.excepthook = except_hook
    sys.exit(app.exec_())