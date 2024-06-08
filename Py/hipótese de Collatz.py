# para contar as etapas é necessario criar uma variavel com valor 0 fora do laço e a mesma veriavel com a chave, +=, que tem a função de adicionar um a cada ciclo do laço; já o laço tem quer ter a condição de ser diferente de 1, pois ao alcaçr o valor 1 encerra o laço.  

c0 = int(input("insira um numero inteiro: ")) 
etapa = 0

while c0 != 1: 

    etapa += 1

    if c0 % 2 == 0:
        c0 = c0 /2
    else:
        c0 = 3 * c0 + 1

    print(int(c0))

print("Etapas = ", etapa)