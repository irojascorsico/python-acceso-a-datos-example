import mysql.connector
from mysql_conn import connect_to_mysql, logger 

conn = connect_to_mysql()

usuarios=[
    ("Camila", 12),
    ("Verónica", 27),
    ("Gabriel", 45)
]

if conn.is_connected:

    try:
        with conn.cursor() as cursor:
            query= "INSERT INTO usuarios (nombre, edad) VALUES (%s,%s)"
            cursor.executemany(query, usuarios)
            conn.commit()
            logger.info("Usuarios registrados satisfactoriamente.")
    except mysql.connector.Error as err:
        logger.error(f"Error al insertar, {err}")