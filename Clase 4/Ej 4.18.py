import csv

def leer_parque(nombre_archivo, parque):
    arboles_parque = []
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            arbol = dict(zip(encabezados, fila))
            if arbol["espacio_ve"].upper() == parque.upper():
                arboles_parque.append(arbol)
    return arboles_parque

def especies(lista_arboles):
    return {arbol['nombre_com'] for arbol in lista_arboles if arbol['nombre_com']}

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].upper() == especie.upper():
            try:
                inclinacion = float(arbol['inclinacio'])
                inclinaciones.append(inclinacion)
            except ValueError:
                continue
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    max_inclinacion = -1
    especie_max = None
    for especie in especies(lista_arboles):
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        if inclinaciones:
            inclinacion_mayor = max(inclinaciones)
            if inclinacion_mayor > max_inclinacion:
                max_inclinacion = inclinacion_mayor
                especie_max = especie
    return especie_max, max_inclinacion

archivo = "C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv"
parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

for parque in parques:
    arboles = leer_parque(archivo, parque)
    especie, inclinacion = especimen_mas_inclinado(arboles)
    print(f"\nParque: {parque}")
    print(f"Especie con ejemplar más inclinado: {especie}")
    print(f"Inclinación máxima: {int(round(inclinacion))}°")