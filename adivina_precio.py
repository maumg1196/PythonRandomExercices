"""Codigo para el juego de Chabelo"""
import random

"""Declaramos 3 listas
La primera será la que le quitemos valores
La segunda será nuestra guia y siempre tendrá el valor original
Y la tercera será la que el usuario vaya armando"""
sala = [5, 1, 8, 3, 'x']
sala_show = [5, 1, 8 ,3]
sala_user = ['o', 'o', 'o', 'o']
# Declaramos un contador para las x's
xs = 0

print('Adivina el precio de la sala\n')

"""Creamos un bucle para que repita el proceso de sacar y acomodar la pelota
Las condiciones son que el contador se menor a 3
Que el largo de la lista principal siga siendo mayor a 0
Y que la lista del usuario sea diferente a nuestra lista guia"""
while xs < 3 and len(sala) > 0 and sala_user != sala_show:
	# Pedimos un valo aleatorio entre el 0 y el rango de la lista menos 1
	valor_rand = sala[random.randrange(len(sala))]
	print('El valor que salió es: {}'.format(valor_rand))
	#Si el valor es 'x' aumentamos en 1 el contador
	if valor_rand == 'x':
		xs += 1
		print('Llevas {} x\'s'.format(xs))
	#Si el valor es un numero le damos la opción de acomodar el numero
	else:
		#Pedimos la posición en la que quiere acomodar el numero
		posicion = int(input('En que posicion lo quieres poner? 1-4\n'))
		#Ponemos el numero en la posición que nos dio en la 3ra lista
		sala_user[posicion-1] = valor_rand
		#Comparamos los elementos en las mismas posiciones
		if sala_user[posicion-1] == sala_show[posicion-1]:
			#Si son iguales removemos el numero de la lista principal
			sala.remove(valor_rand)
		else:
			#Si son diferentes aumentamos el contador
			xs += 1
			print('Llevas {} x\'s'.format(xs))

print('El valor verdadero es: {}'.format(sala_show))
print('Tu resultado del juego es : {}'.format(sala_user))

if sala_show == sala_user:
	print('¡¡¡¡Felicidades has ganado una sala!!!')
else:
	print('Lo siento cuate :C')
