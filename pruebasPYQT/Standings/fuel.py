# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import irsdk
import sqlite3 as sql

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 671, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lblFuelLevel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.lblFuelLevel.setFont(font)
        self.lblFuelLevel.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFuelLevel.setObjectName("lblFuelLevel")
        self.verticalLayout_2.addWidget(self.lblFuelLevel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.lblLaps = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.lblLaps.setFont(font)
        self.lblLaps.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLaps.setObjectName("lblLaps")
        self.verticalLayout_3.addWidget(self.lblLaps)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.lblAverage = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.lblAverage.setFont(font)
        self.lblAverage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAverage.setObjectName("lblAverage")
        self.verticalLayout_6.addWidget(self.lblAverage)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.lblRemaining = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.lblRemaining.setFont(font)
        self.lblRemaining.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRemaining.setObjectName("lblRemaining")
        self.verticalLayout_7.addWidget(self.lblRemaining)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.lblRefuel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.lblRefuel.setFont(font)
        self.lblRefuel.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRefuel.setObjectName("lblRefuel")
        self.verticalLayout_5.addWidget(self.lblRefuel)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.lblFuelAtEnd = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.lblFuelAtEnd.setFont(font)
        self.lblFuelAtEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFuelAtEnd.setObjectName("lblFuelAtEnd")
        self.verticalLayout_4.addWidget(self.lblFuelAtEnd)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

         # Iniciamos el temporizador para actualizar el valor
        self.timer = QTimer()
        self.timer.timeout.connect(self.cargarDatos)
        self.timer.start(1000)  # Actualiza cada 1000 milisegundos (1 segundo)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Fuel Level"))
        self.lblFuelLevel.setText(_translate("MainWindow", "15.55 l"))
        self.label_13.setText(_translate("MainWindow", "Laps in Race"))
        self.lblLaps.setText(_translate("MainWindow", "10.00"))
        self.label_4.setText(_translate("MainWindow", "Average"))
        self.lblAverage.setText(_translate("MainWindow", "2.03"))
        self.label_6.setText(_translate("MainWindow", "Laps Remaining"))
        self.lblRemaining.setText(_translate("MainWindow", "8.05"))
        self.label_9.setText(_translate("MainWindow", "Refuel"))
        self.lblRefuel.setText(_translate("MainWindow", "--:--"))
        self.label_11.setText(_translate("MainWindow", "Fuel at End"))
        self.lblFuelAtEnd.setText(_translate("MainWindow", "1.06"))
    

    ir = irsdk.IRSDK()
    ir.startup(test_file='carreraBots.bin')
    playerID = ir['PlayerCarIdx']
    trackID = ir['WeekendInfo']['TrackID']
    carID = ir['DriverInfo']['Drivers'][playerID]['CarID']    

    def getAVGFuelDB(IDVehiculo, IDCircuito):
        conn = sql.connect("iRacing.db")
        cursor = conn.cursor()
        query = f"SELECT MediaConsumo FROM VueltaRapida WHERE IDCircuito = {IDCircuito} AND IDVehiculo = {IDVehiculo}"
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        if(data == None):
            return 0
        else:
            return data[0]
    #Buscamos en la bbdd la media de consumo por vuelta con el coche y circuito actuales  
    avgFuel = getAVGFuelDB(carID, trackID)

    def getFastestLapDB(IDVehiculo, IDCircuito):
        conn = sql.connect("iRacing.db")
        cursor = conn.cursor()
        query = f"SELECT Tiempo FROM VueltaRapida WHERE IDCircuito = {IDCircuito} AND IDVehiculo = {IDVehiculo}"
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        if(data == None):
            return 0
        else:
            return data[0]
        
    #vueltas totales de carrera si es por tiempo, calcula las vueltas que se hará
    vueltasTotales = ir['SessionInfo']['Sessions'][0]['SessionLaps']
    if vueltasTotales == 'unlimited':
        tiempototal = ir['SessionInfo']['Sessions'][0]['SessionTime'].split(" ")
        vueltasTotales = float(tiempototal[0]) / getFastestLapDB(carID, trackID)

    def calcularRefuel(self, fuelLevel, fuelConsuption, totalLaps, currentLap):
        autonomia = fuelLevel / fuelConsuption
        vRestantes = totalLaps - currentLap
        if autonomia > vRestantes:
            return 0
        else:
            refuel = vRestantes * fuelConsuption + 1.5
            return refuel

        
    def cargarDatos(self):
        fuelLevel = self.ir['FuelLevel']
        currentLap = self.ir['Lap']
        #Mostramos combustible actual
        self.lblFuelLevel.setText("{0:.2f}".format((fuelLevel)))

        refuel = self.calcularRefuel(fuelLevel, self.avgFuel, self.vueltasTotales, currentLap)

        self.lblRefuel.setText("{0:.2f}".format((refuel)))
        if(self.avgFuel == 0):   #Si no encuentra devuelve 0, por lo que no mostramos por pantalla ningun dato
            self.lblAverage.setText("--:--")
            self.lblRemaining.setText("--:--")
        else:   #Si encuentra valor, mostramos por pantalla 
            self.lblAverage.setText(str(self.avgFuel))
            remainingLaps = fuelLevel / self.avgFuel
            self.lblRemaining.setText("{0:.2f}".format((remainingLaps)))
        
        self.lblLaps.setText("{0:.2f}".format((self.vueltasTotales)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.cargarDatos()
    MainWindow.show()

    sys.exit(app.exec_())
