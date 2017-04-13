numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(lista):
    pares = []
    impares = []

    for numero in lista:
        if numero%2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares

pares, impares = separar(numeros)
print(pares)
print(impares)
