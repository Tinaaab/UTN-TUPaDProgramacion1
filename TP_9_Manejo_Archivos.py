#Ejercicio Nro 1
try:

    with open("productos.txt", "x") as archivo:

        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,850,15\n")
        archivo.write("Goma,75,40\n")

    print("Archivo creado correctamente.")

except FileExistsError:

    print("El archivo ya existe.")

#Ejercicio Nro 2
try:

    with open("productos.txt", "r") as archivo:

        for linea in archivo:

            datos = linea.strip().split(",")

            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]

            print(
                f"Producto: {nombre} | "
                f"Precio: ${precio} | "
                f"Cantidad: {cantidad}"
            )

except FileNotFoundError:

    print("Error: el archivo no existe.")

#Ejercicio Nro 3
try:

    with open("productos.txt", "r") as archivo:

        for linea in archivo:

            datos = linea.strip().split(",")

            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]

            print(
                f"Producto: {nombre} | "
                f"Precio: ${precio} | "
                f"Cantidad: {cantidad}"
            )

except FileNotFoundError:

    print("Error: el archivo no existe.")

#Ejercicio Nro 3
try:

    with open("productos.txt", "r") as archivo:

        for linea in archivo:

            datos = linea.strip().split(",")

            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]

            print(
                f"Producto: {nombre} | "
                f"Precio: ${precio} | "
                f"Cantidad: {cantidad}"
            )

    nombre = input("\nIngrese nombre: ").strip()

    precio = float(
        input("Ingrese precio: ")
    )

    cantidad = int(
        input("Ingrese cantidad: ")
    )

    with open("productos.txt", "a") as archivo:

        archivo.write(
            f"{nombre},{precio},{cantidad}\n"
        )

    print("Producto agregado correctamente.")

except FileNotFoundError:

    print("Error: el archivo no existe.")

except ValueError:

    print("Error: precio o cantidad inválidos.")

#Ejercicio Nro 4
productos = []

try:

    with open("productos.txt", "r") as archivo:

        for linea in archivo:

            datos = linea.strip().split(",")

            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }

            productos.append(producto)

    print("\nLista de productos cargados:")

    for producto in productos:

        print(producto)

except FileNotFoundError:

    print("Error: el archivo no existe.")

#Ejercicio Nro 5
productos = []

try:

    with open("productos.txt", "r") as archivo:

        for linea in archivo:

            datos = linea.strip().split(",")

            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }

            productos.append(producto)

    nombre_buscado = input(
        "\nIngrese el producto a buscar: "
    )

    encontrado = False

    for producto in productos:

        if producto["nombre"].lower() == nombre_buscado.lower():

            print("\nProducto encontrado")

            print(
                f"Nombre: {producto['nombre']}"
            )

            print(
                f"Precio: ${producto['precio']}"
            )

            print(
                f"Cantidad: {producto['cantidad']}"
            )

            encontrado = True

            break

    if not encontrado:

        print("Producto no encontrado.")

except FileNotFoundError:

    print("Error: el archivo no existe.")

#Ejercicio Nro 6
productos = []

try:

    with open("productos.txt", "r") as archivo:

        for linea in archivo:

            datos = linea.strip().split(",")

            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }

            productos.append(producto)

    print("\nProductos actuales:")

    for producto in productos:

        print(
            f"Producto: {producto['nombre']} | "
            f"Precio: ${producto['precio']} | "
            f"Cantidad: {producto['cantidad']}"
        )

    nombre = input("\nIngrese nombre: ").strip()

    precio = float(
        input("Ingrese precio: ")
    )

    cantidad = int(
        input("Ingrese cantidad: ")
    )

    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(nuevo_producto)

    nombre_buscado = input(
        "\nIngrese el producto a buscar: "
    )

    encontrado = False

    for producto in productos:

        if producto["nombre"].lower() == nombre_buscado.lower():

            print("\nProducto encontrado")

            print(
                f"Nombre: {producto['nombre']}"
            )

            print(
                f"Precio: ${producto['precio']}"
            )

            print(
                f"Cantidad: {producto['cantidad']}"
            )

            encontrado = True

            break

    if not encontrado:

        print("Producto no encontrado.")

    with open("productos.txt", "w") as archivo:

        for producto in productos:

            archivo.write(
                f"{producto['nombre']},"
                f"{producto['precio']},"
                f"{producto['cantidad']}\n"
            )

    print(
        "\nProductos guardados correctamente."
    )

except FileNotFoundError:

    print("Error: el archivo no existe.")

except ValueError:

    print("Error: precio o cantidad inválidos.")