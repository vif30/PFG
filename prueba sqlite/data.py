import sqlite3 as sql

# Establecer la conexión con la base de datos
conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
cursor = conn.cursor()
#query = f"INSERT INTO VueltaRapida (IDCircuito, IDVehiculo, MediaConsumo) VALUES ({self.trackID}, {self.carID}, {self.avgFuel}"
query2 = f"SELECT COUNT(*) FROM VueltaRapida"
cursor.execute(query2)
data = cursor.fetchone()
conn.commit()
conn.close()
print(data[0])