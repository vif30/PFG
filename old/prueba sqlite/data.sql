        CREATE TABLE Vehiculos (
                IDVehiculo INTEGER NOT NULL PRIMARY KEY,
                Modelo TEXT,
                Categoria TEXT,
                Legacy INTEGER,
                Comprado INTEGER
        )
        CREATE TABLE Circuitos (
                IDCircuito INTEGER NOT NULL PRIMARY KEY,
                Nombre TEXT,
                Pais TEXT,
                Ciudad TEXT,
                Longitud TEXT,
                Variante TEXT,
                Legacy INTEGER,
                Comprado INTEGER
        )
        CREATE TABLE VueltaRapida (
                IDTiempo INTEGER NOT NULL PRIMARY KEY,
                IDCircuito INTEGER,
                IDVehiculo INTEGER,
                Tiempo REAL,
                MediaConsumo REAL,
                FOREIGN KEY(IDCircuito) REFERENCES Circuitos(IDCircuito),
                FOREIGN KEY(IDVehiculo) REFERENCES Vehiculos(IDVehiculo)
        )
        INSERT INTO  Circuitos VALUES
        (95, 'Sebring International Raceway', 'USA', 'Sebring, Florida', '5.95 km', 'International', 0, 1),
        (96, 'Sebring International Raceway', 'USA', 'Sebring, Florida', '3.17 km', 'Modified', 0, 1),
        (97, 'Sebring International Raceway', 'USA', 'Sebring, Florida', '2.81 km', 'Club', 0, 1),
        (47, 'Weathertech Raceway at Laguna Seca', 'USA', 'Monterey, California', '3.60 km', 'Full Course', 0, 1),
        (432, 'Watkins Glen International', 'USA', 'Watkins Glen, New York', '3.89 km', 'Classic', 0, 1),
        (433, 'Watkins Glen International', 'USA', 'Watkins Glen, New York', '3.94 km', 'Cup', 0, 1),
        (434, 'Watkins Glen International', 'USA', 'Watkins Glen, New York', '5.55 km', 'Boot', 0, 1),
        (435, 'Watkins Glen International', 'USA', 'Watkins Glen, New York', '5.43 km', 'Classic Boot', 0, 1),
        (403, 'Red Bull Ring', 'Austria', 'Spielberg', '4.31 km', 'Grand Prix', 0, 1),
        (404, 'Red Bull Ring', 'Austria', 'Spielberg', '2.33 km', 'National', 0, 1),
        (407, 'Red Bull Ring', 'Austria', 'Spielberg', '1.83 km', 'North', 0, 1),
        (444, 'Fuji International Speedway', 'Japan', 'Oyama, Sunto District, Shizuoka', '4.55 km', 'Grand Prix', 0, 1),
        (445, 'Fuji International Speedway', 'Japan', 'Oyama, Sunto District, Shizuoka', '4.48 km', 'No chicane', 0, 1)

        INSERT INTO Vehiculos VALUES
        (1, 'Skip Barber Formula 2000', 'Skip Barber', 0, 1),
        (67, 'Mazda MX-5 Cup', 'MX-5 Cup', 0, 1),
        (112, 'Audi RS3 LMS', 'TCR', 0, 1),
        (119, 'Porsche 718 Cayman GT4 Clubsport MR', 'GT4', 0, 1),
        (144, 'Ferrari 488 GT3 Evo 2020', 'GT3', 0, 1),
        (148, 'iRacing iR-04', 'F4', 0, 1),
        (160, 'Toyota GR86', 'GR86', 0, 1)

        INSERT INTO VueltaRapida VALUES
        (1, 47, 144, 86.375, 2.19),
        (2, 95, 144, 126.242, 3.39),
        (3, 403, 148, 95.500, 0.95),
        (4, 445, 144, 103.663, 2.51)