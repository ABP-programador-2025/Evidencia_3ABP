from db_config import get_db_connection

def ver_destinos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID_destino, Ciudad, Pais, costo_base FROM destinos")
    destinos = cursor.fetchall()
    if destinos:
        print("\nLista de destinos:")
        for destino in destinos:
            print(f"ID: {destino[0]}, Ciudad: {destino[1]}, País: {destino[2]}, Costo base: ${destino[3]}")
    else:
        print("No hay destinos registrados aún.")
    cursor.close()
    conn.close()

def agregar_destino():
    ciudad = input("Ingrese la ciudad: ")
    pais = input("Ingrese el país: ")
    costo_base = input("Ingrese el costo base: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO destinos (Ciudad, Pais, costo_base) VALUES (%s, %s, %s)",
        (ciudad, pais, costo_base)
    )
    conn.commit()
    print("Destino agregado correctamente.")
    cursor.close()
    conn.close()

def modificar_destino():
    id_destino = input("Ingrese el ID del destino a modificar: ")
    ciudad = input("Nueva ciudad: ")
    pais = input("Nuevo país: ")
    costo_base = input("Nuevo costo base: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE destinos SET Ciudad=%s, Pais=%s, costo_base=%s WHERE ID_destino=%s",
        (ciudad, pais, costo_base, id_destino)
    )
    conn.commit()
    print("Destino modificado correctamente.")
    cursor.close()
    conn.close()

def eliminar_destino():
    id_destino = input("Ingrese el ID del destino a eliminar: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM destinos WHERE ID_destino=%s", (id_destino,))
    conn.commit()
    print("Destino eliminado correctamente.")
    cursor.close()
    conn.close()