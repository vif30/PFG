import sqlite3 as sql

class Database(object):

    def getAVGFuelDB(trackID, carID):
        conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
        cursor = conn.cursor()
        query = f"SELECT MediaConsumo FROM VueltaRapida WHERE IDCircuito = {trackID} AND IDVehiculo = {carID}"
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        if(data == None):
            return 0
        else:
            return data[0]
    
    #Metodo para obtener el vehiculo de la bbdd    
    def getCarDB(carID):
        conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
        cursor = conn.cursor()
        cursor = conn.cursor()
        query = f"SELECT Marca, Modelo FROM Vehiculos WHERE IDVehiculo = {carID}"
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        if(data == None):
            return 0
        else:
            return data[0] + " " + data[1]
    
    #Metodo para obtener el nombre de la Serie de la bbdd
    def getSerieDB(serieID):
             conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
             cursor = conn.cursor()
             query = f"SELECT Nombre FROM Series WHERE IDSerie = {serieID}"
             cursor.execute(query)
             data = cursor.fetchone()
             conn.commit()
             conn.close()
             if(data == None):
                 return 0
             else:
                 return data[0]
    
    #Metodo para obetner el nombre del circuito de la bbdd, sino lo encuentra, lo añade a la bbdd
    def getCircuitoDB(trackID):
        conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
        cursor = conn.cursor()
        query = f"SELECT Nombre FROM Circuitos WHERE IDCircuito = {trackID}"
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        if(data == None):
            return 0
        else:
            return data[0]
    
    def insertNuevoCircuito(trackID, trackName, TrackCountry, TrackCity, TrackLengthOfficial, TrackConfigName):
        conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
        cursor = conn.cursor()
        query = f"""INSERT INTO Circuitos (IDCircuito, Nombre, Pais, Ciudad, Longitud, Variante, Comprado) VALUES ({trackID}, '{trackName}', '{TrackCountry}', '{TrackCity}', '{TrackLengthOfficial}', '{TrackConfigName}', 1)"""
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        
    def getAVGFuelDB(trackID, carID):
            conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
            cursor = conn.cursor()
            query = f"SELECT MediaConsumo FROM VueltaRapida WHERE IDCircuito = {trackID} AND IDVehiculo = {carID}"
            cursor.execute(query)
            data = cursor.fetchone()
            conn.commit()
            conn.close()
            if(data == None):
                return 0
            else:
                return data[0]


        
    #Metodo para insertar en la bbdd la media de consumo
    def insertNewAvgFuel(trackID, carID, avgFuel):
            conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
            cursor = conn.cursor()
            query2 = f"SELECT COUNT(*) FROM VueltaRapida"
            cursor.execute(query2)
            data = cursor.fetchone()
            id = data[0] + 1
            query = f"INSERT INTO VueltaRapida (IDTiempo, IDCircuito, IDVehiculo, MediaConsumo) VALUES ({id}, {trackID}, {carID}, {avgFuel})"
            cursor.execute(query)
            conn.commit()
            conn.close()

    #Metodo para actualizar en la bbdd la media de consumo
    def updateAvgFuel(avgFuel, trackID, carID):
            conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
            cursor = conn.cursor()
            query = f"UPDATE VueltaRapida SET MediaConsumo = {avgFuel} WHERE IDCircuito = {trackID} AND IDVehiculo = {carID}"
            cursor.execute(query)
            conn.commit()
            conn.close()

    #Metodo para obtener la vuelta rapida de la bbdd
    def getVueltaRapidaDB(trackID, carID):
        conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
        cursor = conn.cursor()
        query = f"SELECT Tiempo FROM VueltaRapida WHERE IDCircuito = {trackID} AND IDVehiculo = {carID}"
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        if(data == None or data[0] == None):
            return 0
        else:
            return data[0]
    #Método para actualizar el tiempo de la bbdd
    def updateVueltaRapidaDB(trackID, carID, vuelta):
        conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
        cursor = conn.cursor()
        query = f"UPDATE VueltaRapida SET Tiempo = {vuelta} WHERE IDCircuito = {trackID} AND IDVehiculo = {carID}"
        cursor.execute(query)
        conn.commit()
        conn.close()
    

if __name__ == "__main__":
    conn = sql.connect("C:/Users/izqui/Documents/GitHub/PFG/v3/data/iRacing.db")
    cursor = conn.cursor()
