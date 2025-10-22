import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        registros = []

        if has_headers:
            encabezados = next(filas)
            if select:
                indices = [encabezados.index(nombre_col) for nombre_col in select]
                encabezados = select
            else:
                indices = list(range(len(encabezados)))

            for fila in filas:
                if not fila:
                    continue
                fila = [fila[index] for index in indices]

                if types:
                    fila = [func(val) for func, val in zip(types, fila)]

                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            for fila in filas:
                if not fila:
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                registros.append(tuple(fila))
                
    return registros

camion = parse_csv(
    'C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv',
    select=['nombre', 'cajones', 'precio'],
    types=[str, int, float],
    has_headers=True
)
for r in camion:
    print(r)

precios = parse_csv(
    'C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/precios.csv',
    types=[str, float],
    has_headers=False
)
for p in precios:
    print(p)

