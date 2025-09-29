def costo_camion(nombre_archivo):
    
    total = 0.0
    with open(nombre_archivo, 'rt') as f:
                next(f)
                for linea in f:
                    fila = linea.strip().split(',')
                    cajones = int(fila[1])
                    precio = float(fila[2])
                    total += cajones * precio
    return total


costo = costo_camion('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv')            
print('Costo total es de:', costo)