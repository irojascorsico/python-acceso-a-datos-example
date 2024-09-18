import mysql.connector
from mysql_conn import connect_to_mysql, logger 

conn = connect_to_mysql()

id=1

if conn.is_connected:

    try:
        with conn.cursor() as cursor:
            query= "DELETE FROM usuarios WHERE id=%s"
            cursor.execute(query, (id,))
            conn.commit()
            logger.info("Usuario eliminado satisfactoriamente.")
    except mysql.connector.Error as err:
        logger.error(f"Error al eliminar, {err}")