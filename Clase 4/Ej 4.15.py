import csv
from collections import Counter


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

def contar_ejemplares(lista_arboles):
    return Counter(arbol['nombre_com'] for arbol in lista_arboles if arbol['nombre_com'])


archivo = "C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv"
parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

for parque in parques:
    arboles = leer_parque(archivo, parque)
    contador = contar_ejemplares(arboles)
    print(f"\nParque: {parque}")
    print("5 especies más frecuentes:")
    for especie, cantidad in contador.most_common(5):
        print(f"{especie}: {cantidad}")
