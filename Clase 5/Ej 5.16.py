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

arboleda = leer_arboles("C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv")

H = [float(arbol['altura_tot']) for arbol in arboleda]

jacarandas = [float(arbol['altura_tot']) for arbol in arboleda
                if arbol['nombre_com'] == 'Jacarandá']

print("Cantidad de árboles en total:", len(arboleda))
print("Primeras 10 alturas generales:", H[:10])
print("Primeras 10 alturas de Jacarandás:", jacarandas[:10])
