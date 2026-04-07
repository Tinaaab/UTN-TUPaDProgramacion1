#EJERCICIO 1:
#Variables:
total = 0
precio_total = 0
precio_sin_descuento = 0
precio_con_descuento = 0
precio_total_con_descuento = 0
ahorro_total = 0
promedio_por_producto = 0
#Pedir nombre del cliente
nombre = input("Por favor complete con su nombre: ")
while not nombre.isalpha():
    print("Utilice solo letras")
    nombre = input("Por favor complete con su nombre: ")
#Pedir cantidad de productos a comprar
cantidad = input("Por favor indique la cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <=0:
    print("Utilice solo números enteros mayores a 0")
    cantidad = input("Por favor indique la cantidad de productos: ")
cantidad = int(cantidad)
#
for i in range(1,cantidad +1):
   precio = input(f"Producto: {i} Precio: ")
   while not precio.isdigit():
        print("Utilice solo números enteros mayores a 0")
        precio = input(f"Producto: {i} Precio: ")
   precio = int(precio)
   descuento = input("El producto tiene descuento?: ")
   while descuento.lower() not in ["s","n"]:
       print("Ingrese s/n")
       descuento = input("El producto tiene descuento?: ")
   if descuento.lower() == "s":
       precio_con_descuento = precio_con_descuento + (precio * 0.9)
   else:
       precio_sin_descuento = precio_sin_descuento + precio
   total = total + precio    
precio_total = precio_total + precio
precio_total_con_descuento = precio_sin_descuento + precio_con_descuento
promedio_por_producto = precio_total_con_descuento / cantidad 
ahorro_total = total - precio_total_con_descuento
print(f"Precio total: {precio_total}")          
print(f"Precio total con descuento: {precio_total_con_descuento}")
print(f"Promedio por producto: {promedio_por_producto:.2f}")
print(f"Ahorro total: {ahorro_total}")

#EJERCICIO 2:
#Variables: