import csv

def parse_csv(filas, select=None, types=None, has_headers=True):
    """
    Parsea un CSV desde un iterable de líneas.
    - filas: iterable de líneas (archivo abierto, lista de strings, etc.)
    - select: lista de nombres de columnas a seleccionar
    - types: lista de funciones para convertir tipos de columna
    - has_headers: si True, interpreta la primera línea como encabezados
    """
    filas = iter(filas)  # Nos aseguramos que sea un iterable

    if has_headers:
        encabezados = next(filas).strip().split(',')  # obtener encabezados

        # Si se seleccionaron columnas específicas
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila.strip():
                continue  # saltear líneas vacías
            fila = fila.strip().split(',')

            # Filtra las columnas seleccionadas
            if indices:
                fila = [fila[i] for i in indices]

            # Aplica conversión de tipos si corresponde
            if types:
                fila = [func(val) for func, val in zip(types, fila)]

            registros.append(dict(zip(encabezados, fila)))
    else:
        registros = []
        for fila in filas:
            if not fila.strip():
                continue
            fila = fila.strip().split(',')
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            registros.append(tuple(fila))

    return registros
