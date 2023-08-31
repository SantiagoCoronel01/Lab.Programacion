def parOimpar(numeros):
    pares= []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return [pares, impares]


n = [2, 5, 6, 7, 8]
print(parOimpar(n))