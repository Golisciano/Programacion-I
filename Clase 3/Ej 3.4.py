import csv

def leer_camion(nombre_archivo):

    camion = []
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            try:
                cajon = {
                    'nombre': row[0],
                    'cajones': int(row[1]),
                    'precio': float(row[2])
                }
                camion.append(cajon)
            except ValueError:
                print(f'Error en la línea {i+1}: datos incompletos {row}')
    return camion


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


def balance(camion, precios):

    costo = 0.0
    recaudacion = 0.0

    for item in camion:
        nombre = item['nombre']
        cajones = item['cajones']
        costo += cajones * item['precio']              
        if nombre in precios:
            recaudacion += cajones * precios[nombre]   

    diferencia = recaudacion - costo
    return costo, recaudacion, diferencia


camion = leer_camion('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv')
precios = leer_precios('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/precios.csv')
costo, recaudacion, diferencia = balance(camion, precios)

print('COSTO DEL CAMIÓN : $', round(costo, 2))
print('RECAUDACIÓN      : $', round(recaudacion, 2))
print('BALANCE          : $', round(diferencia, 2))

if diferencia > 0:
    print('Hubo ganancia')
elif diferencia < 0:
    print('Hubo perdida')

