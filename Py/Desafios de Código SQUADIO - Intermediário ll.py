positivos = 0
negativos = 0
    
numero = ()

while numero != 0:
    numero = int(input())
    if numero > 0:
        print('positivo!')
        positivos += 1
        continue
    elif numero < 0:   
        print('negativo!')
        negativos +=1
        continue  
    else:
        print(f"{positivos} números positivos, {negativos} números negativos")