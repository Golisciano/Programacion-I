total = 0.0

with open('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv', 'rt') as f:
        next(f)
        for linea in f:
            fila = linea.strip().split(',')
            nombre = fila[0]
            cajones = int(fila[1])
            precio = float(fila[2])
       
            total += cajones * precio
            
print('Costo total es de:', total)