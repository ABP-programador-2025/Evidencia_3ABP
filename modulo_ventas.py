from db_config import get_db_connection
from datetime import datetime

def ver_ventas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.ID_venta, c.Nombre_razonsocial, d.Ciudad, d.Pais, v.Fecha_venta, v.Estado, v.Costo_total, v.Fecha_anulacion
        FROM ventas v
        JOIN clientes c ON v.ID_cliente = c.ID_cliente
        JOIN destinos d ON v.ID_destino = d.ID_destino
    """)
    ventas = cursor.fetchall()
    if ventas:
        print("\nLista de ventas:")
        for v in ventas:
            print(
                f"ID: {v[0]}, "
                f"Cliente: {v[1]}, "
                f"Destino: {v[2]}, {v[3]}, "
                f"Fecha: {v[4]}, "
                f"Estado: {v[5]}, "
                f"Total: ${v[6]}, "
                f"Fecha de anulación: {v[7] if v[7] else 'N/A'}"
            )
    else:
        print("No hay ventas registradas aún.")
    cursor.close()
    conn.close()

def agregar_venta():
    id_cliente = input("Ingrese el ID del cliente: ")
    id_destino = input("Ingrese el ID del destino: ")
    costo_total = input("Ingrese el costo total: ")
    fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ventas (ID_cliente, ID_destino, Fecha_venta, Costo_total, Estado) VALUES (%s, %s, %s, %s, %s)",
        (id_cliente, id_destino, fecha_venta, costo_total, "Activa")
    )
    conn.commit()
    print("Venta agregada correctamente.")
    cursor.close()
    conn.close()

def anular_venta():
    limite_tiempo = 60
    unidad_tiempo = "dias"  # "dias" o "minutos"
    print(f"Para anular una venta, debe hacerlo dentro de {limite_tiempo} {unidad_tiempo} desde la fecha de venta. De lo contrario, no se podrá anular.")
    id_venta = input("Ingrese el ID de la venta a anular: ")


    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Fecha_venta FROM ventas WHERE ID_venta=%s", (id_venta,))
    resultado = cursor.fetchone()

    if resultado:
        fecha_venta = resultado[0]
        ahora = datetime.now()

        if unidad_tiempo == "dias":
            diferencia = (ahora - fecha_venta).days
        elif unidad_tiempo == "minutos":
            diferencia = int((ahora - fecha_venta).total_seconds() / 60)
        else:
            print("Unidad de tiempo no soportada.")
            cursor.close()
            conn.close()
            return

        print(f"Han pasado {diferencia} {unidad_tiempo} desde la venta.")

        if diferencia <= limite_tiempo:
            fecha_anulacion = datetime.now()
            cursor.execute(
                "UPDATE ventas SET Estado='Anulada', Fecha_anulacion=%s WHERE ID_venta=%s",
                (fecha_anulacion, id_venta)
            )
            conn.commit()
            print("Venta anulada correctamente.")
        else:
            print(f"No se puede anular la venta. Han pasado más de {limite_tiempo} {unidad_tiempo}.")
    else:
        print("Venta no encontrada.")

    cursor.close()
    conn.close()

def consultar_ventas_por_cliente():
    id_cliente = input("Ingrese el ID del cliente: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.ID_venta, d.Ciudad, d.Pais, v.Fecha_venta, v.Estado, v.Costo_total
        FROM ventas v
        JOIN destinos d ON v.ID_destino = d.ID_destino
        WHERE v.ID_cliente = %s
    """, (id_cliente,))
    ventas = cursor.fetchall()
    if ventas:
        print("\nVentas del cliente:")
        for v in ventas:
            print(f"ID: {v[0]}, Destino: {v[1]}, {v[2]}, Fecha: {v[3]}, Estado: {v[4]}, Total: ${v[5]:.2f}")
    else:
        print("No hay ventas para este cliente.")
    cursor.close()
    conn.close()

def consultar_ventas_por_destino():
    id_destino = input("Ingrese el ID del destino: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.ID_venta, c.Nombre_razonsocial, v.Fecha_venta, v.Estado, v.Costo_total
        FROM ventas v
        JOIN clientes c ON v.ID_cliente = c.ID_cliente
        WHERE v.ID_destino = %s
    """, (id_destino,))
    ventas = cursor.fetchall()
    if ventas:
        print("\nVentas para el destino:")
        for v in ventas:
            print(f"ID: {v[0]}, Cliente: {v[1]}, Fecha: {v[2]}, Estado: {v[3]}, Total: ${v[4]}")
    else:
        print("No hay ventas para este destino.")
    cursor.close()
    conn.close()

def consultar_ventas_anuladas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.ID_venta, c.Nombre_razonsocial, d.Ciudad, d.Pais, v.Fecha_venta, v.Costo_total, v.Fecha_anulacion
        FROM ventas v
        JOIN clientes c ON v.ID_cliente = c.ID_cliente
        JOIN destinos d ON v.ID_destino = d.ID_destino
        WHERE v.Estado = 'Anulada'
    """)
    ventas = cursor.fetchall()
    if ventas:
        print("\nVentas anuladas:")
        for v in ventas:
            print(f"ID: {v[0]}, Cliente: {v[1]}, Destino: {v[2]}, {v[3]}, Fecha de venta: {v[4]}, Total: ${v[5]}, Fecha de anulación: {v[6]}")
    else:
        print("No hay ventas anuladas.")
    cursor.close()
    conn.close()

def reporte_general_ventas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*), SUM(Costo_total) FROM ventas WHERE Estado='Activa'
    """)
    result = cursor.fetchone()
    print("\nReporte General de Ventas:")
    print(f"Total de ventas activas: {result[0]}")
    print(f"Total recaudado: ${result[1]}")
    cursor.close()
    conn.close()