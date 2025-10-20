def busqueda_binaria(lista, x, verbose=False):
    '''
    Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos


def donde_insertar(lista, x):
    '''
    Devuelve la posición donde x se encuentra o donde debería insertarse
    en una lista ordenada de menor a mayor.
    '''
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            return medio
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return izq


def insertar(lista, x):
    '''
    Inserta x en la lista ordenada si no está.
    Devuelve la posición del elemento (insertado o existente).
    '''
    pos = donde_insertar(lista, x)
    # Si el elemento no está en la lista, insertarlo en su posición correcta
    if pos == len(lista) or lista[pos] != x:
        lista.insert(pos, x)
    return pos


# --- Ejemplo de uso ---
if __name__ == "__main__":
    lista = [1, 2, 3]
    print(insertar(lista, 5))  # 1
    print(lista)               # [1, 2, 3]
    print(insertar(lista, 1))  # 3
    print(lista)               # [1, 2, 3, 4]
    print(insertar(lista, 3))  # 0
    print(lista)               # [0, 1, 2, 3, 4]
