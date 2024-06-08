blocks = int(input("Insira o número de blocos:"))  
# Escreva seu código aqui.
altura = 0

while True:
    
    # if blocks == 2:
    #         altura == 1
    # if blocks < 2:
    #     altura = 1
        
    if blocks > 0:
        blocks = blocks // 2
        altura += 1
        
    else:
        break

print("A altura da pirâmide:", altura)