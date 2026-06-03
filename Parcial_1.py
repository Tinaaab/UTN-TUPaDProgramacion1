# sistema_inventario.py

# Listas principales:
# herramientas → guarda los nombres de los productos
# existencias → guarda el stock correspondiente a cada producto
herramientas = []
existencias = []

# Bucle principal del sistema (menú infinito hasta elegir salir)
while True:
    print("\n--- Sistema de Control de Inventario ---")
    print("1) Carga Inicial de Herramientas")
    print("2) Carga de Existencias")
    print("3) Visualización de Inventario")
    print("4) Consulta de Stock")
    print("5) Reporte de Agotados")
    print("6) Alta de Nuevo Producto")
    print("7) Actualización de Stock (Venta/Ingreso)")
    print("8) Salir")

    # Validación de opción (solo números del 1 al 8)
    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= 8):
        print("Error, Ingresa un numero del 1 al 8 ")
        opcion = input("Seleccion de opciones: ")
        continue
    opcion = int(opcion)

    # ---------------------------------------------------
    # 1) CARGA INICIAL DE HERRAMIENTAS
    # ---------------------------------------------------
    if opcion == 1:
        # Reinicia las listas (borra datos anteriores)
        herramientas = []
        existencias = []

        # Solicita cantidad de herramientas
        cantidad_str = input("Cantidad de herramientas: ").strip()
        while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
            print("Error: número inválido.")
            cantidad_str = input("Cantidad de herramientas: ").strip()

        cantidad = int(cantidad_str)
        i = 0

        # Carga de nombres
        while i < cantidad:
            nombre = input(f"Nombre herramienta {i+1}: ").strip()

            # Validación: nombre no vacío
            if nombre == "":
                print("Error: nombre vacío.")
                continue

            # Validación: evitar duplicados
            duplicado = False
            j = 0
            while j < len(herramientas):
                if herramientas[j].lower() == nombre.lower():
                    duplicado = True
                    break
                j += 1

            if duplicado:
                print("Error: nombre duplicado.")
                continue

            herramientas.append(nombre)
            i += 1

    # ---------------------------------------------------
    # 2) CARGA DE EXISTENCIAS
    # ---------------------------------------------------
    elif opcion == 2:
        # No se puede cargar stock si no hay productos
        if len(herramientas) == 0:
            print("Error: primero cargue herramientas.")
        else:
            existencias = []
            i = 0

            # Se pide el stock para cada herramienta
            while i < len(herramientas):
                print(f"Herramienta: {herramientas[i]}")
                cantidad_str = input("Cantidad: ")

                # Validación: número positivo
                while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
                    print("Error: número inválido.")
                    cantidad_str = input("Cantidad: ")

                existencias.append(int(cantidad_str))
                i += 1

            print("Existencias cargadas correctamente.")

    # ---------------------------------------------------
    # 3) VISUALIZACIÓN DEL INVENTARIO
    # ---------------------------------------------------
    elif opcion == 3:
        if len(herramientas) == 0:
            print("Catálogo vacío.")
        else:
            print("\nInventario:")
            i = 0

            # Muestra cada herramienta con su stock
            while i < len(herramientas):
                if i < len(existencias):
                    print(f"{herramientas[i]} - {existencias[i]}")
                else:
                    # Caso donde aún no se cargó stock
                    print(f"{herramientas[i]} - sin stock cargado")
                i += 1

    # ---------------------------------------------------
    # 4) CONSULTA DE STOCK
    # ---------------------------------------------------
    elif opcion == 4:
        if len(herramientas) == 0:
            print("Catálogo vacío.")
        else:
            nombre = input("Ingrese herramienta: ").strip()

            if nombre == "":
                print("Error: nombre vacío.")
            else:
                encontrado = False
                i = 0

                # Busca la herramienta
                while i < len(herramientas):
                    if herramientas[i].lower() == nombre.lower():
                        if i < len(existencias):
                            print(f"Stock: {existencias[i]}")
                        else:
                            print("Stock no cargado.")
                        encontrado = True
                        break
                    i += 1

                if not encontrado:
                    print("Error: herramienta no encontrada.")

    # ---------------------------------------------------
    # 5) REPORTE DE PRODUCTOS AGOTADOS
    # ---------------------------------------------------
    elif opcion == 5:
        if len(herramientas) == 0:
            print("Catálogo vacío.")
        elif len(existencias) == 0:
            print("No hay existencias cargadas.")
        else:
            print("\nProductos agotados:")
            hay = False
            i = 0

            # Recorre ambas listas
            while i < len(herramientas) and i < len(existencias):
                if existencias[i] == 0:
                    print(herramientas[i])
                    hay = True
                i += 1

            if not hay:
                print("No hay productos agotados.")

    # ---------------------------------------------------
    # 6) ALTA DE NUEVO PRODUCTO
    # ---------------------------------------------------
    elif opcion == 6:
        # Requiere inventario completo cargado
        if len(herramientas) == 0 or len(existencias) != len(herramientas):
            print("Error: primero cargue herramientas y existencias.")
        else:
            nombre = input("Nombre del producto: ").strip()

            if nombre == "":
                print("Error: nombre vacío.")
            else:
                duplicado = False
                i = 0

                # Verifica duplicados
                while i < len(herramientas):
                    if herramientas[i].lower() == nombre.lower():
                        duplicado = True
                        break
                    i += 1

                if duplicado:
                    print("Error: nombre duplicado.")
                else:
                    cantidad_str = input("Stock inicial: ")

                    # Validación del stock
                    while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
                        print("Error: ingresa un número mayor a cero.")
                        cantidad_str = input("Stock inicial: ")
                  
                    herramientas.append(nombre)
                    existencias.append(int(cantidad_str))
                    print("Producto agregado.")

    # ---------------------------------------------------
    # 7) ACTUALIZACIÓN DE STOCK
    # ---------------------------------------------------
    elif opcion == 7:
        if len(herramientas) == 0 or len(existencias) != len(herramientas):
            print("Error: cargue el inventario completo.")
        else:
            nombre = input("Herramienta: ").strip()

            if nombre == "":
                print("Error: nombre vacío.")
            else:
                encontrado = False
                i = 0

                # Buscar producto
                while i < len(herramientas):
                    if herramientas[i].lower() == nombre.lower():
                        encontrado = True
                        break
                    i += 1

                if not encontrado:
                    print("Error: herramienta no encontrada.")
                else:
                    print("1) Venta")
                    print("2) Ingreso")
                    op = input("Seleccione: ").strip()

                    if op != "1" and op != "2":
                        print("Error: opción inválida.")
                    else:
                        cantidad_str = input("Cantidad: ").strip()

                        # Validación de cantidad
                        while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
                            print("Error: ingresa un número.")
                            cantidad_str = input("Cantidad: ").strip()

                        cantidad = int(cantidad_str)

                        # Venta → resta stock
                        if op == "1":
                            if cantidad > existencias[i]:
                                print("Error: stock insuficiente.")
                            else:
                                existencias[i] -= cantidad
                                print("Venta realizada.")

                        # Ingreso → suma stock
                        if op == "2":
                            existencias[i] += cantidad
                            print("Ingreso realizado.")

    # ---------------------------------------------------
    # 8) SALIR DEL SISTEMA
    # ---------------------------------------------------
    elif opcion == 8:
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
