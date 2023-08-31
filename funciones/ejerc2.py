def contarPalabras(frase):
    fraseContar = frase.split()
    cantidadPal = len(fraseContar)
    return cantidadPal

fraseContar = "El señor de los anillos"


print(contarPalabras(fraseContar))
