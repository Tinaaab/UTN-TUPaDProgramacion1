#Punto 1
notas_estudiantes = [9,1,6,3,10,5,9,7,8,2]

nota_maxima = max(notas_estudiantes)
suma_notas = sum(notas_estudiantes)
print("La suma de notas es: ",suma_notas)
print("La nota mas alta es: ",nota_maxima)

#Punto 2
productos = []
for i in range (5):
    producto = input(f"Ingrese el producto: {i+1}:")
    productos.append(producto)
print("Lista de productos: ",productos)
productos.sort()
print("La lista de productos ordenada: ",productos)

eliminar = input("Que productos desea eliminar?: ")

if eliminar in productos:
    productos.remove(eliminar) 
    print("Producto eliminado exitosamente")
else:
    print("El producto no se encuentra en la lista")

print("Lista actualizada: ",productos)

#Punto 3
import random
lista = [random.randint(1, 100) for _ in range(15)]

pares = [num for num in lista if num % 2 == 0]
impares = [num for num in lista if num % 2 != 0]

print("Lista original:", lista)
print("Lista de numeros pares:", pares)
print("Lista de numeros impares:", impares)

print("Cantidad de numeros pares:", len(pares))
print("Cantidad de numeros impares:", len(impares))

#Punto 4
datos = [1,3,5,3,7,1,9,5,3]
sin_repetidos = []
print("Lista de datos: ",datos)

for num in datos:
    if num not in sin_repetidos:
        sin_repetidos.append(num)
print("Lista sin repetidos:",sin_repetidos)

#Punto 5
estudiantes = ["ana","pao","luz","manu","tomas","matias","sofia","luis"]

print("Estudiantes presentes:", estudiantes)
desicion = input("¿Deseas agregar o eliminar un estudiante? (agregar/eliminar): ")

if desicion == "agregar":
    nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print("Estudiante agregado exitosamente Colombiano El Mejor.")
elif desicion == "eliminar":
    eliminar = input("Ingresa el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print("Estudiante eliminado exitosamente.")
    else:
        print("El estudiante no esta en la lista.")
else:
    print("Opcion no valida.")

print("La lista de estudiantes actualizada es:",estudiantes)           

#Punto 6
lista = [1, 2, 3, 4, 5, 6, 7]

ultimo = lista[-1]

for i in range(len(lista)-1, 0, -1):
    lista[i] = lista[i-1]

lista[0] = ultimo

print(lista)

#Punto 7
# Matriz 7x2 (7 días, mínima y máxima)
temperaturas = [
    [12, 20],  # Día 1
    [10, 18],  # Día 2
    [11, 22],  # Día 3
    [9, 17],   # Día 4
    [13, 25],  # Día 5
    [14, 24],  # Día 6
    [8, 19]    # Día 7
]

# Calcular promedios
suma_min = 0
suma_max = 0

for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]

prom_min = suma_min / 7
prom_max = suma_max / 7

# Buscar mayor amplitud térmica
mayor_amplitud = 0
dia_mayor = 0

for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i + 1  # +1 porque los días empiezan en 1

# Mostrar resultados
print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)
print("Mayor amplitud térmica en el día:", dia_mayor)

#Punto 8
# Matriz: 5 estudiantes x 3 materias
notas = [
    [7, 8, 6],  # Estudiante 1
    [5, 9, 7],  # Estudiante 2
    [8, 6, 9],  # Estudiante 3
    [4, 7, 5],  # Estudiante 4
    [9, 8, 10]  # Estudiante 5
]

# Promedio de cada estudiante
print("Promedio por estudiante:")
for i in range(len(notas)):
    promedio = sum(notas[i]) / 3
    print(f"Estudiante {i+1}: {promedio}")

# Promedio de cada materia
print("\nPromedio por materia:")
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    promedio = suma / 5
    print(f"Materia {j+1}: {promedio}")

#Punto 9
# Crear tablero 3x3 inicializado con "-"
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Función para mostrar el tablero
def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

# Turnos de jugadores
jugador = "X"

for turno in range(9):  # máximo 9 jugadas
    print(f"Turno del jugador {jugador}")
    mostrar_tablero()
    
    # Pedir fila y columna
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))
    
    # Validar que la casilla esté vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        
        # Cambiar de jugador
        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"
    else:
        print("Casilla ocupada, intente de nuevo.")
        continue

# Mostrar tablero final
print("Tablero final:")
mostrar_tablero()


#Punto 10
# Crear la matriz (4 productos x 7 días)
ventas = [
    [10, 12, 9, 14, 11, 13, 15],   # Producto 1
    [8, 7, 10, 9, 6, 11, 12],      # Producto 2
    [15, 14, 13, 16, 12, 11, 10],  # Producto 3
    [5, 6, 7, 8, 9, 10, 11]        # Producto 4
]

# 1. Total vendido por cada producto
print("Total vendido por cada producto:")
totales_productos = []

for i in range(4):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")

# 2. Día con mayores ventas totales
totales_dias = []

for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    totales_dias.append(total_dia)

dia_mayor = totales_dias.index(max(totales_dias))
print(f"\nDía con mayores ventas: Día {dia_mayor + 1}")

# 3. Producto más vendido en la semana
producto_mas_vendido = totales_productos.index(max(totales_productos))
print(f"Producto más vendido: Producto {producto_mas_vendido + 1}")

#Punto 11
# Lista de 10 estudiantes
estudiantes = [
    "Ana", "Luis", "Carlos", "María", "Sofía",
    "Julián", "Lucía", "Pedro", "Valentina", "Diego"
]

# Solicitar nombre a buscar
nombre = input("Ingresá el nombre a buscar: ")

# Buscar en la lista
if nombre in estudiantes:
    posicion = estudiantes.index(nombre)
    print(f"El nombre {nombre} se encuentra en la lista.")
    print(f"Posición: {posicion}")
else:
    print(f"El nombre {nombre} no está en la lista.")
    
#Punto 12
# Pedir 8 números al usuario
numeros = []

for i in range(8):
    num = int(input(f"Ingresá el número {i+1}: "))
    numeros.append(num)

# Mostrar lista original
print("\nLista original:")
print(numeros)

# Ordenar de menor a mayor
orden_asc = sorted(numeros)
print("\nLista ordenada de menor a mayor:")
print(orden_asc)

# Ordenar de mayor a menor
orden_desc = sorted(numeros, reverse=True)
print("\nLista ordenada de mayor a menor:")
print(orden_desc)

#Punto 13
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# 1. Puntaje más alto y más bajo
maximo = max(puntajes)
minimo = min(puntajes)

print(f"Puntaje más alto: {maximo}")
print(f"Puntaje más bajo: {minimo}")

# 2. Lista ordenada de mayor a menor (ranking)
ranking = sorted(puntajes, reverse=True)
print("\nRanking (de mayor a menor):")
print(ranking)

# 3. Posición del puntaje 990 en el ranking
posicion = ranking.index(990)
print(f"\nEl puntaje 990 está en la posición: {posicion}")