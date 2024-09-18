from mysql_conn import connect_to_mysql

conn = connect_to_mysql()

if conn.is_connected:
# Crear un cursor para sentencias  SQL
    cursor = conn.cursor()

    # Crear una consulta SQL
    query = "SELECT * FROM usuarios"

    # Ejecutar la consulta SQL
    cursor.execute(query)

    # Iterar los registros obtenidos
    for fila in cursor.fetchall():
        print(f"Id: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}")

    cursor.close()
    conn.close()