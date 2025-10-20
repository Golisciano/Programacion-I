import csv

def parse_csv(nombre_archivo, select=None, types=None):
    """
    Parsea un archivo CSV en una lista de diccionarios.
    
    Parámetros:
    - select: lista de nombres de columnas a incluir (opcional)
    - types: lista de funciones de conversión (opcional)
    """
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        if select:
            indices = [encabezados.index(nombre_col) for nombre_col in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:
                continue
            if select:
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila)]

            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

archivo = 'C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv'

registros = parse_csv(archivo)
for r in registros:
    print(r)

registros_tipeados = parse_csv(
    archivo,
    select=['nombre', 'cajones', 'precio'],
    types=[str, int, float]
)
for r in registros_tipeados:
    print(r)
