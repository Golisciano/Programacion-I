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

def scatter_hd(lista_de_pares):
    alturas = [par[0] for par in lista_de_pares]
    diametros = [par[1] for par in lista_de_pares]

    plt.scatter(diametros, alturas, alpha=0.5, color='mediumseagreen', edgecolor='black')
    plt.title('Relación entre altura y diámetro de Jacarandás')
    plt.xlabel('Diámetro (cm)')
    plt.ylabel('Altura (m)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

arboleda = leer_arboles("C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/arbolado.csv")

A_D_jacarandas = [(float(arbol['altura_tot']), float(arbol['diametro'])) 
                  for arbol in arboleda 
                  if arbol['nombre_com'] == 'Jacarandá']

print("Primeras 10 tuplas (altura, diámetro) de Jacarandás:")
print(A_D_jacarandas[:10])
scatter_hd(A_D_jacarandas)
