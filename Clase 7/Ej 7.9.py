import fileparse  # Importamos el módulo fileparse

def leer_camion(nombre_archivo):
    """Lee un archivo de lotes de un camión y devuelve una lista de diccionarios"""
    camion = fileparse.parse_csv(
        nombre_archivo,
        select=['nombre', 'cajones', 'precio'],
        types=[str, int, float],
        has_headers=True
    )
    return camion


def costo_camion(nombre_archivo):
    """Calcula el costo total de los lotes del camión usando leer_camion()"""
    camion = leer_camion(nombre_archivo)
    total = 0.0
    for lote in camion:
        total += lote['cajones'] * lote['precio']
    return total


# --- Ejecución ---
archivo = 'C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/fecha_camion.csv'
costo = costo_camion(archivo)
print('Costo total es de:', costo)
