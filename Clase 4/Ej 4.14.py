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


archivo = "C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv"
parque_elegido = "GENERAL PAZ"

arboles_general_paz = leer_parque(archivo, parque_elegido)
print(f"Cantidad de árboles en {parque_elegido}: {len(arboles_general_paz)}")

mis_especies = especies(arboles_general_paz)
print(f"Cantidad de especies distintas: {len(mis_especies)}")
print(mis_especies)
