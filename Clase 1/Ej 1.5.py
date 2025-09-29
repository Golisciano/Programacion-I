altura = 100
rebote = 3/5
contador = 0

while altura > 1:  
    altura *= rebote
    contador += 1
    print(contador, round(altura))
    