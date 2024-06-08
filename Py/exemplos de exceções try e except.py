
# Exceções:

# TRY e EXCEPT

# Ex: 1

try:
 value = int(input('Digite um número natural: '))
 print('O recíproco de', value, 'é', 1/value) 
except ValueError:
 print('Eu não sei o que fazer.') 
except ZeroDivisionError:
 print('A divisão por zero não é permitida em nosso Universo.') 

################################################################

# Ex: 2

try:
    value = int (input('Insira um número natural:')) 
    print('O recíproco de', value, 'é', 1 / value) 
except ValueError:
    print('Não sei o que fazer.' ) 
except ZeroDivisionError:
    print('Divisão por zero não é permitida em nosso universo.') 
except: 
    print('algo de estranho aconteceu aqui ... Desculpe! ')

################################################################

