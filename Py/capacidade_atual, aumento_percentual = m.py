capacidade_atual, aumento_percentual = map(int, input().split())

storage = capacidade_atual + ((aumento_percentual*capacidade_atual)//100)

print(storage)

