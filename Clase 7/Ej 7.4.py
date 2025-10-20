import csv

def parse_csv(nombre_archivo, select=None):
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

            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

archivo = 'C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv'

print("Todas las columnas")
registros_completos = parse_csv(archivo)
for r in registros_completos:
    print(r)

print("\nSolo columnas seleccionadas ")
registros_seleccionados = parse_csv(archivo, select=['nombre', 'cajones'])
for r in registros_seleccionados:
    print(r)