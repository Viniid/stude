import time

chapeu = [1, 2, 3, 4, 5]

print("\nCoelhos em suas casas na cartola mágica: ", chapeu)

chapeu [2] = int(input("\nInsira o numero de coelhos a serem substituidos pelo mágico: "))

time.sleep(1)

print("\nquantas casas tem na cartola: ", len (chapeu))

time.sleep(2)

print("\nCoelhos na Cartola após um passe de mágica: ", chapeu)

#time.sleep(2)

del chapeu[2]

time.sleep(3)

print("\nUê desapareceu a casa '2', quantas casas sobraram !? : ", len (chapeu))

time.sleep(3)

print("\nQuantos coelhos sobraram na Cartola: ", chapeu)

time.sleep(3)

print("\nEsse magico é incrivel!, mas !\nCadê os coelhos! ?\n")

time.sleep(2)