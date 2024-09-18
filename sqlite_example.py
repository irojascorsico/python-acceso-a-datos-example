import sqlite3

# Conectar a una base de datos en memoria
conexion = sqlite3.connect(":memory:")

# Crear un cursor para sentencias  SQL
cursor = conexion.cursor()

# Crear una tabla (si no existe)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
""")

# Insertar datos en la tabla
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Bob", 25))

# Consultar datos
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}")

# Cerrar la conexión (no es necesario en :memory:)
conexion.close()
