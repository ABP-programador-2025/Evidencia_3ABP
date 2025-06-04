from db_config import get_db_connection

def ver_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID_cliente, Nombre_razonsocial, DNI_CUIT, Correo_contacto FROM clientes")
    clientes = cursor.fetchall()
    if clientes:
        print("\nLista de clientes:")
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nombre/Razón Social: {cliente[1]}, DNI/CUIT: {cliente[2]}, Correo: {cliente[3]}")
    else:
        print("No hay clientes registrados aún.")
    cursor.close()
    conn.close()

def agregar_cliente():
    nombre_razonsocial = input("Ingrese el nombre o razón social: ")
    dni_cuit = input("Ingrese el DNI o CUIT: ")
    correo_contacto = input("Ingrese el correo de contacto: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clientes (Nombre_razonsocial, DNI_CUIT, Correo_contacto) VALUES (%s, %s, %s)",
        (nombre_razonsocial, dni_cuit, correo_contacto)
    )
    conn.commit()
    print("Cliente agregado correctamente.")
    cursor.close()
    conn.close()

def modificar_cliente():
    id_cliente = input("Ingrese el ID del cliente a modificar: ")
    nombre_razonsocial = input("Nuevo nombre o razón social: ")
    dni_cuit = input("Nuevo DNI o CUIT: ")
    correo_contacto = input("Nuevo correo de contacto: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE clientes SET Nombre_razonsocial=%s, DNI_CUIT=%s, Correo_contacto=%s WHERE ID_cliente=%s",
        (nombre_razonsocial, dni_cuit, correo_contacto, id_cliente)
    )
    conn.commit()
    print("Cliente modificado correctamente.")
    cursor.close()
    conn.close()

def eliminar_cliente():
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE ID_cliente=%s", (id_cliente,))
    conn.commit()
    print("Cliente eliminado correctamente.")
    cursor.close()
    conn.close()