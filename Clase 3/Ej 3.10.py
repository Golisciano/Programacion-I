rebote = 3/5
contador = 0

entrada = input("Ingresá la altura inicial de la pelota: ")

if entrada.strip() == "":
    altura = 100
else:
    altura = float(entrada)

while altura > 1:
    altura *= rebote
    contador += 1
    print(contador, round(altura, 4))
