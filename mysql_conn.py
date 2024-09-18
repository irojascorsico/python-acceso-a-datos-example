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
            user='your_username',
            password='your_password',
            host='your_host',
            database='your_data_base_name',
            port="your_port"
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Usuario o Password no válido")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("La base de datos no existe.")
        else:
            logger.error(err)
    return None

