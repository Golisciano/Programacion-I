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

arboles_general_paz = leer_parque("C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv", "GENERAL PAZ")
print(len(arboles_general_paz))
print(arboles_general_paz[0])
    