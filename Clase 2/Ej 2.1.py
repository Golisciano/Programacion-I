with open('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv', 'rt') as f:
        data = f.read()
        
        print(data)
        
        data
        
with open('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv', 'rt') as f:
        
        for line in f:
            print(line, end = '')
            
            for line in f:
                row = line.split(',')
                print(row)