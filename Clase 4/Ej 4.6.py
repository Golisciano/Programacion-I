import csv
from collections import Counter

def costo_camion(nombre_archivo):
    total = 0.0
    contador = Counter()
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        next(filas)
        for fila in filas:
            try:
                nombre = fila[0]
                cajones = int(fila[1])
                precio = float(fila[2])
                total += cajones * precio
                contador[nombre] += cajones 
            except:
                continue
    return total, contador

costo, cajones_por_fruta = costo_camion('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv')

print('Costo total es de:', costo)
print('Cajones por fruta:', dict(cajones_por_fruta))
