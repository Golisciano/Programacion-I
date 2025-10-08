import csv
import matplotlib.pyplot as plt

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

def scatter_hd(lista_de_pares, especie, color):
    alturas = [par[0] for par in lista_de_pares]
    diametros = [par[1] for par in lista_de_pares]

    plt.scatter(diametros, alturas, alpha=0.5, color=color, edgecolor='black')
    plt.title(f'Relación altura-diámetro de {especie}')
    plt.xlabel('Diámetro (cm)')
    plt.ylabel('Altura (m)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

arboleda = leer_arboles("C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv")

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

dicc_medidas = medidas_de_especies(especies, arboleda)

for especie, medidas in dicc_medidas.items():
    print(f"{especie}: {len(medidas)} árboles, primeras 5 medidas: {medidas[:5]}")

colores = {
    'Eucalipto': 'seagreen',
    'Palo borracho rosado': 'salmon',
    'Jacarandá': 'mediumpurple'
}

for especie in especies:
    scatter_hd(dicc_medidas[especie], especie, colores[especie])
