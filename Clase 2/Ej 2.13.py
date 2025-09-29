def en_geringoso(palabra):
    """Traduce una palabra al geringoso"""
    traduccion = ''
    for c in palabra:
        if c.lower() in 'aeiou':
            traduccion += c + 'p' + c
        else:
            traduccion += c
    return traduccion


def diccionario_geringoso(lista_palabras):
    """Devuelve un diccionario {palabra: palabra_en_geringoso}"""
    geringoso = {}
    for palabra in lista_palabras:
        geringoso[palabra] = en_geringoso(palabra)
    return geringoso



palabras = ['banana', "manzana", "mandarina"]
dicc = diccionario_geringoso(palabras)
print(dicc)
