import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x, y

def estimar_pi(N=100000):
    dentro = 0
    for _ in range(N):
        x, y = generar_punto()
        if x**2 + y**2 < 1:
            dentro += 1
    return 4 * dentro / N

if __name__ == "__main__":
    N = 100000
    pi_estimado = estimar_pi(N)
    print(f"Con {N} puntos, la estimación de pi es: {pi_estimado:.6f}")
