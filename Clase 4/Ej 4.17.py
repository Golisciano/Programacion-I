import csv

def obtener_inclinaciones_csv(nombre_archivo, especie):
    inclinaciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            arbol = dict(zip(encabezados, fila))
            if arbol['nombre_com'].upper() == especie.upper():
                try:
                    inclinacion = float(arbol['inclinacio'])
                    inclinaciones.append(inclinacion)
                except ValueError:
                    continue 
    return inclinaciones

archivo = "C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv"
especie = "Jacarandá"

inclinaciones_jacaranda = obtener_inclinaciones_csv(archivo, especie)
print(f"Cantidad de Jacarandá: {len(inclinaciones_jacaranda)}")
print(f"Primeras inclinaciones: {inclinaciones_jacaranda[:10]}...")
