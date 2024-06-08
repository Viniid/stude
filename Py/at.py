

blocks = int(input("Insira o número de blocos:"))  
 # Escreva seu código aqui.
 
altura = 0

while blocks != 0:

    if blocks % 2 == 0:
        altura += 1
    else:
        blocks % 2 == 1     
        altura += 1

jls_extract_var = print
jls_extract_var("A altura da pirâmide:", altura)
