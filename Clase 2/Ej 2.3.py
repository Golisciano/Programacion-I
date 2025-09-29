with open('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/precios.csv', 'rt') as f:
    
     for linea in f:
       fruta, precio = linea.strip().split(',') #separa en dos partes: nombre y precio.
       if fruta.lower() == 'naranja':   # comparo en minúsculas
           print('El precio de la naranja es:', precio)
           break