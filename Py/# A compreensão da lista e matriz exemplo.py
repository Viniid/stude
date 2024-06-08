# A compreensão da lista permite criar novas listas a partir das existentes de forma concisa e elegante. A sintaxe de uma compreensão de lista tem a seguinte aparência:

# [expressão para elemento na lista se condicional]

# que é equivalente ao seguinte código:

#for element in list:
#    if conditional:
#        expression

# ex:

cubed = [num ** 3 for num in range(5)]
print(cubed)

## Uma tabela de quatro colunas/quatro linhas ‒ uma matriz bidimensional (4x4)
 
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# 3. Você pode aninhar quantas listas desejar, criando assim listas n-dimensionais, por exemplo, matrizes de três, quatro ou até mesmo sessenta e quatro dimensões. Por exemplo:
 
 # Cubo - uma matriz tridimensional (3x3x3)
 
cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
 
print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
 