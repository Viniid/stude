#estação meteorológica automática

#O dispositivo registra a temperatura do ar a cada hora e faz isso durante todo o mês. Isso gera um total de 24 × 31 = 744 valores. Vamos tentar criar uma lista capaz de armazenar todos esses resultados.

##

temps = [[0.0 for h in range(24)] for d in range(31)]

#################################################################################################################

# Agora é hora de determinar a temperatura média mensal ao meio-dia. Adicione todas as 31 leituras gravadas ao meio-dia e divida a soma por 31. Você pode supor que a temperatura da meia-noite é armazenada primeiro. Aqui está o código relevante:

temps = [[0.0 for h in range(24)] for d in range(31)]

#
# A matriz é magicamente atualizada aqui.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura média ao meio-dia:", average)

#################################################################################################################

# Agora, encontre a temperatura mais alta durante todo o mês - veja o código:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("A maior temperatura foi:", highest)

#################################################################################################################

# Agora conte os dias em que a temperatura ao meio-dia era de pelo menos 20 ℃:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "dias estavam quentes.")
 
################################################################################################################

