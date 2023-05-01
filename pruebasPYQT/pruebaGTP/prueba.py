from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        botonCerrar = QPushButton('Cerrar', self)
        botonCerrar.setGeometry(50, 50, 100, 50)
        botonCerrar.clicked.connect(self.close)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        botonMostrar = QPushButton('Mostrar ventana', self)
        botonMostrar.clicked.connect(self.mostrarVentana)

        vbox = QVBoxLayout()
        vbox.addWidget(botonMostrar)

        self.setLayout(vbox)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Ventana principal')

    def mostrarVentana(self):
        ventana = Ventana()
        ventana.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaPrincipal = VentanaPrincipal()
    ventanaPrincipal.show()
    sys.exit(app.exec_())
