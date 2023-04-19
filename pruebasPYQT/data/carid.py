import irsdk

""" ir = irsdk.IRSDK()
ir.startup()

car_id = ir['DriverInfo']['Drivers'][0]['CarID']
print("El ID del vehículo seleccionado es:", car_id)

ir.shutdown() """

minutos, segundos_sobrantes = divmod(float(124.7344), 60)
print(minutos, segundos_sobrantes)