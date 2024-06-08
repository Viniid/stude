# Utilize a estrutura de repetição "while" para desenvolver um algoritmo, em Python, que permita que um usuário seja capaz de inserir apenas números não-negativos. Caso o usuário digite um valor negativo, o algoritmo deverá interromper esse laço de repetição.

Atividade_1 = True

while Atividade_1:

   numero = int(input("\nInsira um número: "))

   print("____________________________________________________________________________")

   if numero >= 0:

       print("\nPossitivo, Prossiga!")
   else:

       print("\nNegativo!" 
       
       "\n\nInterrompendo esse laço de repetição."
       
       "\n\nObrigado pelo teste, Volte Sempre!")

       print("____________________________________________________________________________" "\n")

       Atividade_1 = False
    
    
