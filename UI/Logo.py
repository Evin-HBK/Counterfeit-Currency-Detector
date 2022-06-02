from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 676)
        font = QtGui.QFont()
        font.setFamily("3270 Condensed")
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(230, 350, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(28)
        self.Name.setFont(font)
        self.Name.setTextFormat(QtCore.Qt.AutoText)
        self.Name.setObjectName("Name")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(-10, 230, 771, 91))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("Assets/Logo.png"))
        self.Logo.setObjectName("Logo")
        self.verinfo = QtWidgets.QLabel(self.centralwidget)
        self.verinfo.setGeometry(QtCore.QRect(680, 640, 71, 20))
        font = QtGui.QFont()
        font.setFamily("3270 Condensed")
        font.setPointSize(8)
        self.verinfo.setFont(font)
        self.verinfo.setObjectName("verinfo")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 640, 121, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 630, 121, 18))
        font = QtGui.QFont()
        font.setFamily("3270 Condensed")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CashCheck"))
        self.Name.setText(_translate("MainWindow", "Currency Verifier"))
        self.verinfo.setText(_translate("MainWindow", "version 1.0"))
        self.label.setText(_translate("MainWindow", "Loading Resouces..."))

def draw():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    draw()