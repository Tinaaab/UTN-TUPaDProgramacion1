import csv
import os

ruta_csv = os.path.join(
    os.path.dirname(__file__),
    "paises.csv"
)

print("Ruta encontrada:")
print(ruta_csv)

with open(ruta_csv, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("\nContenido del archivo:")
print(contenido)
