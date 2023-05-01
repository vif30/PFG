import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class VentanaDialogo(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1162, 730)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1161, 731))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lblSerie_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblSerie_3.setFont(font)
        self.lblSerie_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSerie_3.setObjectName("lblSerie_3")
        self.horizontalLayout_9.addWidget(self.lblSerie_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lblCar_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCar_2.sizePolicy().hasHeightForWidth())
        self.lblCar_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblCar_2.setFont(font)
        self.lblCar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCar_2.setObjectName("lblCar_2")
        self.horizontalLayout_10.addWidget(self.lblCar_2)
        self.lblCircuito_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblCircuito_2.setFont(font)
        self.lblCircuito_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCircuito_2.setObjectName("lblCircuito_2")
        self.horizontalLayout_10.addWidget(self.lblCircuito_2)
        self.lblSOF_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblSOF_2.setMinimumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblSOF_2.setFont(font)
        self.lblSOF_2.setTextFormat(QtCore.Qt.PlainText)
        self.lblSOF_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSOF_2.setObjectName("lblSOF_2")
        self.horizontalLayout_10.addWidget(self.lblSOF_2)
        self.lblVueltas_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblVueltas_2.setMinimumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblVueltas_2.setFont(font)
        self.lblVueltas_2.setTextFormat(QtCore.Qt.PlainText)
        self.lblVueltas_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVueltas_2.setObjectName("lblVueltas_2")
        self.horizontalLayout_10.addWidget(self.lblVueltas_2)
        self.lblTiempo_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblTiempo_2.setMinimumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblTiempo_2.setFont(font)
        self.lblTiempo_2.setTextFormat(QtCore.Qt.PlainText)
        self.lblTiempo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTiempo_2.setObjectName("lblTiempo_2")
        self.horizontalLayout_10.addWidget(self.lblTiempo_2)
        self.lblTempPista_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblTempPista_2.setMinimumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.lblTempPista_2.setFont(font)
        self.lblTempPista_2.setTextFormat(QtCore.Qt.PlainText)
        self.lblTempPista_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTempPista_2.setObjectName("lblTempPista_2")
        self.horizontalLayout_10.addWidget(self.lblTempPista_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.lwPosiciones_2 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lwPosiciones_2.setObjectName("lwPosiciones_2")
        self.verticalLayout_2.addWidget(self.lwPosiciones_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblSerie_3.setText(_translate("Dialog", "European Endurance Pure Dribing School Series"))
        self.lblCar_2.setText(_translate("Dialog", "Audi RS3 LMS"))
        self.lblCircuito_2.setText(_translate("Dialog", "Weathertech Laguna Seca"))
        self.lblSOF_2.setText(_translate("Dialog", "2000"))
        self.lblVueltas_2.setText(_translate("Dialog", "12 / 24"))
        self.lblTiempo_2.setText(_translate("Dialog", "15:00 / 30:00"))
        self.lblTempPista_2.setText(_translate("Dialog", "36º C"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui2 = VentanaDialogo()
#     ui2.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

    def __init__(self, parent=None):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui2 = VentanaDialogo()
        ui2.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
    
    def abrir_ventana(self):
#        VentanaPrincipal()
        self.ventanaPrincipal = VentanaPrincipal()               # +++
        self.ventanaPrincipal.show()                             # +++
        self.hide()                                              # +++


class VentanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        self.setWindowTitle("VentanaPrincipal")
        
        self.centerWidget = QWidget()
        self.setCentralWidget(self.centerWidget)

        self.label = QLabel("Hello World", alignment=Qt.AlignHCenter)
        layout = QVBoxLayout(self.centerWidget)
        layout.addWidget(self.label)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaDialogo()
    window.show()
    sys.exit(app.exec_())