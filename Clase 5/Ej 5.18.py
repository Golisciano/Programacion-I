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

def medidas_de_especies(especies, arboleda):
    return {
        especie: [(float(arbol['altura_tot']), float(arbol['diametro']))
                  for arbol in arboleda if arbol['nombre_com'] == especie]
        for especie in especies
    }

arboleda = leer_arboles("C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv")

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

dicc_medidas = medidas_de_especies(especies, arboleda)

for especie, medidas in dicc_medidas.items():
    print(f"{especie}: {len(medidas)} árboles, primeras 5 medidas: {medidas[:5]}")
