largest_number = -99999999
counter = 0

while True:
    number = int(input("Digite um número ou digite -1 para terminar o programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("TO maior número é", largest_number)
else:
    print("Você não inseriu nenhum número.")

