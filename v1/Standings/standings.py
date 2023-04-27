# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import QTimer, Qt
import irsdk, operator
import sqlite3 as sql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1031, 731))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblSerie = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblSerie.setFont(font)
        self.lblSerie.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSerie.setObjectName("lblSerie")
        self.horizontalLayout_6.addWidget(self.lblSerie)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblCar = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblCar.setFont(font)
        self.lblCar.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCar.setObjectName("lblCar")
        self.horizontalLayout_7.addWidget(self.lblCar)
        self.lblCircuito = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblCircuito.setFont(font)
        self.lblCircuito.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCircuito.setObjectName("lblCircuito")
        self.horizontalLayout_7.addWidget(self.lblCircuito)
        self.lblSOF = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblSOF.setMinimumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblSOF.setFont(font)
        self.lblSOF.setTextFormat(QtCore.Qt.PlainText)
        self.lblSOF.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSOF.setObjectName("lblSOF")
        self.horizontalLayout_7.addWidget(self.lblSOF)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(16)
        self.lwPosiciones = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lwPosiciones.setObjectName("lwPosiciones")
        self.lwPosiciones.setFont(font)
        self.verticalLayout.addWidget(self.lwPosiciones)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 21))
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
        self.lblSerie.setText(_translate("MainWindow", "European Endurance Pure Dribing School Series"))
        self.lblCar.setText(_translate("MainWindow", "Audi RS3 LMS"))
        self.lblCircuito.setText(_translate("MainWindow", "Weathertech Laguna Seca"))
        self.lblSOF.setText(_translate("MainWindow", "2000"))
    
    ir = irsdk.IRSDK()
    ir.startup()
    playerID = ir['PlayerCarIdx']
    trackID = ir['WeekendInfo']['TrackID']
    carID = ir['DriverInfo']['Drivers'][playerID]['CarID']
    seriesID = ir['WeekendInfo']['SeriesID']

    def getCarDB(self):
            conn = sql.connect("iRacing.db")
            cursor = conn.cursor()
            query = f"SELECT Marca, Modelo FROM Vehiculos WHERE IDVehiculo = {self.carID}"
            cursor.execute(query)
            data = cursor.fetchone()
            conn.commit()
            conn.close()
            if(data == None):
                return 0
            else:
                return data[0] + " " + data[1]
    def getSerieDB(self):
            conn = sql.connect("iRacing.db")
            cursor = conn.cursor()
            query = f"SELECT Nombre FROM Series WHERE IDSerie = {self.seriesID}"
            cursor.execute(query)
            data = cursor.fetchone()
            conn.commit()
            conn.close()
            if(data == None):
                return 0
            else:
                return data[0]
    def getCircuitoDB(self):
        conn = sql.connect("iRacing.db")
        cursor = conn.cursor()
        query = f"SELECT Nombre FROM Circuitos WHERE IDCircuito = {self.trackID}"
        cursor.execute(query)
        data = cursor.fetchone()
        if data == None:
            query2 = f"""INSERT INTO Circuitos (IDCircuito, Nombre, Pais, Ciudad, Longitud, Variante, Comprado) VALUES ({self.trackID}, '{self.ir['WeekendInfo']['TrackDisplayName']}', '{self.ir['WeekendInfo']['TrackCountry']}', '{self.ir['WeekendInfo']['TrackCity']}', '{self.ir['WeekendInfo']['TrackLengthOfficial']}', '{self.ir['WeekendInfo']['TrackConfigName']}', 1)"""
            cursor.execute(query2)
            cursor.execute(query)
            data = cursor.fetchone()
        conn.commit()
        conn.close()
        if(data == None):
            return 0
        else:
            return data[0]

    def cargarDatosFijos(self):
        if Ui_MainWindow.getSerieDB(self) != 0:
            self.lblSerie.setText(Ui_MainWindow.getSerieDB(self))
        if Ui_MainWindow.getCarDB(self) != 0:
            self.lblCar.setText(Ui_MainWindow.getCarDB(self))
        if Ui_MainWindow.getCircuitoDB(self) != 0:
            self.lblCircuito.setText(Ui_MainWindow.getCircuitoDB(self))
        #self.lblSOF.setText(self.ir[])

    def agregar_cero_si_es_necesario(self, valor):
        return f"{valor:02d}"
    
    def convertirVueltas(self, vuelta):
        minutos, segundos_sobrantes = divmod(float(vuelta), 60)
        tiempo = self.agregar_cero_si_es_necesario(int(minutos)) + ":{0:.3f}".format(segundos_sobrantes)
        return tiempo

    def cargarDatosVariables(self):
        self.lwPosiciones.clear()
    # Obtén los datos de la posición de los participantes
        participantes = self.ir['SessionInfo']['Sessions'][0]['ResultsPositions']
    # Ordena los participantes por su posición en la carrera
        if participantes != None:
            for i in participantes:
                posicion = str(i['Position'])
                while len(posicion) < 5:
                    posicion += " "
                nombre = self.ir['DriverInfo']['Drivers'][i['CarIdx']]['UserName']
                while len(nombre) < 25:
                    nombre += " "
                safety = self.ir['DriverInfo']['Drivers'][i['CarIdx']]['LicString']
                iRating = str(self.ir['DriverInfo']['Drivers'][i['CarIdx']]['IRating'])
                while len(iRating) < 8:
                    iRating += " "
                vRapida = str(i['FastestTime'])
                vRapida = self.convertirVueltas(vRapida)
                uVuelta = str(i['LastTime'])
                uVuelta = self.convertirVueltas(uVuelta)
                item = QListWidgetItem(posicion + nombre + safety + "    " + iRating + vRapida + "    " + uVuelta)
                self.lwPosiciones.addItem(item)
                gris = QColor(189, 195, 199)  # Color gris
                blanco = QColor(236, 240, 241)  # Color blanco
                if int(posicion) % 2 == 0:
                    brush = QBrush(blanco)
                else:
                    brush = QBrush(gris)
                
                item.setData(Qt.BackgroundRole, brush)
        else:
            participantes = self.ir['QualifyResultsInfo']['Results']
            for i in participantes:
                nombre = self.ir['DriverInfo']['Drivers'][i['CarIdx']]['UserName']
                vRapida = nombre = self.ir['DriverInfo']['Drivers'][i['CarIdx']]['FastestTime']
                uVuelta = nombre = self.ir['DriverInfo']['Drivers'][i['CarIdx']]['LastTime']
                item = QListWidgetItem(nombre)
                self.lwPosiciones.addItem(item)

        currentLap = self.ir['Lap']
        #Mostramos combustible actual
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.cargarDatosFijos()
    ui.cargarDatosVariables()
    MainWindow.show()

    sys.exit(app.exec_())
