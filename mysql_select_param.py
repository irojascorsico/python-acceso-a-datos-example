from mysql_conn import connect_to_mysql
import mysql

conn = connect_to_mysql()

if conn.is_connected:

    # Crear un cursor para sentencias  SQL
    cursor = conn.cursor()
    user_name="Alice"

    try:
            
        # Crear una consulta SQL
        query = "SELECT * FROM usuarios WHERE nombre =%s and edad>%s"

        # Ejecutar la consulta SQL
        cursor.execute(query, (user_name,18))

        # Iterar los registros obtenidos
        for fila in cursor.fetchall():
            print(f"Id: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}")

        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()