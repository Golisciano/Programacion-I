def rebotar(altura_inicial, rebotes):
    """Calcula y muestra la altura luego de cada rebote."""
    altura = altura_inicial
    factor = 3 / 5
    for i in range(1, rebotes + 1):
        altura *= factor
        print(f"{i}:  {altura:.2f}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 3:
        altura_inicial = float(sys.argv[1])
        rebotes = int(sys.argv[2])
    else:
        print("Ejecutando en modo interactivo (Spyder o sin argumentos)")
        altura_inicial = float(input("Ingresá la altura inicial: "))
        rebotes = int(input("Ingresá la cantidad de rebotes: "))

    rebotar(altura_inicial, rebotes)
