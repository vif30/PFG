# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import irsdk, time
import sqlite3 as sql
from database import Database
from iRData import iRData

class Fuel(object):
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
        self.timer.timeout.connect(self.cargarDatosVariables)
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
    ir.startup(test_file='datavuelta4.bin')
    if ir.is_connected:
        playerID = ir['PlayerCarIdx']
        trackID = ir['WeekendInfo']['TrackID']
        carID = ir['DriverInfo']['Drivers'][playerID]['CarID']
        vuelta = ir['Lap']
        fuelLevel1 = ir['FuelLevel']
        while fuelLevel1 == 0:
            fuelLevel1 = ir['FuelLevel']
        fuelCon = []
        avgFuel = 0
        vTotales = 0
        totalFuel = 0
        lastLapPit = False

    #Metodo para obtener el tipo de sesion en la que estamos (practica, clasificacion o carrera)
    def getSesion(self):
        if len(self.ir['SessionInfo']['Sessions']) == 3:
            return 2
        elif len(self.ir['SessionInfo']['Sessions']) == 2:
            return 1
        elif len(self.ir['SessionInfo']['Sessions']) == 1:
            return 0

    def calcularRefuel(self, fuelLevel, fuelConsuption, totalLaps, currentLap):
        if fuelConsuption > 0:
            autonomia = fuelLevel / fuelConsuption
            vRestantes = totalLaps - currentLap
            if autonomia > vRestantes:
                return 0
            else:
                refuel = vRestantes * fuelConsuption + 1.5
                return refuel
        else: 
            return 0

    def getConsumo(self):
        currLap = self.ir['Lap']
        if self.vuelta != currLap:
            if self.lastLapPit:
                self.lastLapPit = False
            else:
                consumoVuelta = self.fuelLevel1 - self.ir['FuelLevel']
                self.fuelCon.append(consumoVuelta)
                self.fuelCon.sort()
                self.vuelta = self.ir['Lap']
                self.fuelLevel1 = self.ir['FuelLevel']
                self.totalFuel = self.totalFuel + consumoVuelta
                self.avgFuel = round(self.totalFuel / len(self.fuelCon), 2)

    def cargarDatosFijos(self):
        sesion = iRData.getSesion()
        tTotal = self.ir['SessionInfo']['Sessions'][sesion]['SessionTime']
        if tTotal != 'unlimited':
            tTotal = tTotal.split()
            tTotal = float(tTotal[0])
        self.avgFuel = Database.getAVGFuelDB(self.trackID, self.carID)

        if self.ir['SessionInfo']['Sessions'][sesion]['SessionLaps'] ==  'unlimited' and self.ir['SessionInfo']['Sessions'][sesion]['SessionType'] == 'Race':
            if Database.getVueltaRapidaDB(self.trackID, self.carID) != 0:
                vRapida = Database.getVueltaRapidaDB(self.trackID, self.carID)
                self.vTotales = tTotal/vRapida
            else:
                estLap = self.ir['DriverInfo']['Drivers'][self.playerID]['CarClassEstLapTime']
                self.vTotales = tTotal/estLap
        elif self.ir['SessionInfo']['Sessions'][sesion]['SessionType'] == 'Race':
            self.vTotales = self.ir['SessionInfo']['Sessions'][sesion]['SessionLaps']
        self.lblLaps.setText("{0:.0f}".format((self.vTotales)))

    def cargarDatosVariables(self):
        if not self.ir.is_connected:
            if len(self.fuelCon) != 0:
                if self.ir['SessionLapsRemainEx'] == 0 or not self.ir.is_connected:
                    self.avgFuel = round(self.totalFuel / len(self.fuelCon), 2)
                    if Database.getAVGFuelDB(self.trackID, self.carID) != 0:
                        Database.updateAvgFuel(self.avgFuel, self.trackID, self.carID)
                    else:
                        Database.insertNewAvgFuel(self.trackID, self.carID, self.avgFuel)
            sys.exit()
        self.lblLaps.setText(str(self.vuelta))
        fuelLevel = self.ir['FuelLevel']
        while fuelLevel == 0:
            fuelLevel = self.ir['FuelLevel']
        if self.ir['PlayerCarInPitStall']:
            self.lastLapPit = True
        print(self.lastLapPit)
        self.getConsumo()
        #Mostramos combustible actual
        self.lblFuelLevel.setText("{0:.2f}".format((fuelLevel)))
        self.fuelCon.sort()
        self.lblAverage.setText("{0:.2f}".format((self.avgFuel)))

        refuel = self.calcularRefuel(fuelLevel, self.avgFuel, self.vTotales, self.ir['Lap'])
        if refuel != 0:
            self.lblRefuel.setText("{0:.2f}".format((refuel)))
            vRestante = self.vTotales - self.ir['Lap']
            sobrante = refuel - (vRestante * self.avgFuel)
            self.lblFuelAtEnd.setText(str(sobrante))
        else:
            self.lblRefuel.setText("--:--")

            self.lblFuelAtEnd.setText("--:--")
        
        if(self.avgFuel == 0):   #Si no encuentra devuelve 0, por lo que no mostramos por pantalla ningun dato
            self.lblAverage.setText("--:--")
            self.lblRemaining.setText("--:--")
        else:   #Si encuentra valor, mostramos por pantalla 
            self.lblAverage.setText(str(self.avgFuel))
            remainingLaps = fuelLevel / self.avgFuel

            self.lblRemaining.setText("{0:.2f}".format((remainingLaps)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Fuel()
    if ui.ir.is_connected:
        ui.setupUi(MainWindow)
        ui.cargarDatosFijos()
        ui.cargarDatosVariables()
        MainWindow.show()
        sys.exit(app.exec_())
    else:
        MainWindow.close()
        sys.exit()
