lista_numeros = [1, 4, 7, 9]
numero_usuario = 10

while numero_usuario < 0 and numero_usuario > 9:
	numero_usuario = int(input('Ingresa tu numero del 0-9'))

if numero_usuario in lista_numeros:
	print('El numero está dentro de la lista')

else:
	print('El numero no está dentro de la lista')
