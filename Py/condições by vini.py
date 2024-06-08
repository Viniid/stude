number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

if number1 > number2: 
    larger_number = number1
    print("Larger Number 1:", larger_number)

elif number2 > number3: 
    larger_number = number2
    print("Larger Number 2:", larger_number)

elif number3 > number1: 
    larger_number = number3
    print("Larger Number 3:", larger_number)
    
else:
    print("Fim")
