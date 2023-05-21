# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import QTimer, Qt
from database import Database
from iRData import iRData


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
        self.horizontalLayout_6.addWidget(self.lblSerie, 0, QtCore.Qt.AlignHCenter)
        self.lblCar = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCar.sizePolicy().hasHeightForWidth())
        self.lblCar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblCar.setFont(font)
        self.lblCar.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCar.setObjectName("lblCar")
        self.horizontalLayout_6.addWidget(self.lblCar, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblCircuito = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblCircuito.setMinimumSize(QtCore.QSize(400, 0))
        self.lblCircuito.setMaximumSize(QtCore.QSize(400, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblCircuito.setFont(font)
        self.lblCircuito.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCircuito.setObjectName("lblCircuito")
        self.horizontalLayout_7.addWidget(self.lblCircuito)
        self.lblSOF = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblSOF.setMinimumSize(QtCore.QSize(100, 25))
        self.lblSOF.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblSOF.setFont(font)
        self.lblSOF.setTextFormat(QtCore.Qt.PlainText)
        self.lblSOF.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSOF.setObjectName("lblSOF")
        self.horizontalLayout_7.addWidget(self.lblSOF)
        self.lblVueltas = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblVueltas.setMinimumSize(QtCore.QSize(200, 25))
        self.lblVueltas.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblVueltas.setFont(font)
        self.lblVueltas.setTextFormat(QtCore.Qt.PlainText)
        self.lblVueltas.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVueltas.setObjectName("lblVueltas")
        self.horizontalLayout_7.addWidget(self.lblVueltas)
        self.lblTiempo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblTiempo.setMinimumSize(QtCore.QSize(200, 25))
        self.lblTiempo.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblTiempo.setFont(font)
        self.lblTiempo.setTextFormat(QtCore.Qt.PlainText)
        self.lblTiempo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTiempo.setObjectName("lblTiempo")
        self.horizontalLayout_7.addWidget(self.lblTiempo, 0, QtCore.Qt.AlignHCenter)
        self.lblIncidentes = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblIncidentes.setMinimumSize(QtCore.QSize(150, 25))
        self.lblIncidentes.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblIncidentes.setFont(font)
        self.lblIncidentes.setTextFormat(QtCore.Qt.PlainText)
        self.lblIncidentes.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIncidentes.setObjectName("lblIncidentes")
        self.horizontalLayout_7.addWidget(self.lblIncidentes)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.lwPosiciones = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lwPosiciones.setObjectName("lwPosiciones")
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(18)
        self.lwPosiciones.setFont(font)
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
        self.timer.start(500)  # Actualiza cada 500 milisegundos (0.5 segundos)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblSerie.setText(_translate("MainWindow", "European Endurance Pure Dribing School Series"))
        self.lblCar.setText(_translate("MainWindow", "Audi RS3 LMS"))
        self.lblCircuito.setText(_translate("MainWindow", "Weathertech Laguna Seca"))
        self.lblSOF.setText(_translate("MainWindow", "2000"))
        self.lblVueltas.setText(_translate("MainWindow", "12 / 24"))
        self.lblTiempo.setText(_translate("MainWindow", "15:00 / 30:00"))
        self.lblIncidentes.setText(_translate("MainWindow", "7/17"))

    gris = QColor(189, 195, 199)  # Color gris
    blanco = QColor(236, 240, 241)  # Color blanco
    
    #Metodo para cargar los datos que son fijos durante toda la carrera
    def cargarDatosFijos(self):
        if Database.getSerieDB(iRData.seriesID) != 0:     #Buscamos el nombre de la serie en la bbdd
            self.lblSerie.setText(Database.getSerieDB(iRData.seriesID))
        if Database.getCarDB(iRData.carID) != 0:       #Buscamos el nombre del coche en la bbdd
            self.lblCar.setText(Database.getCarDB(iRData.carID))
        if Database.getCircuitoDB(iRData.trackID) != 0:  #Buscamos el nombre del circuito en la bbdd
            self.lblCircuito.setText(Database.getCircuitoDB(iRData.trackID))
        else:
            Database.insertNuevoCircuitoDB(iRData.trackID, iRData.ir['WeekendInfo']['TrackDisplayName'], iRData.ir['WeekendInfo']['TrackCountry'], iRData.ir['WeekendInfo']['TrackCity'], iRData.ir['WeekendInfo']['TrackLengthOfficial'], iRData.ir['WeekendInfo']['TrackConfigName'])
            self.lblCircuito.setText(Database.getCircuitoDB( self.trackID))

        #Calculo del SOF de la partida, esto solo se calcula cuando la sesion es del tipo RACE
        if len(iRData.ir['SessionInfo']['Sessions']) == 3:
            participantes = iRData.ir['DriverInfo']['Drivers']
            totaliR = 0
            for i in participantes:
                if i['CarIdx'] == 0:
                    pass
                else:
                    totaliR += i['IRating']
            self.lblSOF.setText("SOF: " + "{0:.0f}".format(totaliR / (len(participantes) - 1)))
        else:
            self.lblSOF.setText(" ")

    #Metodo para añadir cero delante de los segundos si hay de 0 a 9 segundos
    def agregar_cero_si_es_necesario(self, valor):      
        return f"{valor:02d}"

    #Metodo para convertir el tiempo de vuelta(segundos) en un string mm:ss:ms
    def convertirVueltas(self, vuelta):     
        minutos, segundos_sobrantes = divmod(float(vuelta), 60)
        segundos = str(segundos_sobrantes).split(".")

        tiempo = self.agregar_cero_si_es_necesario(int(minutos)) + ":" + self.agregar_cero_si_es_necesario(int(segundos[0])) + "." + segundos[1][0:3]
        return tiempo
    def convertirTiempo(self, vuelta):     
        minutos, segundos_sobrantes = divmod(float(vuelta), 60)
        tiempo = self.agregar_cero_si_es_necesario(int(minutos)) + ":" + self.agregar_cero_si_es_necesario(int(segundos_sobrantes))
        return tiempo

    #Metodo para cargar los datos varian durante la carrera
    def cargarDatosVariables(self):
        if not iRData.ir.is_connected:
            if self.playerFastLap != 0:
                if self.playerFastLap < Database.getVueltaRapidaDB(iRData.trackID, iRData.carID) or Database.getVueltaRapidaDB(iRData.trackID, iRData.carID) == 0:
                    Database.updateVueltaRapidaDB(iRData.trackID, iRData.carID, self.playerFastLap)
            sys.exit()
        self.lwPosiciones.clear()
        sesionName = ""
    # Obtén los datos de la posición de los participantes comprobando en que sesion estamos
        sesion = iRData.getSesion()
        participantes = iRData.getParticipantes(self)
        if sesion == 2:
            sesionName = "Race: "
        elif sesion == 1:
            sesionName = "Qualify: "
        elif sesion == 2:
            sesionName = "Practice: "
       
        #Tiempo de sesion
        tTotal = iRData.ir['SessionInfo']['Sessions'][sesion]['SessionTime']
        tTotal = tTotal.split()
        tTotalFrm = self.convertirTiempo(tTotal[0])
        tTotal = float(tTotal[0])
        
        tTranscurrido = self.convertirTiempo(iRData.ir['SessionTime'])
        tRestante = self.convertirTiempo(iRData.ir['SessionTimeRemain'])
        if tRestante == '-1:59':
            self.lblTiempo.setText(sesionName + str(tTranscurrido) + " / " + str(tTotalFrm))
        else:
            self.lblTiempo.setText(sesionName + str(tRestante) + " / " + str(tTotalFrm))

        #Calculo vueltas de carrera
        if iRData.getSesionLaps(self) ==  'unlimited':
            if Database.getVueltaRapidaDB(iRData.trackID, iRData.carID) != 0:
                vRapida = Database.getVueltaRapidaDB(self.trackID, self.carID)
                vTotales = tTotal/vRapida
            else:
                estLap = iRData.ir['DriverInfo']['Drivers'][iRData.playerID]['CarClassEstLapTime']
                vTotales = tTotal/estLap
            self.lblVueltas.setText("Lap: " + str(iRData.lap))
        else:
            vTotales = iRData.getSesionLaps(self)
            self.lblVueltas.setText("Lap: " + str(iRData.lap) + "/" + "{0:.0f}".format((vTotales)) )    
        #if sesion == 0:
         #   self.lblVueltas.setText("Lap: " + str(iRData.lap))
        #else:
         #   self.lblVueltas.setText("Lap: " + str(iRData.lap) + "/" + "{0:.2f}".format((vTotales)) )      

        if iRData.maxIncidents == 'unlimited':
            self.lblIncidentes.setText("X " + str(iRData.myIncidents))
        else:
            self.lblIncidentes.setText("X " + str(iRData.myIncidents) + "/" + str(iRData.maxIncidents))

    # Ordena los participantes por su posición en la carrera
        if participantes != None:
            for i in participantes:                
                posicion = str(i['Position'])
                #Añadimos espacios detras de posicion para separarlo del resto del string
                while len(posicion) < 5:    
                    posicion += " "

                #Añadimos el nombre del piloto, en caso de no tener nombre abreviado, añadimos el nombre completo
                nombre = iRData.ir['DriverInfo']['Drivers'][i['CarIdx']]['AbbrevName']
                if nombre == "":
                    nombre = iRData.ir['DriverInfo']['Drivers'][i['CarIdx']]['UserName']
                
                #Añadimos espeacios en blanco detras
                while len(nombre) < 20:
                    nombre += " "
                safety = iRData.ir['DriverInfo']['Drivers'][i['CarIdx']]['LicString']
                iRating = str(iRData.ir['DriverInfo']['Drivers'][i['CarIdx']]['IRating'])
                #Añadimos espeacios en blanco detras
                while len(iRating) < 8:
                    iRating += " "

                #Comprobamos si la vuelta rapida o la ultima vuelta del piloto son nulas, si es asi lo deja en blanco.
                if i['FastestTime'] == -1.0:
                    vRapida = "         "
                else:
                    vRapida = str(i['FastestTime'])
                    vRapida = self.convertirVueltas(vRapida)
                if i['LastTime'] == -1.0:
                    uVuelta = "         "
                else:
                    uVuelta = str(i['LastTime'])
                    uVuelta = self.convertirVueltas(uVuelta)

                #Añadimos todos los datos del piloto al QlistWidget y mostramos por pantalla
                item = QListWidgetItem(posicion + nombre + safety + "    " + iRating + vRapida + "    " + uVuelta)
                self.lwPosiciones.addItem(item)
                
                #Pintamos la linea del color correspondiente
                if int(posicion) % 2:
                    brush = QBrush(self.blanco)
                else:
                    brush = QBrush(self.gris)
                
                item.setData(Qt.BackgroundRole, brush)
                if i['CarIdx'] == iRData.playerID:
                    self.playerFastLap = i['FastestTime']



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Standings()
    if iRData.ir.is_connected:
        ui.setupUi(MainWindow)
        ui.cargarDatosFijos()
        ui.cargarDatosVariables()
        MainWindow.show()
        sys.exit(app.exec_())
    else:
        MainWindow.close()
        sys.exit()
