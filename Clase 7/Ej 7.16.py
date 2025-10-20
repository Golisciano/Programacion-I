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


def busqueda_binaria_comps(lista, x):
    izq = 0
    der = len(lista) - 1
    comps = 0

    while izq <= der:
        comps += 1
        medio = (izq + der) // 2

        if lista[medio] == x:
            return medio, comps
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1

    return -1, comps


archivo = 'C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv'

print("Todas las columnas")
registros_completos = parse_csv(archivo)
for r in registros_completos:
    print(r)

print("\nSolo columnas seleccionadas ")
registros_seleccionados = parse_csv(archivo, select=['nombre', 'cajones'])
for r in registros_seleccionados:
    print(r)

# --- Prueba de la búsqueda binaria ---
print("\nPrueba búsqueda binaria con comparaciones:")

lista = [1, 3, 5, 7, 9, 11, 13]

pos, comps = busqueda_binaria_comps(lista, 7)
print(f"Elemento encontrado en posición {pos} con {comps} comparaciones")

pos, comps = busqueda_binaria_comps(lista, 4)
print(f"Elemento no encontrado (pos={pos}) con {comps} comparaciones")
