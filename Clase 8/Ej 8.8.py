import sys
import fileparse

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        camion = fileparse.parse_csv(
            f,
            select=['nombre', 'cajones', 'precio'],
            types=[str, int, float],
            has_headers=True
        )
    return camion


def leer_precios(nombre_archivo):
    """Lee la lista de precios de venta y devuelve un diccionario"""
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        precios = dict(fileparse.parse_csv(
            f,
            types=[str, float],
            has_headers=False
        ))
    return precios



def hacer_informe(camion, precios):
    informe = []
    for lote in camion:
        nombre = lote['nombre']
        cajones = lote['cajones']
        precio = lote['precio']
        cambio = precios[nombre] - precio
        informe.append((nombre, cajones, precio, cambio))
    return informe


def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * 4)
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')



def f_principal(args):
    if len(args) != 3:
        print('Uso: informe_final.py archivo_camion archivo_precios')
        return
    archivo_camion = args[1]
    archivo_precios = args[2]

    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


if __name__ == '__main__':
    f_principal(sys.argv)
