import csv

def costo_camion(nombre_archivo):
    total = 0.0
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        next(filas)
        for fila in filas:
            try:
                cajones = int(fila[1])
                precio = float(fila[2])
                total += cajones * precio
            except:
                continue
    return total

costo = costo_camion('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv')
print('Costo total es de:', costo)
