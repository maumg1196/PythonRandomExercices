try:
    resultado = 10/0
except:
    print('Error: No es posible dividir entre 0')

lista[1,2,3,4,5]
try:
    lista[10]
except:
    print('Error el indice al que intentas acceder se encuentra fuera de rango')
    print('El largo de la lista es de: {}'.format(len(lista)))

colores = {'rojo': 'red',
           'verde': green,
           'negro':black,}

try:
    colores['blanco']
except:
    print('La clave no existe debes probar con una existente')
