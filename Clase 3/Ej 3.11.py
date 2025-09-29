# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    total = 0.0
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        filas = csv.reader(f)
        next(filas)  # salteo encabezado
        for fila in filas:
            try:
                cajones = int(fila[1])
                precio = float(fila[2])
                total += cajones * precio
            except ValueError:
                # Si falta algún dato, lo ignoro
                continue
    return total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)


