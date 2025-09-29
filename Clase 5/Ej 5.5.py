def invertir_lista(lista):
    invertida = []
    for e in lista:  
        invertida.insert(0, e) 
    return invertida

if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

    print(invertir_lista(lista1))
    print(invertir_lista(lista2))  