import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 125, 36))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "start"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushed = 0
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        if self.pushed:
            for i in range(10):
                rad = randint(10, 100)
                color = [randint(0, 255), randint(0, 255), randint(0, 255)]
                self.qp.setPen(QColor(*color))
                self.qp.setBrush(QBrush(QColor(*color), Qt.SolidPattern))
                self.qp.drawEllipse(randint(0, 1000), randint(0, 300), rad, rad)
        self.qp.end()


    def run(self, event):
        self.pushed = 1
        self.update()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())