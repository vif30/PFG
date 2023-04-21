import sqlite3 as sql

def createTable():
    conn = sql.connect("iRacing.db")
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO VueltaRapida VALUES
        (4, 445, 144, 103.663, 2.51)"""
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
def dropTable():
    conn = sql.connect("iRacing.db")
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO VueltaRapida VALUES
        (1, 47, 144, 86.375, 2.19),
        (2, 95, 144, 126.242, 3.39),
        (3, 403, 148, 95.500, 0.95),
        (4, 445, 144, 103.663, 2.51)"""
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #dropTable()
    getAVGFuelDB(145, 445)