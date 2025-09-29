cadena = input("Ingrese una frase: ")

resultado = ""
for letra in cadena:
    resultado += letra
    if letra.lower() == "a":
        resultado += "pa"
    elif letra.lower() == "e":
        resultado += "pe"
    elif letra.lower() == "i":
        resultado += "pi"
    elif letra.lower() == "o":
        resultado += "po"
    elif letra.lower() == "u":
        resultado += "pu"

print("Resultado:", resultado)
