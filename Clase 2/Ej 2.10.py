import csv

def costo_camion(nombre_archivo):
    total = 0.0
    tuplas = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        next(filas)  # salteo cabecera
        for fila in filas:
            try:
                t = (fila[0], int(fila[1]), float(fila[2]))  # nombre, cajones, precio
                tuplas.append(t)
                total += t[1] * t[2]
            except ValueError:
                # si alguna fila está mal (ej. vacía) la ignoro
                continue
    return total, tuplas



costo, datos = costo_camion('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv')
print('Costo total es de:', costo)
print('Primeras tuplas:', datos[:3])
