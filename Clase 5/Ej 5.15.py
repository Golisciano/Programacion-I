import csv

def leer_arboles(nombre_archivo):
    lista_arboles = []
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            arbol = dict(zip(encabezados, fila)) 
            lista_arboles.append(arbol) 
    return lista_arboles

todos_los_arboles = leer_arboles("C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv")
print(len(todos_los_arboles))
print(todos_los_arboles[0])
