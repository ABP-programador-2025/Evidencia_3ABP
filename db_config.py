import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="skyroute"
    )

# Ejemplo de uso
if __name__ == "__main__":
    conn = get_db_connection()

    if conn.is_connected():
        print("Conexión exitosa a la base de datos.")
    else:
        print("Error al conectar a la base de datos.")
    conn.close()