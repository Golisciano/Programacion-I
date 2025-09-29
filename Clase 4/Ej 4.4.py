import csv

def costo_camion(nombre_archivo):
    total = 0.0
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)   

        for fila in filas:
            try:
                # Unimos encabezados con valores usando zip
                record = dict(zip(encabezados, fila))
                cajones = int(record['cajones'])
                precio = float(record['precio'])
                total += cajones * precio
            except ValueError:
                continue
    return total


costo = costo_camion('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/fecha_camion.csv')
print('Costo total es de:', costo)
