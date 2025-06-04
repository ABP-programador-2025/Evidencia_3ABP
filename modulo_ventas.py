from db_config import get_db_connection

def ver_ventas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.ID_venta, c.Nombre_razonsocial, d.Ciudad, d.Pais, v.Fecha_venta, v.Estado, v.Costo_total
        FROM ventas v
        JOIN clientes c ON v.ID_cliente = c.ID_cliente
        JOIN destinos d ON v.ID_destino = d.ID_destino
    """)
    ventas = cursor.fetchall()
    if ventas:
        print("\nLista de ventas:")
        for v in ventas:
            print(f"ID: {v[0]}, Cliente: {v[1]}, Destino: {v[2]}, {v[3]}, Fecha: {v[4]}, Estado: {v[5]}, Total: ${v[6]:.2f}")
    else:
        print("No hay ventas registradas aún.")
    cursor.close()
    conn.close()

def agregar_venta():
    id_cliente = input("Ingrese el ID del cliente: ")
    id_destino = input("Ingrese el ID del destino: ")
    costo_total = input("Ingrese el costo total: ")
    from datetime import datetime
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
    id_venta = input("Ingrese el ID de la venta a anular: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE ventas SET Estado='Anulada' WHERE ID_venta=%s", (id_venta,))
    conn.commit()
    print("Venta anulada correctamente.")
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
            print(f"ID: {v[0]}, Cliente: {v[1]}, Fecha: {v[2]}, Estado: {v[3]}, Total: ${v[4]:.2f}")
    else:
        print("No hay ventas para este destino.")
    cursor.close()
    conn.close()

def consultar_ventas_anuladas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.ID_venta, c.Nombre_razonsocial, d.Ciudad, d.Pais, v.Fecha_venta, v.Costo_total
        FROM ventas v
        JOIN clientes c ON v.ID_cliente = c.ID_cliente
        JOIN destinos d ON v.ID_destino = d.ID_destino
        WHERE v.Estado = 'Anulada'
    """)
    ventas = cursor.fetchall()
    if ventas:
        print("\nVentas anuladas:")
        for v in ventas:
            print(f"ID: {v[0]}, Cliente: {v[1]}, Destino: {v[2]}, {v[3]}, Fecha: {v[4]}, Total: ${v[5]:.2f}")
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
    print(f"Total recaudado: ${result[1] if result[1] else 0:.2f}")
    cursor.close()
    conn.close()