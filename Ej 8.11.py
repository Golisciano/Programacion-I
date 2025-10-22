def valor_absoluto(n):
    """
        Devuelve el valor absoluto de un número entero o flotante.

    Parámetros:
        n: número del cual se quiere el valor absoluto.

    Retorna:
        el valor absoluto de n.
    """
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    """
        Calcula la suma de todos los números pares de una lista de enteros.

    Parámetros:
        l: lista de números enteros.

    Retorna:
         suma de los elementos pares de la lista.
    """
    res = 0
    for e in l:
        # Si el número es par, se suma
        if e % 2 == 0:
            res += e
        else:
            res += 0 

    return res


def veces(a, b):
    """
        Calcula el producto de dos enteros a y b sumando a consigo mismo b veces.

    Parámetros:
        a : multiplicando
        b : número de veces que se suma a

    Retorna:
        int: resultado de a * b
    """
    res = 0
    nb = b  # nb es el contador que disminuye hasta 0

    while nb != 0:
        res += a
        nb -= 1

    return res


def collatz(n):
    """
        Calcula la longitud de la secuencia de Collatz para un número entero positivo n.

    La secuencia de Collatz se define:
        - Si n es par: n -> n / 2
        - Si n es impar: n -> 3 * n + 1
    La secuencia termina cuando n llega a 1.

    Parámetros:
        n : número entero positivo para calcular la secuencia.

    Retorna:
        int: cantidad de pasos hasta llegar a 1 (incluyendo el primer número).
    """
    res = 1 

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res += 1

    return res