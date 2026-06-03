#Ejercicio Nro 1

def imprimir_hola_mundo():
    print("¡Hola Mundo!")

imprimir_hola_mundo()

#Ejercicio Nro 2

def saludar_usuario(nombre):
    return f"¡Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

#Ejercicio Nro 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio Nro 4

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio: "))

print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))

#Ejercicio Nro 5

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese los segundos: "))

print("Horas:", segundos_a_horas(segundos))

#Ejercicio Nro 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))

tabla_multiplicar(numero)

#Ejercicio Nro 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a- b
    multiplicacion = a * b
    division = a / b

    return suma, resta, multiplicacion, division

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)

#Ejercicio Nro 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"IMC: {imc:.2f}")

#Ejercicio Nro 9

def celsius_a_farenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))

print("Farenheit: ", celsius_a_farenheit(celsius))

#Ejercicio Nro 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

print("Promedio:", calcular_promedio(a, b, c))




