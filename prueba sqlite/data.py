import sqlite3

# Establecer la conexión con la base de datos
conn = sqlite3.connect('iRacing.db')

# Crear un objeto Cursor
cursor = conn.cursor()

# Leer el contenido del archivo SQL
with open('data.sql', 'r') as archivo:
    contenido = archivo.read()

# Ejecutar el script SQL
cursor.executescript(contenido)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()