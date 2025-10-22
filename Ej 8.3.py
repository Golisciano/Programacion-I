import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True, silence_errors=False):
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    registros = []

    try:
        with open(nombre_archivo, 'rt', encoding='utf-8') as f:
            filas = csv.reader(f)
            if has_headers:
                encabezados = next(filas)
                if select:
                    indices = [encabezados.index(nombre_col) for nombre_col in select]
                    encabezados = select
                else:
                    indices = list(range(len(encabezados)))

                for n_fila, fila in enumerate(filas, start=1):
                    if not fila:
                        continue
                    fila = [fila[index] for index in indices]
                    if types:
                        try:
                            fila = [func(val) for func, val in zip(types, fila)]
                        except ValueError as e:
                            if not silence_errors:
                                print(f'Fila {n_fila}: No se pudo convertir {fila}. Motivo: {e}')
                            continue  
                    registro = dict(zip(encabezados, fila))
                    registros.append(registro)
            else: 
                for n_fila, fila in enumerate(filas, start=1):
                    if not fila:
                        continue
                    if types:
                        try:
                            fila = [func(val) for func, val in zip(types, fila)]
                        except ValueError as e:
                            if not silence_errors:
                                print(f'Fila {n_fila}: No se pudo convertir {fila}. Motivo: {e}')
                            continue
                    registros.append(tuple(fila))

    except FileNotFoundError:
        if not silence_errors:
            print(f'Error: no se encontró el archivo "{nombre_archivo}".')

    return registros

camion = parse_csv('C:/Users/toshiba/Desktop/unsam/ejercicios_python/Data/camion.csv', types=[str, int, float])
print(camion)