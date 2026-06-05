# Ejercicio Nro 1 - Factorial recursivo
def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n - 1)


# Ejercicio Nro 2 - Serie de Fibonacci
def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Ejercicio Nro 3 - Potencia recursiva
def potencia(base, exp):
    # Caso base
    if exp == 0:
        return 1
    # Caso recursivo
    else:
        return base * potencia(base, exp - 1)


# Ejercicio Nro 4 - Decimal a binario
def decimal_a_binario(n):
    # Caso base implícito en 0
    if n == 0:
        return ""
    # Caso recursivo
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


#PROGRAMA PRINCIPAL
print("===== PRÁCTICO 11 - RECURSIVIDAD =====")

print("1 - Factorial")
print("2 - Fibonacci")
print("3 - Potencia")
print("4 - Decimal a binario")

opcion = int(input("Seleccione una opción: "))


#FACTORIAL
if opcion == 1:
    num = int(input("Ingrese un número: "))

    for i in range(1, num + 1):
        print(f"Factorial de {i} = {factorial(i)}")


#FIBONACCI
elif opcion == 2:
    num = int(input("Ingrese la posición: "))

    for i in range(num + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")


#POTENCIA
elif opcion == 3:
    base = int(input("Ingrese la base: "))
    exp = int(input("Ingrese el exponente: "))

    print("Resultado:", potencia(base, exp))


#BINARIO 
elif opcion == 4:
    num = int(input("Ingrese un número decimal: "))

    if num == 0:
        print("Resultado: 0")
    else:
        print("Resultado:", decimal_a_binario(num))


else:
    print("Opción inválida")