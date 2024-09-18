import mysql.connector
from mysql_conn import connect_to_mysql, logger 

conn = connect_to_mysql()

nombre="Maira"
edad="18"

if conn.is_connected:

    try:
        with conn.cursor() as cursor:
            query= "INSERT INTO usuarios (nombre, edad) VALUES (%s,%s)"
            cursor.execute(query, (nombre,edad))
            conn.commit()
            logger.info("Usuario registrado satisfactoriamente.")
    except mysql.connector.Error as err:
        logger.error(f"Error al insertar, {err}")
            