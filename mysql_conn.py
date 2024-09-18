import mysql.connector
import logging
from mysql.connector import errorcode

# Configuración del logger
logger = logging.getLogger("mysql.connector")
logger.setLevel(logging.INFO)  # Establece el nivel de registro (puedes ajustarlo según tus necesidades)

# Formateador para los mensajes de registro
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Manejador para mostrar los registros en la consola
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def connect_to_mysql():
    # Conectar a una base de datos MySQL Server
    try: 
        return mysql.connector.connect(
            user='root',
            password='1234',
            host='localhost',
            database='my_db'
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o Password no válido")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe.")
        else:
            print(err)
    return None

