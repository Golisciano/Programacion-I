def busqueda_lineal_lordenada(lista, e):

    for elemento in lista:
        if elemento == e:
            return True
        elif elemento > e:
            return False
    return False


lista = [1, 3, 5, 7, 9]
print(busqueda_lineal_lordenada(lista, 5))  # True
print(busqueda_lineal_lordenada(lista, 6))  # False
print(busqueda_lineal_lordenada(lista, 10)) # False
