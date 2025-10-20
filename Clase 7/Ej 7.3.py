# fileparse.py
import csv

def parse_csv(camion):

    with open(camion) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)
            print(registros)

    return registros
    



parse_csv('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv')