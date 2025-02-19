import mysql.connector
from mysql.connector import pooling

# Configuración del pool de conexiones
db_config = {
    "host": "localhost",       # Cambia si usas un servidor remoto
    "port": 3309,              # Asegúrate de que es el puerto correcto
    "user": "root",            # Usuario de MySQL
    "password": "root",         # Contraseña del usuario
    "database": "tfg"       # Nombre de tu base de datos
}

# Crear el pool de conexiones
try:
    pool = pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size=10,  # Límite de conexiones en el pool
        **db_config
    )
    print("✅ Pool de conexiones MySQL creado correctamente.")
except mysql.connector.Error as err:
    print(f"❌ Error al crear el pool de conexiones: {err}")

# Función para obtener una conexión del pool
def get_connection():
    try:
        connection = pool.get_connection()
        print("🔄 Conexión obtenida del pool")
        return connection
    except mysql.connector.Error as err:
        print(f"❌ Error al obtener la conexión: {err}")
        return None

# Ejemplo de consulta
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES;")
        for db in cursor.fetchall():
            print(db)
        cursor.close()
        conn.close()
        print("🔒 Conexión cerrada")
