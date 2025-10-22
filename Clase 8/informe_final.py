import sys
import fileparse

# ---------------------------------------------------------
# FUNCIONES DE LECTURA
# ---------------------------------------------------------

def leer_camion(nombre_archivo):
    """Lee el archivo del camión y devuelve una lista de diccionarios"""
    camion = fileparse.parse_csv(
        nombre_archivo,
        select=['nombre', 'cajones', 'precio'],
        types=[str, int, float],
        has_headers=True
    )
    return camion


def leer_precios(nombre_archivo):
    """Lee la lista de precios de venta y devuelve un diccionario"""
    precios = dict(fileparse.parse_csv(
        nombre_archivo,
        types=[str, float],
        has_headers=False
    ))
    return precios


# ---------------------------------------------------------
# FUNCIONES DE INFORME
# ---------------------------------------------------------

def hacer_informe(camion, precios):
    """Genera los datos del informe como una lista de tuplas"""
    informe = []
    for lote in camion:
        nombre = lote['nombre']
        cajones = lote['cajones']
        precio = lote['precio']
        cambio = precios[nombre] - precio
        informe.append((nombre, cajones, precio, cambio))
    return informe


def imprimir_informe(informe):
    """Imprime el informe con formato"""
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * 4)
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')


# ---------------------------------------------------------
# FUNCIÓN PRINCIPAL DE INFORME_FINAL
# ---------------------------------------------------------

def f_principal(args):
    """Función principal, recibe lista de argumentos como sys.argv"""
    if len(args) != 3:
        print('Uso: informe_final.py archivo_camion archivo_precios')
        return
    archivo_camion = args[1]
    archivo_precios = args[2]

    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


# ---------------------------------------------------------
# BLOQUE PRINCIPAL
# ---------------------------------------------------------

if __name__ == '__main__':
    f_principal(sys.argv)



# =========================================================
# AHORA EL SEGUNDO PROGRAMA: costo_camion.py
# =========================================================

# costo_camion.py
# Este módulo usa informe_final para leer los datos del camión

def costo_camion(nombre_archivo):
    """Calcula el costo total de un camión de frutas"""
    camion = leer_camion(nombre_archivo)
    total = 0.0
    for lote in camion:
        total += lote['cajones'] * lote['precio']
    return total


def f_principal_costo(args):
    """Función principal para ejecución directa o desde import"""
    if len(args) != 2:
        print('Uso: costo_camion.py archivo_camion')
        return
    archivo = args[1]
    costo = costo_camion(archivo)
    print(f'Costo total: {costo:.2f}')


# ---------------------------------------------------------
# BLOQUE PRINCIPAL DE COSTO_CAMION
# ---------------------------------------------------------

if __name__ == '__main__' and sys.argv[0].endswith('costo_camion.py'):
    f_principal_costo(sys.argv)
