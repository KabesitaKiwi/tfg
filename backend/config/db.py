import mysql.connector
import os
from mysql.connector import pooling
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env

# Configuración del pool de conexiones
db_config = {
    "host": "localhost",       # Cambia si usas un servidor remoto
    "port": 3309,              # Asegúrate de que es el puerto correcto
    "user": "root",            # Usuario de MySQL
    "password": "root",         # Contraseña del usuario
    "database": "mi_tienda"       # Nombre de tu base de datos
}
# Crear el pool de conexiones
try:
    connection_pool = pooling.MySQLConnectionPool(**db_config)
    print("✅ Pool de conexiones creado correctamente")
except mysql.connector.Error as e:
    print(f"❌ Error al crear el pool de conexiones: {e}")
    connection_pool = None

# Función para obtener una conexión del pool
def get_connection():
    try:
        if connection_pool:
            return connection_pool.get_connection()
        else:
            print("⚠️ Pool de conexiones no disponible")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al obtener una conexión: {e}")
        return None

# Ejemplo de consulta
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        for db in cursor.fetchall():
            print(db)
        cursor.close()
        conn.close()
        print("🔒 Conexión cerrada")