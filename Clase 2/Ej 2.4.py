import gzip

with gzip.open('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')