import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    """
    Parsea un archivo CSV en una lista de registros.
    Puede seleccionar un subconjunto de columnas, aplicar conversión de tipos
    y manejar archivos con o sin encabezados.
    """
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)

        # Lee los encabezados si existen
        if has_headers:
            encabezados = next(filas)

            # Si se seleccionaron algunas columnas
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

            registros = []
            for fila in filas:
                if not fila:    # Saltea filas vacías
                    continue

                # Filtra las columnas seleccionadas
                if indices:
                    fila = [fila[index] for index in indices]

                # Aplica conversión de tipos si corresponde
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]

                # Arma el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            # Sin encabezados → crea tuplas
            registros = []
            for fila in filas:
                if not fila:
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                registros.append(tuple(fila))

    return registros
