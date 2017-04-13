def agregar_una_vez(lista, elemento):
    try:
        if elemento not in lista:
            lista.append(elemento)
        else:
            raise ValueError
    except ValueError:
        print('Error: Imposible añadir elementos duplicados => {}'.format(elemento))

lista_prueba = [1, 5, "Hola",-2]
elemento1 = int(input('Ingresa un 10'))
agregar_una_vez(lista_prueba, elemento1)
elemento2 = input('Ingresa un Hola')
agregar_una_vez(lista_prueba, elemento2)
elemento3 = int(input('Ingresa un -2'))
agregar_una_vez(lista_prueba, elemento3)
print(lista_prueba)
