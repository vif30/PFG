        CREATE TABLE Vehiculos (
        IDVehiculo INTEGER NOT NULL PRIMARY KEY,
        Marca TEXT,
        Modelo TEXT,
        Categoria TEXT,
        Consumo REAL,
        Legacy INTEGER,
        Comprado INTEGER
        )
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
        )
        CREATE TABLE VueltaRapida (
        IDTiempo INTEGER NOT NULL PRIMARY KEY,
        IDCircuito INTEGER,
        IDVehiculo INTEGER,
        Tiempo REAL,
        MediaConsumo TEXT,
        FOREIGN KEY(IDCircuito) REFERENCES Circuitos(IDCircuito),
        FOREIGN KEY(IDVehiculo) REFERENCES Vehiculos(IDVehiculo)
        )
        INSERT INTO  Circuitos VALUES
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
        (407, 'Red Bull Ring', 'Austria', 'Spielberg', '1.83 km', 3, 'North', 0, 1)

        INSERT INTO Vehiculos VALUES
        (144, 'Ferrari', '488 GT3 Evo 2020', 'GT3', 3.83, 0, 1)
