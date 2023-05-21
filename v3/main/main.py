# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from standings import Standings

from iRData import iRData

class Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnFuel = QtWidgets.QPushButton(self.centralwidget)
        self.btnFuel.setGeometry(QtCore.QRect(340, 290, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.btnFuel.setFont(font)
        self.btnFuel.setObjectName("btnFuel")
        self.lblBienvenida = QtWidgets.QLabel(self.centralwidget)
        self.lblBienvenida.setGeometry(QtCore.QRect(170, 40, 481, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(20)
        self.lblBienvenida.setFont(font)
        self.lblBienvenida.setObjectName("lblBienvenida")
        self.btnStandings = QtWidgets.QPushButton(self.centralwidget)
        self.btnStandings.setGeometry(QtCore.QRect(340, 200, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.btnStandings.setFont(font)
        self.btnStandings.setObjectName("btnStandings")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Iniciamos el temporizador para actualizar el valor
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkiRacing)
        self.timer.start(1000)  # Actualiza cada 1000 milisegundos (1 segundo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnFuel.setText(_translate("MainWindow", "Fuel Calculator"))
        self.lblBienvenida.setText(_translate("MainWindow", "Elija los complementos que desea iniciar"))
        self.btnStandings.setText(_translate("MainWindow", "Standings"))
    
    def openStandings(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Standings()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    def openFuel(self):
        from fuel import Fuel
        self.ventana2 = QtWidgets.QMainWindow()
        self.ui2 = Fuel()
        self.ui2.setupUi(self.ventana2)
        self.ventana2.show()

    def checkiRacing(self):
        if iRData.ir.is_connected:
            self.btnFuel.setStyleSheet('background-color: green')
            self.btnFuel.clicked.connect(self.openFuel)
            self.btnStandings.setStyleSheet('background-color: green')
            self.btnStandings.clicked.connect(self.openStandings)
        else:
            self.btnFuel.setStyleSheet('background-color: red')
            self.btnStandings.setStyleSheet('background-color: red')
        iRData.ir.startup()
  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    ui.checkiRacing()
    MainWindow.show()
    sys.exit(app.exec_())
