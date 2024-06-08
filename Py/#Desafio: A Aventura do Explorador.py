 #Desafio: A Aventura do Explorador

# Entrada
#quantidade_passos = int(input())

#//TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
#// Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#// Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

q_p = int(input())


if q_p <= 0:
    print("Nenhum passo dado na floresta.")
else:
    for i in range(q_p + 1 ):
        if i == 1:
            print("Explorador:", i, "passo"  )
        elif i > 1: 
            print("Explorador:", i, "passos")
    
    