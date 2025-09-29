import csv

def leer_precios(nombre_archivo):

    precios = {}
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows, start=1):
            try:
                nombre = row[0]
                precio = float(row[1])
                precios[nombre] = precio
            except IndexError:

                continue
            except ValueError:
                print(f'Error en la línea {i}: no pude interpretar {row}')
    return precios


precios = leer_precios('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/precios.csv')
for fruta, precio in precios.items():
    print(fruta,',',precio)
