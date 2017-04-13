def perimetro_cuadrado(lado):
	return lado*4

def perimetro_circulo(diametro):
	return diametro*3.14

def perimetro_triangulo(lado1, lado2, lado3):
	return lado1+lado2+lado3

def perimetro_pentagono(lado):
	return lado*5

def area_cuadrado(lado):
	return lado*lado

def area_circulo(radio):
	return (radio**2)*3.14

def area_triangulo(base, altura):
	return base*altura

def area_pentagono(lado, apotema):
	return 0.5*perimetro_pentagono(lado)*apotema

while True:
    opcion = input('Que es lo que deseas obtener?\nPerimetro o Area\n').lower()
    if opcion == 'perimetro':
        opcion_figura = input("""De que figuras quieres el perimetro?
            Cuadrado\nCirculo\nTriangulo\nPentagono""").lower()
        if opcion_figura == 'cuadrado':
            lado = float(input('Ingrese el valor de los lados'))
            print(perimetro_cuadrado(lado))
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
        elif opcion_figura == 'circulo':
            diametro = float(input('Ingrese el valor del diametro'))
            print(perimetro_circulo(diametro))
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
        elif opcion_figura == 'triangulo':
            lado1 = float(input('Ingrese el valor del primer lado'))
            lado2 = float(input('Ingrese el valor del segundo lado'))
            lado3 = float(input('Ingrese el valor del tercer lado'))
            print(perimetro_triangulo(lado1, lado2, lado3))
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
        elif opcion_figura == 'pentagono':
            lado = float(input('Ingrese el valor de los lados'))
            print(perimetro_pentagono(lado))
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
        else:
            print('Opcion inexistente')
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
    elif opcion == 'area':
        opcion_figura = input("""De que figuras quieres el area?
            Cuadrado\nCirculo\nTriangulo\nPentagono""").lower()
        if opcion_figura == 'cuadrado':
            lado = float(input('Ingrese el valor de los lados'))
            print(area_cuadrado(lado))
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
        elif opcion_figura == 'circulo':
            diametro = float(input('Ingrese el valor del diametro'))
            print(area_circulo(diametro))
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
        elif opcion_figura == 'triangulo':
            base = float(input('Ingrese el valor de la base'))
            altura = float(input('Ingrese el valor de la altura'))
            print(area_triangulo(base, altura))
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
        elif opcion_figura == 'pentagono':
            lado = float(input('Ingrese el valor de los lados'))
            ap = float(input('Ingrese el valor de la apotema'))
            print(area_pentagono(lado, ap))
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
        else:
            print('Opcion inexistente')
            repetir = input('Desea repetir el programa?S/N').lower()
            if repetir == 's':
                pass
            else:
                break
    else:
        print('Opcion inexistente')
        repetir = input('Desea repetir el programa?S/N').lower()
        if repetir == 's':
            pass
        else:
            break
