# import from modulos/
from modulo_clientes import ver_clientes, agregar_cliente, modificar_cliente, eliminar_cliente
from modulo_destinos import ver_destinos, agregar_destino, modificar_destino, eliminar_destino
from modulo_ventas import (
    ver_ventas, agregar_venta, anular_venta,
    consultar_ventas_por_cliente, consultar_ventas_por_destino,
    consultar_ventas_anuladas, reporte_general_ventas
)

opcion_menu_principal = ""

while opcion_menu_principal != "x":
    print("\033[1;36m  🛫   SkyRoute S.R.L.  🛬\033[0m")
    print("═════════════════════════════")
    print("1️  Gestionar Clientes")
    print("2️  Gestionar Destinos")
    print("3️  Gestionar Ventas")
    print("4️  Consultar Ventas")
    print("5️  Ver Reporte General")
    print("🅱️  Botón de Arrepentimiento")
    print("ℹ️  Acerca del Sistema")
    print("❎ Salir")

    opcion_menu_principal = input("\nIngrese una opción: ")

    # menu de gestión de clientes
    if opcion_menu_principal == "1":
        opcion_clientes = ""
        while opcion_clientes != "x":
            print("\033[1;36m  🛫   Gestión Clientes  🛬\033[0m")
            print("═════════════════════════════")
            print("1️  Ver Clientes")
            print("2️  Agregar Cliente")
            print("3️  Modificar Cliente")
            print("4️  Eliminar Cliente")
            print("❎ Volver al Menú Principal")

            opcion_clientes = input("\nIngrese una opción: ")

            if opcion_clientes == "1":
                ver_clientes()
            elif opcion_clientes == "2":
                agregar_cliente()
            elif opcion_clientes == "3":
                modificar_cliente()
            elif opcion_clientes == "4":
                eliminar_cliente()
            elif opcion_clientes != "x":
                print("\n⚠️  Opción inválida. Intente nuevamente. \n")  

    # menu de gestión de destinos
    elif opcion_menu_principal == "2":
        opcion_destinos = ""
        while opcion_destinos != "x":
            print("\033[1;36m  🛫   Gestión Destinos  🛬\033[0m")
            print("═════════════════════════════")
            print("1️  Ver Destinos")
            print("2️  Agregar Destino")
            print("3️  Modificar Destino")
            print("4️  Eliminar Destino")
            print("❎ Volver al Menú Principal")

            opcion_destinos = input("\nIngrese una opción: ")

            if opcion_destinos == "1":
                ver_destinos()
            elif opcion_destinos == "2":
                agregar_destino()
            elif opcion_destinos == "3":
                modificar_destino()
            elif opcion_destinos == "4":
                eliminar_destino()
            elif opcion_destinos != "x":
                print("\n⚠️  Opción inválida. Intente nuevamente. \n")

    # menu de gestión de ventas
    elif opcion_menu_principal == "3":
        opcion_ventas = ""
        while opcion_ventas != "x":
            print("\033[1;36m  🛫   Gestión Ventas  🛬\033[0m")
            print("═════════════════════════════")
            print("1️  Ver Ventas")
            print("2️  Agregar Venta")
            print("❎ Volver al Menú Principal")

            opcion_ventas = input("\nIngrese una opción: ")

            if opcion_ventas == "1":
                ver_ventas()
            elif opcion_ventas == "2":
                agregar_venta()
            elif opcion_ventas != "x":
                print("\n⚠️  Opción inválida. Intente nuevamente. \n")  
                
    # menu de consultas de ventas
    elif opcion_menu_principal == "4":
        opcion_consultas = ""
        while opcion_consultas != "x":
            print("\033[1;36m  🛫   Gestión Consultas  🛬\033[0m")
            print("═════════════════════════════")
            print("1️  Consultar Ventas por Cliente")
            print("2️  Consultar Ventas por Destino")
            print("3️  Consultar Ventas Anuladas")
            print("❎ Volver al Menú Principal")

            opcion_consultas = input("\nIngrese una opción: ")

            if opcion_consultas == "1":
                consultar_ventas_por_cliente()
            elif opcion_consultas == "2":
                consultar_ventas_por_destino()
            elif opcion_consultas == "3":
                consultar_ventas_anuladas()
            elif opcion_consultas != "x":
                print("\n⚠️  Opción inválida. Intente nuevamente. \n")

    # menu de reporte general
    elif opcion_menu_principal == "5":
        opcion_reporte_general = ""
        while opcion_reporte_general != "x":
            print("\033[1;36m  🛫   Reporte General  🛬\033[0m")
            print("═════════════════════════════")
            print("1️  Ver Reporte de Ventas")
            print("❎ Volver al Menú Principal")

            opcion_reporte_general = input("\nIngrese una opción: ")

            if opcion_reporte_general == "1":
                reporte_general_ventas()
            elif opcion_reporte_general != "x":
                print("\n⚠️  Opción inválida. Intente nuevamente. \n")

    # menu de botón de arrepentimiento
    elif opcion_menu_principal == "b":
        opcion_arrepentimiento = ""
        while opcion_arrepentimiento != "x":
            print("\033[1;36m  🛫   Arrepentimiento  🛬\033[0m")
            print("═════════════════════════════")
            print("1️  Anular Venta")
            print("❎ Volver al Menú Principal")

            opcion_arrepentimiento = input("\nIngrese una opción: ")

            if opcion_arrepentimiento == "1":
                anular_venta()
            elif opcion_arrepentimiento != "x":
                print("\n⚠️  Opción inválida. Intente nuevamente. \n") 

    # menu de acerca del sistema
    elif opcion_menu_principal == "i":
        opcion_acerca = ""
        while opcion_acerca != "x":
            print("\033[1;36m🛫  Acerca de SkyRoute App  🛬\033[0m")
            print("═════════════════════════════")
            print("1️  Ver Información del Sistema")
            print("❎ Volver al Menú Principal")

            opcion_acerca = input("\nIngrese una opción: ")

            if opcion_acerca == "1":
                print("Opción seleccionada: Acerca del Sistema")
                print("\n📝 Información del Sistema")
                print("────────────────────────────────────────────────────────")
                print("🛩️  Nombre: SkyRoute - Sistema de Gestión de Pasajes Aéreos")
                print("🧩 Versión: 2.0.0")
                print("🛠️  Estado: Prototipo funcional con integración a base de datos MySQL")
                print("🗄️  Motor de Base de Datos: MySQL")
                print("🔗  Arquitectura: Modular, basada en funcionalidades")
                print("📦  Funcionalidades: Gestión de clientes, destinos y ventas, consultas y reportes")
                print("👨‍💻  Desarrolladores: Equipo de estudiantes de Módulo Programador")
                print("© 2025 SkyRoute S.R.L. Todos los derechos reservados.")
                print("────────────────────────────────────────────────────────\n")

            elif opcion_acerca != "x":
                print("\n⚠️  Opción inválida. Intente nuevamente. \n")  
                
    # menu de salida
    elif opcion_menu_principal == "x":
        print("\n👋 Gracias por usar SkyRoute App.")
    else:
        print("\n⚠️  Opción inválida. Intente nuevamente. \n")

print("Salió de la aplicación.")