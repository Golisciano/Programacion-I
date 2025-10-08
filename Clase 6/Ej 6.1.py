import random

def tirar():
    return [random.randint(1,6) for _ in range(5)]

def es_generala(tirada):
    return all(dado == tirada[0] for dado in tirada)

N = 100000
G = sum([es_generala(tirar()) for _ in range(N)])
prob = G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Probabilidad estimada: {prob:.6f}')
