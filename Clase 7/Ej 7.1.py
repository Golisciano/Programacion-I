import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            try:
                record = dict(zip(encabezados, fila))
                lote = {
                    'nombre': record['nombre'],
                    'cajones': int(record['cajones']),
                    'precio': float(record['precio'])
                }
                camion.append(lote)
            except ValueError:
                continue
    return camion


def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        filas = csv.reader(f)
        for fila in filas:
            try:
                precios[fila[0]] = float(fila[1])
            except (ValueError, IndexError):
                continue
    return precios


def hacer_informe(camion, precios):
    informe = []
    for lote in camion:
        nombre = lote['nombre']
        cajones = lote['cajones']
        precio_compra = lote['precio']
        precio_venta = precios.get(nombre, 0)
        cambio = precio_venta - precio_compra
        informe.append((nombre, cajones, precio_compra, cambio))
    return informe


def imprimir_informe(informe):
    print(f'{"Nombre":>10s} {"Cajones":>10s} {"Precio":>10s} {"Cambio":>10s}')
    print('-'*10, '-'*10, '-'*10, '-'*10)
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} ${precio:<9.2f} {cambio:>10.2f}')


def main():
    camion = leer_camion('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv')
    precios = leer_precios('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/precios.csv')
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


if __name__ == '__main__':
    main()
