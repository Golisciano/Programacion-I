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

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].upper() == especie.upper():
            try:
                altura = float(arbol['altura_tot'])
                alturas.append(altura)
            except ValueError:
                continue  
    return alturas

archivo = "C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv"
parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
especie = "Jacarandá"

for parque in parques:
    arboles = leer_parque(archivo, parque)
    alturas_jacaranda = obtener_alturas(arboles, especie)
    if alturas_jacaranda:  # si hay al menos un ejemplar
        altura_promedio = sum(alturas_jacaranda) / len(alturas_jacaranda)
        altura_maxima = max(alturas_jacaranda)
        print(f"\nParque: {parque}")
        print(f"Altura promedio de {especie}: {altura_promedio:.2f} m")
        print(f"Altura máxima de {especie}: {altura_maxima:.2f} m")
    else:
        print(f"\nParque: {parque}")
        print(f"No se encontraron ejemplares de {especie}.")
