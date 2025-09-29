def multiplicar(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado

print('     ', end='')
for j in range(10):
    print(f'{j:>4d}', end='')
print()
print('-'*45)

for i in range(10):
    print(f'{i:>2d}:', end='')
    for j in range(10):
        print(f'{multiplicar(i, j):>4d}', end='')
    print() 
    
