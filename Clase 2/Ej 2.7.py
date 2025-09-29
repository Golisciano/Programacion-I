def buscar_precio(fruta):
    encontrado = False
    with open('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/precios.csv', 'rt') as f:
     for linea in f:
         try:            
             nombre, precio = linea.strip().split(',') 
         except:
         
             continue
    
         if nombre.lower() == fruta.lower():   # comparo en minúsculas
           print(f'El precio de la {fruta} es:', {precio})
           encontrado = True
           break
    
    if not encontrado:
        print(f"{fruta} no figura en el listo de precios")
        

buscar_precio("Naranja")
buscar_precio("anana")