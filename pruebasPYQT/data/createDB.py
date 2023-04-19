import sqlite3 as sql

def createTable():
    conn = sql.connect("iRacing.db")
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO VueltaRapida VALUES
        (1, 47, 144, 86.375, 2.19),
        (2, 95, 144, 126.242, 3.39),
        (3, 403, 148, 95.500, 0.95)"""
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":

    createTable()