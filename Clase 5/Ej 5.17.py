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

A_D_jacarandas = [(float(arbol['altura_tot']), float(arbol['diametro'])) 
                  for arbol in arboleda 
                  if arbol['nombre_com'] == 'Jacarandá']

# Ejemplo de impresión
print("Primeras 10 tuplas (altura, diámetro) de Jacarandás:")
print(A_D_jacarandas[:10])
