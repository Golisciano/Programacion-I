import random

def envido_mano():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor, palo) for valor in valores for palo in palos]
    random.shuffle(naipes)
    mano = [naipes.pop(), naipes.pop(), naipes.pop()]
    return mano

def calcular_envido(mano):
    puntos = {10:0, 11:0, 12:0}
    for i in range(1,10):
        puntos[i] = i
    max_envido = 0
    for i in range(3):
        for j in range(i+1,3):
            v1, p1 = mano[i]
            v2, p2 = mano[j]
            if p1 == p2:
                e = puntos[v1] + puntos[v2] + 20
                if e > max_envido:
                    max_envido = e
    if max_envido == 0:
        max_envido = max(puntos[v] for v, _ in mano)
    return max_envido

def prob_envido(N=100000):
    c31 = c32 = c33 = 0
    for _ in range(N):
        mano = envido_mano()
        e = calcular_envido(mano)
        if e == 31: c31 += 1
        if e == 32: c32 += 1
        if e == 33: c33 += 1
    return c31/N, c32/N, c33/N

if __name__ == "__main__":
    N = 200000
    p31, p32, p33 = prob_envido(N)
    print(f"Probabilidad de 31: {p31:.6f}")
    print(f"Probabilidad de 32: {p32:.6f}")
    print(f"Probabilidad de 33: {p33:.6f}")