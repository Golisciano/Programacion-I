import random

def tirar(n=5):
    return [random.randint(1,6) for _ in range(n)]

def es_generala(tirada):
    return all(dado == tirada[0] for dado in tirada)

def prob_generala(N):
    G = 0
    for _ in range(N):
        dados = tirar()
        objetivo = max(set(dados), key=dados.count)
        guardados = [d for d in dados if d == objetivo]
        dados = tirar(5 - len(guardados))
        guardados += [d for d in dados if d == objetivo]
        dados = tirar(5 - len(guardados))
        guardados += [d for d in dados if d == objetivo]
        if len(guardados) == 5:
            G += 1
    return G / N

if __name__ == "__main__":
    N = 100000
    print(f"Probabilidad estimada de obtener generala: {prob_generala(N):.6f}")
