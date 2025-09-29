def buscar_u_elemento(lista, elem):
    pos = -1
    for i, x in enumerate(lista):
        if x == elem:
            pos = i
    return pos


def buscar_n_elemento(lista, elem):
    contador = 0
    for x in lista:
        if x == elem:
            contador += 1
    return contador


def maximo(lista):
    m = 0  
    for e in lista:
        if e > m:
            m = e
    return m

if __name__ == "__main__":
    print(buscar_u_elemento([1,2,3,2,3,4], 1))  
    print(buscar_u_elemento([1,2,3,2,3,4], 2))  
    print(buscar_u_elemento([1,2,3,2,3,4], 3))  
    print(buscar_u_elemento([1,2,3,2,3,4], 5))  

    print(buscar_n_elemento([1,2,3,2,3,4], 1))  
    print(buscar_n_elemento([1,2,3,2,3,4], 2))  

    print(maximo([1,2,3,2,3,4]))  
    print(maximo([7,1,5,9,2]))    

