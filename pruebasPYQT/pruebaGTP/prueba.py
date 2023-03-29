import sys
import time
import irsdk
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Definir el tamaño y título de la ventana
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Mi aplicación con PyQt5')

        # Crear el Label
        self.lblRPM = QLabel('Revoluciones del motor: 0', self)
        self.lblID = QLabel('ID del coche del jugador: 0', self)
        self.lblMarcha = QLabel('Marcha engranada: 0', self)

        # Crear el botón y conectar su señal con la función que lo maneja
        self.boton = QPushButton('Mostrar Revoluciones', self)
        self.boton.clicked.connect(self.iniciar_actualizacion)

        # Crear el layout vertical y añadir los widgets a él
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.lblRPM)
        layout_vertical.addWidget(self.lblMarcha)
        layout_vertical.addWidget(self.lblID)
        layout_vertical.addWidget(self.boton)

        # Asignar el layout a la ventana principal
        self.setLayout(layout_vertical)

        # Inicializar el SDK de iRacing
        self.ir = irsdk.IRSDK()
        self.ir.startup()

        # Crear un temporizador y establecer su intervalo en 200 milisegundos
        self.timer = QTimer(self)
        self.timer.setInterval(200)

    def iniciar_actualizacion(self):
        if self.timer.isActive():
            # Si el temporizador está activo, detener la actualización
            self.timer.stop()
            self.boton.setText('Mostrar Revoluciones')
        else:
            # Si el temporizador no está activo, iniciar la actualización
            self.timer.timeout.connect(self.mostrar_revoluciones)
            self.timer.start()
            self.boton.setText('Detener')

    def mostrar_revoluciones(self):
        # Obtener las revoluciones del motor
        rpm = self.ir['RPM']
        id = self.ir['CarIdxBestLapTime'][28]
        for i in range(30):
            gear = self.ir['DriverInfo']['Drivers'][i]['UserName']
            print(gear)
        gear = self.ir['DriverInfo']['Drivers'][28]['UserName']
        # Actualizar el texto del Label con las revoluciones del motor
        self.lblRPM.setText('Revoluciones del motor: {:.0f}'.format(rpm))
        self.lblMarcha.setText(str(gear))
        vuelta = str(id)
        minutos, segundos_sobrantes = divmod(float(vuelta), 60)
        def agregar_cero_si_es_necesario(valor):
            return f"{valor:02d}"
        self.lblID.setText(agregar_cero_si_es_necesario(int(minutos)) + ":{0:.3f}".format(segundos_sobrantes))

    def getTiempos(segundos):
        def agregar_cero_si_es_necesario(valor):
            return f"{valor:02d}"
    
        minutos, segundos_sobrantes = divmod(float(segundos), 60)
        return (agregar_cero_si_es_necesario(int(minutos)) + ":{0:.3f}".format(segundos_sobrantes))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Crear la ventana principal
    ventana = MiVentana()
    ventana.show()
    
    sys.exit(app.exec_())
