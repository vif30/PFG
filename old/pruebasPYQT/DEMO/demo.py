# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lblPhysics = QtWidgets.QLabel(Form)
        self.lblPhysics.setGeometry(QtCore.QRect(50, 30, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblPhysics.setFont(font)
        self.lblPhysics.setObjectName("lblPhysics")
        self.lblMath = QtWidgets.QLabel(Form)
        self.lblMath.setGeometry(QtCore.QRect(50, 90, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblMath.setFont(font)
        self.lblMath.setObjectName("lblMath")
        self.lblTotal = QtWidgets.QLabel(Form)
        self.lblTotal.setGeometry(QtCore.QRect(50, 210, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblTotal.setFont(font)
        self.lblTotal.setObjectName("lblTotal")
        self.btnAdd = QtWidgets.QPushButton(Form)
        self.btnAdd.setGeometry(QtCore.QRect(40, 160, 75, 23))
        self.btnAdd.setObjectName("btnAdd")
        self.etPhysics = QtWidgets.QLineEdit(Form)
        self.etPhysics.setGeometry(QtCore.QRect(200, 40, 113, 20))
        self.etPhysics.setObjectName("etPhysics")
        self.etMaths = QtWidgets.QLineEdit(Form)
        self.etMaths.setGeometry(QtCore.QRect(200, 100, 113, 20))
        self.etMaths.setObjectName("etMaths")
        self.etTotal = QtWidgets.QLineEdit(Form)
        self.etTotal.setGeometry(QtCore.QRect(200, 220, 113, 20))
        self.etTotal.setObjectName("etTotal")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblPhysics.setText(_translate("Form", "Physics"))
        self.lblMath.setText(_translate("Form", "Maths"))
        self.lblTotal.setText(_translate("Form", "Total"))
        self.btnAdd.setText(_translate("Form", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
