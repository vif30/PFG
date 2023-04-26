import sqlite3 as sql

def createTables():
    conn = sql.connect(r"iRacing.db")
    cursor = conn.cursor()
    createTables = {
    """CREATE TABLE Vehiculos (
    IDVehiculo INTEGER NOT NULL PRIMARY KEY,
    Marca TEXT,
    Modelo TEXT,
    Categoria TEXT,
    Consumo REAL,
    Legacy INTEGER,
    Comprado INTEGER)""",
    """CREATE TABLE Circuitos (
    IDCircuito INTEGER NOT NULL PRIMARY KEY,
    Nombre TEXT,
    Pais TEXT,
    Ciudad TEXT,
    Longitud TEXT,
    NVariante INTEGER,
    Variante TEXT,
    Legacy INTEGER,
    Comprado INTEGER)""",
    """CREATE TABLE VueltaRapida (
    IDTiempo INTEGER NOT NULL PRIMARY KEY,
    IDCircuito INTEGER,
    IDVehiculo INTEGER,
    Tiempo REAL,
    MediaConsumo REAL,
    FOREIGN KEY(IDCircuito) REFERENCES Circuitos(IDCircuito),
    FOREIGN KEY(IDVehiculo) REFERENCES Vehiculos(IDVehiculo))""",
    """CREATE TABLE Series (
    IDSerie INTEGER NOT NULL PRIMARY KEY,
    Nombre TEXT,
    Clase TEXT)""",
    }
    
    for i in createTables:
        cursor.execute(i)
    conn.commit()
    conn.close()

def insertData():
    conn = sql.connect(r"iRacing.db")
    cursor = conn.cursor()
    insertData = {
        """INSERT INTO  Circuitos VALUES
    (95, 'Sebring International Raceway', 'USA', 'Sebring, Florida', '5.95 km', 1, 'International', 0, 1),
    (96, 'Sebring International Raceway', 'USA', 'Sebring, Florida', '3.17 km', 2, 'Modified', 0, 1),
    (97, 'Sebring International Raceway', 'USA', 'Sebring, Florida', '2.81 km', 1, 'Club', 0, 1),
    (47, 'Weathertech Raceway at Laguna Seca', 'USA', 'Monterey, California', '3.60 km', 1, 'Full Course', 0, 1),
    (432, 'Watkins Glen International', 'USA', 'Watkins Glen, New York', '3.89 km', 1, 'Classic', 0, 1),
    (433, 'Watkins Glen International', 'USA', 'Watkins Glen, New York', '3.94 km', 2, 'Cup', 0, 1),
    (434, 'Watkins Glen International', 'USA', 'Watkins Glen, New York', '5.55 km', 3, 'Boot', 0, 1),
    (435, 'Watkins Glen International', 'USA', 'Watkins Glen, New York', '5.43 km', 4, 'Classic Boot', 0, 1),
    (403, 'Red Bull Ring', 'Austria', 'Spielberg', '4.31 km', 1, 'Grand Prix', 0, 1),
    (404, 'Red Bull Ring', 'Austria', 'Spielberg', '2.33 km', 2, 'National', 0, 1),
    (407, 'Red Bull Ring', 'Austria', 'Spielberg', '1.83 km', 3, 'North', 0, 1),
    (444, 'Fuji International Speedway', 'Japan', 'Oyama, Sunto District, Shizuoka', '4.55 km', 1, 'Grand Prix', 0, 1),
    (445, 'Fuji International Speedway', 'Japan', 'Oyama, Sunto District, Shizuoka', '4.48 km', 1, 'No chicane', 0, 1)""",
    """INSERT INTO Vehiculos VALUES
    (1, 'Skip Barber', 'Formula 2000', 'Skip Barber', 0.0, 0, 1),
    (67, 'Mazda', 'MX-5 Cup', 'MX-5 Cup', 0.0, 0, 1),
    (112, 'Audi', 'RS3 LMS', 'TCR', 0.0, 0, 1),
    (119, 'Porsche', '718 Cayman GT4 Clubsport MR', 'GT4', 0.0, 0, 1),
    (144, 'Ferrari', '488 GT3 Evo 2020', 'GT3', 3.83, 0, 1),
    (148, 'iRacing', 'iR-04', 'F4', 0.0, 0, 1),
    (160, 'Toyota', 'GR86', 'GR86', 0.0, 0, 1)""",
    """INSERT INTO VueltaRapida VALUES
    (1, 47, 144, 86.375, 2.19),
    (2, 95, 144, 126.242, 3.39),
    (3, 403, 148, 95.500, 0.95),
    (4, 445, 144, 103.663, 2.51)""",
    """INSERT INTO Series VALUES 
    (353, 'Ferrari GT3 Challenge - Fixed', 'D'),
    (112, 'Production Car Sim-Lab Challenge', 'D'),
    (491, 'GT4 Falken Tyre Challenge - Fixed', 'D'),
    (65, 'Classic Lotus Grand Prix', 'C'),
    (455, 'Formula Vee SIMAGIC', 'R'),
    (430, 'Touring Car Turn Racing Challenge - Fixed', 'D'),
    (498, 'Formula D - Ricmotech IR-04 Challenge - Fixed', 'D'),
    (63, 'Spec Racer Ford Challenge', 'D'),
    (476, 'Porsche Cup - Fixed', 'C'),
    (447, 'IMSA iRacing Series', 'B'),
    (521, 'Formula 1600 Trophy', 'D'),
    (139, 'Global Mazda MX-5 Fanatec Cup', 'R'),
    (505, 'Mission R Challenge - Fixed', 'D'),
    (74, 'Radical Racing Challenge', 'C'),
    (285, 'Kamel GT Championship', 'C'),
    (414, 'US Open Wheel C - Indy Pro 2000 Series', 'C'),
    (448, 'European Sprint Pure Driving School Series', 'A'),
    (484, 'Formula A - Grand Prix Series', 'A'),
    (519, 'iRacing Clio Cup - Fixed', 'D'),
    (514, 'GR Buttkicker Cup - Fixed', 'D'),
    (34, 'Skip Barber Race Series', 'D'),
    (431, 'Formula C - DOF Reality Dallara F3 Series', 'C'),
    (399, 'Supercars Series', 'C'),
    (520, 'Formula 1600 Rookie Series - Fixed', 'R'),
    (231, 'Advanced Mazda MX-5 Cup Series', 'C'),
    (437, 'BMW M Sim Cup', 'D'),
    (451, 'Creventic Endurance Series', 'C'),
    (429, 'Dallara Formula iR - Fixed', 'C'),
    (331, 'European Endurance Pure Driving School Series', 'A'),
    (260, 'Formula A - Grand Prix Series', 'A'),
    (495, 'Formula A - Grand Prix Tour', 'C'),
    (496, 'Formula A - Grand Prix Tour - Fixed', 'C'),
    (359, 'Formula B - Formula Renault 3.5 Series', 'B'),
    (456, 'Formula C - Moza Racing Dallara F3 Series - Fixed', 'C'),
    (497, 'Formula D - Ricmotech IR-04 Challenge', 'D'),
    (210, 'Fanatec Global Challenge', 'D'),
    (201, 'Grand Prix Legends', 'C'),
    (432, 'GT Challenge', 'C'),
    (237, 'GT Endurance VRS Series', 'C'),
    (228, 'GT Sprint VRS Series', 'B'),
    (444, 'GT3 Fanatec Challenge - Fixed', 'B'),
    (502, 'GT4 Falken Tyre Challenge', 'C'),
    (419, 'IMSA Endurance Series', 'B'),
    (492, 'IMSA Michelin Pilot Challenge Series', 'C'),
    (457, 'LMP2 Prototype Challenge - Fixed', 'B'),
    (275, 'Nurburgring Endurance Championship', 'D'),
    (299, 'Porsche Cup', 'C'),
    (314, 'Road America 500', 'C'),
    (493, 'Stock Car Brasil - Fixed', 'C'),
    (503, 'Touring Car Turn Racing Challenge', 'C'),
    (133, 'US Open Wheel B - Dallara IR-18', 'B'),
    (443, 'US Open Wheel D - Dallara IR-18', 'D')"""
    }
    for j in insertData:
        cursor.execute(j)
    conn.commit()
    conn.close()
if __name__ == "__main__":
    createTables()
    insertData()
