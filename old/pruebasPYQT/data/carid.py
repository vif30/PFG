# import irsdk

# ir = irsdk.IRSDK()
# ir.startup()


# car_id = ir['SessionInfo']['Sessions'][0]['ResultsPositions'][1]['Time']
# print( car_id)

# ir.shutdown() 

from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget

# Creamos la aplicación
app = QApplication([])

# Creamos el widget principal
widget = QWidget()

# Creamos un layout vertical para el widget principal
layout = QVBoxLayout()

# Creamos el QListWidget y lo añadimos al layout
list_widget = QListWidget()
layout.addWidget(list_widget)

# Añadimos elementos al QListWidget
for i in range(10):
    item = QListWidgetItem(f"Elemento {i}")
    list_widget.addItem(item)

# Añadimos el layout al widget principal
widget.setLayout(layout)

# Mostramos el widget principal
widget.show()

# Ejecutamos la aplicación
app.exec_()