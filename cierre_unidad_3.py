#EJERCICIO 1:

#Variables:
total_con_descuento = 0
total_sin_descuentos = 0
ahorro = 0
#Pedir nombre del cliente
nombre = input("Cliente: ")
while not nombre.isalpha() or nombre == "":
    print("Error: Utilice solo letras y no vacío")
    nombre = input("Cliente: ")

#Pedir cantidad de productos a comprar
cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <=0:
    print("Error: Ingrese un número mayor a 0")
    cantidad = input("Cantidad de productos: ")
cantidad = int(cantidad)

#Productos
for i in range(1,cantidad +1):
   precio = input(f"Producto: {i} Precio: ")
   while not precio.isdigit():
            print("Error: solo números")
            precio = input(f"Producto {i} - Precio: ")
    
   precio = int(precio)

#Descuento            
   descuento = input("Descuento (S/N): ")
   while descuento.lower() not in ["s","n"]:
       print("Error:Ingrese S o N")
       descuento = input("Descuento (S/N): ")

#Total sin descuento SIEMPRE suma el precio original
   total_sin_descuentos += precio

#Aplicar descuento si corresponde
   if descuento.lower() == "s":
       total_con_descuento += precio * 0.9
   else:
       total_con_descuento += precio
#Cálculos finales
ahorro = total_sin_descuentos - total_con_descuento
promedio = total_con_descuento / cantidad

#Salida EXACTA
print(f"\nTotal sin descuentos: {total_sin_descuentos:.2f}")
print(f"Total con descuentos: {total_con_descuento:.2f}")
print(f"Ahorro: {ahorro}")
print(f"Promedio por producto: {promedio:.2f}")

#EJERCICIO 2:

#Variables:
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
max_intentos = 3
acceso = False
#Login
while intentos < max_intentos:
    print(f"\nIntento {intentos+1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")        
        acceso = True
        break
    else:  
        print("Error: credenciales invalidas.")
        intentos += 1
if not acceso:
    print("Cuenta bloqueada")
#MENÚ                
while acceso:
     print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) SALIR")
     opcion = input("Opción: ")

    #Validación número
     if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue
       
     opcion = int(opcion)
    
     #Validación rango    
     if opcion < 1 or opcion > 4:
         print("Error: Opción fuera de rango.")
         continue
        
     if opcion == 1:
        print("Inscripto")
           
     elif opcion == 2:
        while True:
            nueva_clave = input("Nueva clave: ")

            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                continue
                
            confirmar = input("Confirmar clave: ")
                
            if nueva_clave != confirmar:
                print("Error: Las claves no coinciden.")
            else:
                clave_correcta = nueva_clave
                print("Clave actualizada correctamente.")
                break        

     elif opcion == 3:
        print("Tu eres perfecta xoxo.")

     elif opcion == 4:
        print("Saliendo del sistema...")
        break
     
# EJERCICIO 3

# Variables (NO listas)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# Nombre operador
operador = input("Nombre del operador: ")
while not operador.isalpha() or operador == "":
    print("Error: solo letras")
    operador = input("Nombre del operador: ")

while True:
    print("\n1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen")
    print("5. Salir")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: fuera de rango")
        continue

    # ---------------- RESERVAR ----------------
    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: 1 o 2")
            dia = input("Día (1=Lunes, 2=Martes): ")
        dia = int(dia)

        nombre = input("Nombre paciente: ")
        while not nombre.isalpha() or nombre == "":
            print("Error: solo letras")
            nombre = input("Nombre paciente: ")

        if dia == 1:
            if nombre in [lunes1, lunes2, lunes3, lunes4]:
                print("Error: ya existe")
            else:
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("No hay turnos disponibles")

        elif dia == 2:
            if nombre in [martes1, martes2, martes3]:
                print("Error: ya existe")
            else:
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("No hay turnos disponibles")

    # ---------------- CANCELAR ----------------
    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: 1 o 2")
            dia = input("Día (1=Lunes, 2=Martes): ")
        dia = int(dia)

        nombre = input("Nombre paciente: ")
        while not nombre.isalpha() or nombre == "":
            print("Error: solo letras")
            nombre = input("Nombre paciente: ")

        encontrado = False

        if dia == 1:
            if lunes1 == nombre:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre:
                lunes4 = ""
                encontrado = True

        elif dia == 2:
            if martes1 == nombre:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado")
        else:
            print("No se encontró el turno")

    # ---------------- VER AGENDA ----------------
    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: 1 o 2")
            dia = input("Día (1=Lunes, 2=Martes): ")
        dia = int(dia)

        if dia == 1:
            print("Lunes:")
            print(f"1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"4: {lunes4 if lunes4 != '' else '(libre)'}")

        elif dia == 2:
            print("Martes:")
            print(f"1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"3: {martes3 if martes3 != '' else '(libre)'}")

    # ---------------- RESUMEN ----------------
    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        for turno in [lunes1, lunes2, lunes3, lunes4]:
            if turno != "":
                ocupados_lunes += 1

        for turno in [martes1, martes2, martes3]:
            if turno != "":
                ocupados_martes += 1

        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} libres")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} libres")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")

    # ---------------- SALIR ----------------
    elif opcion == 5:
        print("Sistema cerrado")
        break