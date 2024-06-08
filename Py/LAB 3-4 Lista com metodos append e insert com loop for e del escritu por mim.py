# etapa 1

beatles = []

import time

print("\nOs Beatles") 

time.sleep (2)

print("\nEtapa 1:", beatles, "\n")

time.sleep (2)

print('Criando uma banda\n')

time.sleep (2)

# etapa 2

beatles.append("John Lennon")
beatles.append('Paul McCartney')
beatles.append('George Harrison')

print("Etapa 2:", beatles, "\n")

time.sleep (3)

# etapa 3

print('Três novos membros entram para o grupo\n')

time.sleep (2)

for i in range (3):
    beatles.append(input("São: "))

time.sleep (3)

print("\nEtapa 3:", beatles, "\n")

time.sleep (3)

# etapa 4
print('Mas, infelismente dois dos novos integantes saem da banda\n')

time.sleep (3)

del beatles [-2]
del beatles [-1]

print("Etapa 4:", beatles, "\n")

time.sleep (3)

# passo 5

print('E por fim, o ultimo integrante que faltava, entra para a banda\n')

time.sleep (3)

beatles.insert (0, 'Ringo Starr')

time.sleep (3)

print("Etapa 5:", beatles, "\n")

time.sleep (3)

# testando o tamanho da lista

print("Formando os", len(beatles), "Fabulosos\n" )

time.sleep (3)