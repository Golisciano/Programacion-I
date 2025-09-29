import csv

def costo_camion(nombre_archivo):
    total = 0.0
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        next(filas)
        for n_fila, fila in enumerate(filas, start = 2):
            try:
                cajones = int(fila[1])
                precio = float(fila[2])
                total += cajones * precio
            except ValueError:
                print(f'Fila {n_fila} : No se puede interpretar : {fila} ')               
    return total

costo = costo_camion('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/missing.csv')
print('Costo total es de:', costo)
