import random

def cumpleanios_repetidos(n):
    dias = [random.randint(1,365) for _ in range(n)]
    return len(dias) != len(set(dias))

def prob_cumples(N, n_personas):
    rep = sum(cumpleanios_repetidos(n_personas) for _ in range(N))
    return rep / N

if __name__ == "__main__":
    N = 100000
    prob30 = prob_cumples(N, 30)
    print(f"Probabilidad con 30 personas: {prob30:.6f}")

    n = 2
    while True:
        p = prob_cumples(N, n)
        if p > 0.5:
            print(f"Con {n} personas, la probabilidad supera 0.5: {p:.6f}")
            break
        n += 1
