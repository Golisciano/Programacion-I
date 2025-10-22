def sumar_enteros_ciclo(a, b):
    """Suma todos los enteros entre a y b inclusive usando un ciclo"""
    total = 0
    for i in range(a, b + 1):
        total += i
    return total

# Ejemplo
print(sumar_enteros_ciclo(1, 5))


def sumar_enteros_constante(a, b):
    """Suma todos los enteros entre a y b inclusive en tiempo constante"""
    return (b - a + 1) * (a + b) // 2

# Ejemplo
print(sumar_enteros_constante(1, 5)) 
