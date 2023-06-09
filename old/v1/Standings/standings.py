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


class Standings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1000, 731))
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
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblCar = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblCar.adjustSize()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCar.sizePolicy().hasHeightForWidth())
        self.lblCar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.lblCar.setFont(font)
        self.lblCar.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCar.setObjectName("lblCar")
        self.horizontalLayout_7.addWidget(self.lblCar)
        self.lblSOF = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.lblSOF.setFont(font)
        self.lblSOF.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSOF.setObjectName("lblCircuito")
        self.lblSOF.adjustSize()
        self.horizontalLayout_7.addWidget(self.lblSOF)
        self.lblCircuito = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblCircuito.setMinimumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.lblCircuito.setFont(font)
        self.lblCircuito.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCircuito.setObjectName("lblSOF")
        self.lblCircuito.adjustSize()
        self.horizontalLayout_7.addWidget(self.lblCircuito)
        self.lblVueltas = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblVueltas.setMinimumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.lblVueltas.setFont(font)
        self.lblVueltas.setTextFormat(QtCore.Qt.PlainText)
        self.lblVueltas.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVueltas.setObjectName("lblVueltas")
        self.lblVueltas.adjustSize()
        self.horizontalLayout_7.addWidget(self.lblVueltas)
        self.lblTiempo = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.lblTiempo.setMinimumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblTiempo.setFont(font)
        self.lblTiempo.setTextFormat(QtCore.Qt.PlainText)
        self.lblTiempo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTiempo.setObjectName("lblTiempo")
        self.lblTiempo.adjustSize()
        self.horizontalLayout_7.addWidget(self.lblTiempo)
        # self.lblTempPista = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.lblTempPista.setMinimumSize(QtCore.QSize(200, 25))
        # font = QtGui.QFont()
        # font.setFamily("Bahnschrift Light SemiCondensed")
        # font.setPointSize(16)
        # self.lblTempPista.setFont(font)
        # self.lblTempPista.setTextFormat(QtCore.Qt.PlainText)
        # self.lblTempPista.setAlignment(QtCore.Qt.AlignCenter)
        # self.lblTempPista.setObjectName("lblTempPista")
        # self.horizontalLayout_7.addWidget(self.lblTempPista)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(16)
        self.lwPosiciones = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lwPosiciones.setObjectName("lwPosiciones")
        self.lwPosiciones.setFont(font)
        self.verticalLayout.addWidget(self.lwPosiciones)
        #self.lblTempPista.adjustSize()
        self.verticalLayout.addWidget(self.lwPosiciones)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1162, 21))
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
        self.timer.start(500)  # Actualiza cada 1000 milisegundos (1 segundo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblSerie.setText(_translate("MainWindow", "European Endurance Pure Dribing School Series"))
        self.lblCar.setText(_translate("MainWindow", "Audi RS3 LMS"))
        self.lblCircuito.setText(_translate("MainWindow", "Weathertech Laguna Seca"))
        self.lblSOF.setText(_translate("MainWindow", "2000"))
        self.lblVueltas.setText(_translate("MainWindow", "12 / 24"))
        self.lblTiempo.setText(_translate("MainWindow", "15:00 / 30:00"))
        #self.lblTempPista.setText(_translate("MainWindow", "36º C"))

    gris = QColor(189, 195, 199)  # Color gris
    blanco = QColor(236, 240, 241)  # Color blanco
    ir = irsdk.IRSDK()
    ir.startup(test_file='datavuelta10.bin')
    if ir['PlayerCarIdx']:
        playerID = ir['PlayerCarIdx']
    if ir['WeekendInfo']['TrackID']:
        trackID = ir['WeekendInfo']['TrackID']
    if ir['DriverInfo']['Drivers'][playerID]['CarID']:
        carID = ir['DriverInfo']['Drivers'][playerID]['CarID']
    if ir['WeekendInfo']['SeriesID']:
        seriesID = ir['WeekendInfo']['SeriesID']
    totalLaps = ir['SessionInfo']['Sessions'][0]['SessionLaps']

    #Metodo para obtener el vehiculo de la bbdd
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
    
    #Metodo para obtener el nombre de la Serie de la bbdd
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
    
    #Metodo para obetner el nombre del circuito de la bbdd, sino lo encuentra, lo añade a la bbdd
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
    
    #Metodo para obtener la vuelta rapida de la bbdd
    def getVueltaRapidaDB(self):
        conn = sql.connect("iRacing.db")
        cursor = conn.cursor()
        query = f"SELECT Tiempo FROM VueltaRapida WHERE IDCircuito = {self.trackID} AND IDVehiculo = {self.carID}"
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        if(data == None):
            return 0
        else:
            return data[0]

    #Metodo para cargar los datos que son fijos durante toda la carrera
    def cargarDatosFijos(self):
        if Standings.getSerieDB(self) != 0:     #Buscamos el nombre de la serie en la bbdd
             self.lblSerie.setText(Standings.getSerieDB(self))
        if Standings.getCarDB(self) != 0:       #Buscamos el nombre del coche en la bbdd
             self.lblCar.setText(Standings.getCarDB(self))
        if Standings.getCircuitoDB(self) != 0:  #Buscamos el nombre del circuito en la bbdd
            self.lblCircuito.setText(Standings.getCircuitoDB(self))

        #Calculo del SOF de la partida, esto solo se calcula cuando la sesion es del tipo RACE
        if len(self.ir['SessionInfo']['Sessions']) == 3:
            participantes = self.ir['DriverInfo']['Drivers']
            totaliR = 0
            for i in participantes:
                if i['CarIdx'] == 0:
                    pass
                else:
                    totaliR += i['IRating']
            self.lblSOF.setText("{0:.0f}".format(totaliR / (len(participantes) - 1)))

    #Metodo para añadir cero delante de los segundos si hay de 0 a 9 segundos
    def agregar_cero_si_es_necesario(self, valor):      
        return f"{valor:02d}"

    #Metodo para convertir el tiempo de vuelta(segundos) en un string mm:ss:ms
    def convertirVueltas(self, vuelta):     
        minutos, segundos_sobrantes = divmod(float(vuelta), 60)
        tiempo = self.agregar_cero_si_es_necesario(int(minutos)) + ":{0:.3f}".format(segundos_sobrantes)
        return tiempo

    #Metodo para cargar los datos varian durante la carrera
    def cargarDatosVariables(self):
        self.lwPosiciones.clear()
        sesion = 0
    # Obtén los datos de la posición de los participantes comprobando en que sesion estamos
        if len(self.ir['SessionInfo']['Sessions']) == 3:
            participantes = self.ir['SessionInfo']['Sessions'][2]['ResultsPositions']
            sesion = 2
        elif len(self.ir['SessionInfo']['Sessions']) == 2:
            participantes = self.ir['SessionInfo']['Sessions'][1]['ResultsPositions']
            sesion = 1
        elif len(self.ir['SessionInfo']['Sessions']) == 1:
            participantes = self.ir['SessionInfo']['Sessions'][0]['ResultsPositions']
            sesion = 0
        else:
            participantes = None
        #Tiempo de sesion
        tTotal = self.ir['SessionInfo']['Sessions'][sesion]['SessionTime']
        tTotal = tTotal.split()
        tTotalFrm = self.convertirVueltas(tTotal[0])
        tTotal = float(tTotal[0])
        
        tTranscurrido = self.convertirVueltas(self.ir['SessionTime'])
        self.lblTiempo.setText(str(tTranscurrido) + " / " + str(tTotalFrm))

        #Calculo vueltas de carrera
        if self.ir['SessionInfo']['Sessions'][sesion]['SessionLaps'] ==  'unlimited':
            if Standings.getVueltaRapidaDB(self) != 0:
                vRapida = Standings.getVueltaRapidaDB(self)
                vTotales = tTotal/vRapida
            else:
                estLap = self.ir['DriverInfo']['Drivers'][self.playerID]['CarClassEstLapTime']
                vTotales = tTotal/estLap
        else:
            vTotales = self.ir['SessionInfo']['Sessions'][sesion]
        self.lblVueltas.setText(str(self.ir['Lap']) + "/" + "{0:.2f}".format((vTotales)) )        

    # Ordena los participantes por su posición en la carrera
        if participantes != None:
            for i in participantes:                
                posicion = str(i['Position'])
                #Añadimos espacios detras de posicion para separarlo del resto del string
                while len(posicion) < 5:    
                    posicion += " "

                #Añadimos el nombre del piloto, en caso de no tener nombre abreviado, añadimos el nombre completo
                nombre = self.ir['DriverInfo']['Drivers'][i['CarIdx']]['AbbrevName']
                if nombre == "":
                    nombre = self.ir['DriverInfo']['Drivers'][i['CarIdx']]['UserName']
                
                #Añadimos espeacios en blanco detras
                while len(nombre) < 17:
                    nombre += " "
                safety = self.ir['DriverInfo']['Drivers'][i['CarIdx']]['LicString']
                iRating = str(self.ir['DriverInfo']['Drivers'][i['CarIdx']]['IRating'])
                #Añadimos espeacios en blanco detras
                while len(iRating) < 8:
                    iRating += " "
                vRapida = str(i['FastestTime'])
                vRapida = self.convertirVueltas(vRapida)
                uVuelta = str(i['LastTime'])
                uVuelta = self.convertirVueltas(uVuelta)

                #Añadimos todos los datos del piloto al QlistWidget y mostramos por pantalla
                item = QListWidgetItem(posicion + nombre + safety + "    " + iRating + vRapida + "    " + uVuelta)
                self.lwPosiciones.addItem(item)
                
                #Pintamos

                if int(posicion) % 2 == 0:
                    brush = QBrush(self.blanco)
                else:
                    brush = QBrush(self.gris)
                
                item.setData(Qt.BackgroundRole, brush)
        #else:

        #Mostramos combustible actual
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Standings()
    ui.setupUi(MainWindow)
    ui.cargarDatosFijos()
    ui.cargarDatosVariables()
    MainWindow.show()

    sys.exit(app.exec_())
