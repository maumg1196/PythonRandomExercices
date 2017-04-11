lista1 = ['H', 'o', 'l', 'a', 'M', 'u', 'n', 'd', 'o']
lista2 = ['A', 'd', 'i', 'o', 's', 'L', 'u', 'n', 'a']
lista_final = []

for element in lista1:
	if element in lista2:
		if element in lista_final:
			pass
		else:
			lista_final.append(element)
	else:
		pass

print(lista_final)
