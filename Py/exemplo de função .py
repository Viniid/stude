# Exemplo :

##### ! O problema:

print("Entre um valor: ")
a = int(input())

print("Entre um valor: ")
b = int(input())

print("Entre um valor: ")
c = int(input())

##### ! Criando a função:

def message():
    print("Entre um valor: ")
 
print("Começamos aqui.")
message()
print("terminamos aqui.")
 
##### ! Resolvendo o problema:

def message():
    print("Entre um valor: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

##### ! É possivel incrementar um argumento na função e evocar com uma variavel:


def hello(name): # definindo uma função
    print("Olá,", name) # o corpo da função
 
 
name = input("Entre um valor: ") # Variavel (argumento, incrementado na função) 
 
hello(name) # chamando a função

##### ! função com argumento deve ser preenchido :

def message(number):
 print("O número escolhido foi:", number)

message(int(input("insira um numero: "))) 

# pode ser criado uma variavel externa para a interação ou 
# pode ser atribuido o valor diretamente na função, 
# ou  até mesmo utilizar outra função no argumento para a interação com a possibilidade de utilizar str. 

#####

def introduction(first_name, last_name): # Mais de um parametro definido 
    print("Olá meu nome é", first_name, last_name)
 
introduction((input("insira o primeiro nome: ")), "Skywalker") 
# Todos parametros devem ser definidos ao evocar a função,
# É possivel utilizar outra função ou até mesmo instruir com uma str o que fazer
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
 
##### ! Tambem é possivel especificar qual o parametro especifico que deseja atribuir o valor

def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond") 
# nesse caso é necessario colocar qual parametro deseja atribuir o valor;
# a atribuição é similar ha uma variavel e deve ser identica ao parametro da função, caso contrario dara erro no codigo
introduction(last_name = "Skywalker", first_name = "Luke")

##### É possivel fazer equação e contas na saida da função, muito util para a saida de valores

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
 
adding(1,2,3)

# É possivel definir quais parametros devem receber os valore especificos, 

# ex: adding(c = 1, a = 2, b = 3) 

# Se os valores estiver na ordem correta é possivel colocar o valor na ordem certa 
# e depois adicionar os valores nos parametros respectivos 

# ex: adding(3, c = 1, b = 2)

# Após adicionar um valor no parametro especifico não é possivel especifica-lo depois, 
# dará erro pois terão dois valores para o mesmo parametro 

# ex: adding(3, a = 1, b = 2)

##### Estipulando o valor do parametro no cabeçalho da função 

def introduction(first_name, last_name="Smith"):
     print("Olá meu nome é", first_name, last_name)
 
introduction("vinicius",) 

# Se o segundo parametro não for estipulado valera o valor do cabeçalho,
# Agora se o segundo parametro for estipulado o valor estipulado subistituira o valor do cabeçalho 

##### Exemplo de função com Variavel 

def address(street, city, postal_code):
    print("Seu endereço é:", street, "St.,", city, postal_code)
 
s = input("Street: ")          # Variavel
p_c = input("Código postal: ") # Variavel
c = input("Cidade: ")          # Variavel

address(s, c, p_c)

##### Exemplos Variaveis

#Ex. 1
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # saídas: 3
subtra(2, 5) # saídas: -3
 
 
#Ex. 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # saídas: 3
subtra(b=2, a=5) # saídas: 3
 
#Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # saídas: 3
subtra(5, 2) # saídas: 3

##### Da para somar str ex:

def intro(a="James Bond", b="Bond"):
     print("Meu nome é", b + ".", a + ".")
 
intro()
 
#####

def add_numbers(a ,b=2, c=0 ):
    print(a + b + c)
 
add_numbers(a=1, c=3)

# todos parametros podem ser atribuidos valores, porêm fica o exemplo acima 
 
#####

# Return () = Tem duas variaveis, uma como expressão e a outra sem expressão
# expressão sem argumento e variavel de retorrno

def happy_new_year(wishes = True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not wishes:
        return
 
    print("Feliz Ano Novo!")

happy_new_year()  # pode ter o argumento boolean  "False", finalizando o processo no return

# já a segunda variante contêm argumnento

def boring_function():
    return 123
 
x = boring_function() 

# quando é aderido por uma variavel  retorna o valor do return, 
# caso não seja aderida por uma variavel 
 
print("A aborrecimento_função retornou seu resultado. Isso é:", x)


##### ! Nota: None é uma palavra-chave.

#Existem apenas dois tipos de circunstâncias em que None pode ser usada com segurança:

#quando você a atribui a uma variável (ou a retorna como resultado de uma função)
#quando você a compara com uma variável para diagnosticar seu estado interno.

# ex:

value = None
if value is None:
    print("Desculpe, você não carrega nenhum valor")

# outro exemplo de  return e none

def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))

######################################################################################

# Função com lista

def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
 
print(list_sum([5, 4, 3])) 
#print(list_sum(5)) # no caso de lista é necessario inserir uma lista, se apresentara um erro "sem itens para interação" 
# Isso é causado pelo fato de que um único valor inteiro não deve ser iterado pelo loop for.

#######################################################################################
 
# ! Exemplo de lista interativa em uma função

def strange_list_fun(n):
    strange_list = []
 
    for i in range(0, n):  
        # for com a função "range", ira criar uma lista começando com zero até o numero inserido pelo usuario 
        strange_list.insert(0, i) 
            # insert adiciona os valores gerados pelo for a variavel, "strange_list", uma lista vazia 
 
    return strange_list # retorna o valor à lista strange_list_fun

print(strange_list_fun(int(input("insira um numero inteiro real: "))))