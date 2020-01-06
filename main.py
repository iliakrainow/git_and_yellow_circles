import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui',self)
        self.pushed = 0
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        if self.pushed:
            self.qp.setPen(QColor(237, 249, 3))
            self.qp.setBrush(QBrush(QColor(237, 249, 3), Qt.SolidPattern))
            for i in range(10):
                rad = randint(10, 100)
                self.qp.drawEllipse(randint(0, 1000), randint(0, 300), rad, rad)
        self.qp.end()


    def run(self, event):
        self.pushed = 1
        self.update()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())