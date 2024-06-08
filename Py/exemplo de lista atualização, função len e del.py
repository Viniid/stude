numbers = [10, 5, 7, 2, 1]
print("Conteúdo da lista original:", numbers) # Imprimindo conteúdo da lista de originais.
numbers[0] = 111
print("Conteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.
numbers[1] = numbers[4] # Copiando o valor do quinto elemento para o segundo.
print ("\nComprimento da lista:", len (numbers)) # Imprimindo comprimento de lista anterior.
print("Conteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

###

del numbers[1] # Removendo o segundo elemento da lista.
print ("\nComprimento da lista:", len (numbers))
print ("Comprimento da lista:", numbers)
