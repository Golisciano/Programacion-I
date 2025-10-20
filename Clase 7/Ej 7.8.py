import fileparse

def leer_camion(nombre_archivo):
    """Lee un archivo de lotes de un camión y devuelve una lista de diccionarios"""
    camion = fileparse.parse_csv(
        nombre_archivo,
        select=['nombre', 'cajones', 'precio'],
        types=[str, int, float],
        has_headers=True
    )
    return camion


def leer_precios(nombre_archivo):
    """Lee un archivo de precios y devuelve un diccionario"""
    precios_lista = fileparse.parse_csv(
        nombre_archivo,
        types=[str, float],
        has_headers=False
    )
    precios = dict(precios_lista)
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


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


informe_camion(
    'C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv',
    'C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/precios.csv'
)
