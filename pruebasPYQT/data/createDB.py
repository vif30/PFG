import sqlite3 as sql

def createTable():
    conn = sql.connect("iRacing.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Vehiculos (
    IDVehiculo INTEGER NOT NULL PRIMARY KEY,
    Marca TEXT,
    Modelo TEXT,
    Categoria TEXT,
    Consumo REAL,
    Legacy INTEGER,
    Comprado INTEGER
);

CREATE TABLE Circuitos (
    IDCircuito INTEGER NOT NULL PRIMARY KEY,
    Nombre TEXT,
    Pais TEXT,
    Ciudad TEXT,
    Longitud TEXT,
    NVariante INTEGER,
    Variante TEXT,
    Legacy INTEGER,
    Comprado INTEGER
);

CREATE TABLE VueltaRapida (
    IDTiempo INTEGER NOT NULL PRIMARY KEY,
    IDCircuito INTEGER,
    IDVehiculo INTEGER,
    Tiempo REAL,
    MediaConsumo REAL,
    FOREIGN KEY(IDCircuito) REFERENCES Circuitos(IDCircuito),
    FOREIGN KEY(IDVehiculo) REFERENCES Vehiculos(IDVehiculo)
);

CREATE TABLE Series (
    IDSerie INTEGER NOT NULL PRIMARY KEY,
    Nombre TEXT,
    Clase TEXT
);"""
    )
    conn.commit()
    conn.close()

def dropTable():
    conn = sql.connect("iRacing.db")
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE Series
        SET Clase = 'C'
        WHERE IDSerie = 285
        """
    )
    conn.commit()
    conn.close()
def getAVGFuelDB(IDVehiculo, IDCircuito):
    conn = sql.connect("iRacing.db")
    cursor = conn.cursor()
    query = f"SELECT MediaConsumo FROM VueltaRapida WHERE IDCircuito = {IDCircuito} AND IDVehiculo = {IDVehiculo}"
    cursor.execute(query)
    data = cursor.fetchone()
    conn.commit()
    conn.close()
    print(data[0])
if __name__ == "__main__":
    dropTable()
    #getAVGFuelDB(145, 445)