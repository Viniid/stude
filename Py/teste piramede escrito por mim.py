blocos = int(input("Insira o número de blocos:"))  
# Escreva seu código aqui.
altura = 0

while True:

    if blocos > 0:

        altura += 1
        blocos -= 1 * altura

if blocos % altura == 1:
    break
    print("quantidade insulficiente de blocos: ")
else:        
    print("A altura da pirâmide:", altura)
 
