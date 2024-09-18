import mysql.connector
from mysql_conn import connect_to_mysql, logger 

conn = connect_to_mysql()

nombre="Rosario"
id=1

if conn.is_connected:

    try:
        with conn.cursor() as cursor:
            query= "UPDATE usuarios SET nombre=%s WHERE id=%s"
            cursor.execute(query, (nombre, id))
            conn.commit()
            logger.info("Usuario modificado satisfactoriamente.")
    except mysql.connector.Error as err:
        logger.error(f"Error al modificar, {err}")