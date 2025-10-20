import random
import matplotlib.pyplot as plt

# --- Búsquedas con conteo de comparaciones ---

def busqueda_secuencial_comps(lista, x):
    comps = 0
    for i, elem in enumerate(lista):
        comps += 1
        if elem == x:
            return i, comps
    return -1, comps


def busqueda_binaria_comps(lista, x):
    izq = 0
    der = len(lista) - 1
    comps = 0

    while izq <= der:
        comps += 1
        medio = (izq + der) // 2

        if lista[medio] == x:
            return medio, comps
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1

    return -1, comps


# --- Experimentos ---

def experimento_secuencial_promedio(lista, m, k):
    """Corre k experimentos con m búsquedas aleatorias y devuelve el promedio de comparaciones."""
    comps_totales = 0
    for _ in range(k):
        x = random.randint(0, m*2)  # elemento que puede o no estar
        _, comps = busqueda_secuencial_comps(lista, x)
        comps_totales += comps
    return comps_totales / k


def experimento_binario_promedio(lista, m, k):
    """Corre k experimentos con búsqueda binaria y devuelve el promedio de comparaciones."""
    comps_totales = 0
    for _ in range(k):
        x = random.randint(0, m*2)
        _, comps = busqueda_binaria_comps(lista, x)
        comps_totales += comps
    return comps_totales / k


# --- Gráfico comparativo ---

def graficar_bbin_vs_bseq(m, k):
    largos = range(1, 257)
    comps_secuencial = []
    comps_binaria = []

    for n in largos:
        lista = list(range(n))
        comps_secuencial.append(experimento_secuencial_promedio(lista, m, k))
        comps_binaria.append(experimento_binario_promedio(lista, m, k))

    plt.figure(figsize=(8, 5))
    plt.plot(largos, comps_secuencial, label='Búsqueda Secuencial', marker='o')
    plt.plot(largos, comps_binaria, label='Búsqueda Binaria', marker='s')
    plt.title('Comparación: Búsqueda Secuencial vs Binaria')
    plt.xlabel('Largo de la lista')
    plt.ylabel('Comparaciones promedio')
    plt.legend()
    plt.xlim(0, 256)
    plt.ylim(0, max(comps_secuencial)*1.1)
    plt.grid(True)
    plt.show()


# --- Ejecución del experimento ---

graficar_bbin_vs_bseq(m=1000, k=1000)
