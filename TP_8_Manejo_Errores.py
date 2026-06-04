#Ejercicio Nro 1

a = 10

b = input("Introduce un número: ")

result = a / b
# Error: TypeError.
# b es un string y no se puede dividir un entero por un string.

print(f"Resultado: {result}")

numbers = [1, 2, 3]

print(numbers[5])
# Error: IndexError.
# La posición 5 no existe dentro de la lista.

#Ejercicio Nro 2

a = 10

b = int(input("Introduce un número: "))

result = a / b

print(f"Resultado: {result}")

numbers = [1, 2, 3]

print(numbers[2])

#Ejercicio Nro 3

a = 10

b = input("Introduce un número: ")

try:

    result = a / b

    print(f"Resultado: {result}")

except:

    print("Ocurrió un error en la división")

numbers = [1, 2, 3]

try:

    print(numbers[5])

except:

    print("Ocurrió un error en la lista")

#Ejercicio Nro 4

a = 10

b = input("Introduce un número: ")

try:

    result = a / b

    print(f"Resultado: {result}")

except TypeError:

    print("Error de tipo")

except ZeroDivisionError:

    print("No se puede dividir por cero")

numbers = [1, 2, 3]

try:

    print(numbers[5])

except IndexError:

    print("Índice fuera de rango")

#Ejercicio Nro 5

a = 10

b = input("Introduce un número: ")

try:

    result = a / b

except TypeError:

    print("Error de tipo")

except ZeroDivisionError:

    print("No se puede dividir por cero")

else:

    print("Resultado:", result)

finally:

    print("Fin de la operación")

numbers = [1, 2, 3]

try:

    print(numbers[5])

except IndexError:

    print("Índice fuera de rango")

else:

    print("Acceso correcto")

finally:

    print("Fin de la consulta")

#Ejercicio Nro 6

try:

    numero = int(input("Ingrese un número: "))

    print("Número ingresado:", numero)

except ValueError:

    print("Debe ingresar un número válido")

except Exception as e:

    print("Se produjo un error inesperado")
    print(e)

#Ejercicio Nro 7

while True:

    try:

        numero = int(input("Ingrese un número: "))

        print("Número ingresado:", numero)

        break

    except ValueError:

        print("Debe ingresar un número válido")

    except Exception as e:

        print("Se produjo un error inesperado")
        print(e)
    
