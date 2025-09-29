import csv

def leer_camion(nombre_archivo):

    camion = []
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            try:
                nombre = row[0]
                cajones = int(row[1])
                precio = float(row[2])
                camion.append((nombre, cajones, precio))
            except ValueError:
                print(f'Error en la línea {i+1}: datos incompletos {row}')
    return camion


camion = leer_camion('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv')
for fruta in camion:
  print(fruta)
