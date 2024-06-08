texto = input("insira o texto: ")

vogais = "aeiou"
reto = ""

for letra in texto:
    if letra not in vogais:
        reto += letra
        
print(reto)