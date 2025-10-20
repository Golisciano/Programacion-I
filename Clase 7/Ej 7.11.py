def donde_insertar(lista, x, verbose=False):
    """
    Devuelve la posición donde x se encuentra o donde debería insertarse
    en una lista ordenada de menor a mayor.
    """
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            return medio  # lo encontró, devuelve su posición
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    # Si no se encontró, izq indica la posición de inserción
    return izq


print(donde_insertar([0, 2, 4, 6], 3))  # ➜ 2
print(donde_insertar([0, 2, 4, 6], 4))  # ➜ 2
print(donde_insertar([0, 2, 4, 6], 7))  # ➜ 4
print(donde_insertar([0, 2, 4, 6], -1)) # ➜ 0
