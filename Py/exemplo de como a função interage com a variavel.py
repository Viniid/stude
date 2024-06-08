def my_function(n):
    print("Eu obtive", n)
    n += 1
    print("Eu tenho", n)


var = 2
my_function(var) # a função só tem efeito na variavel se a mesma for especificada na função ou for utilizada a função "global"
print(var)

############################################################################################################################

# EXEMPLOS:

# ex: 1
# Uma variável que existe fora de uma função tem escopo dentro do corpo da função
var = 2
  
def mult_by_var(x):
    return x * var
 
print(mult_by_var(7)) # saídas: 14

##################################################################

# ex:2
# função define uma variável com o mesmo nome

def mult(x):
    var = 5
    return x * var
 
 
print(mult(7)) # saídas: 35

##################################################################

# ex:3
# função define1 uma variável com o mesmo nome

def mult(x):
    var = 7
    return x * var
 
 
var = 3
print(mult(7)) # saídas: 49

##################################################################

# ex: 4
# Uma variável que existe dentro de uma função tem escopo dentro do corpo da função

def adding(x):
    var = 7
    return x + var
 
 
print(adding(4)) # saídas: 11
print(var) # NameError

##################################################################

# ex:5
# Você pode usar a palavra-chave global seguida por um nome de variável para tornar o escopo da variável global

var = 2
print(var) # saídas: 2
 
 
def return_var():
    global var
    var = 5
    return var
 
 
print(return_var()) # saídas: 5
print(var) # saídas: 5

##################################################################

a = 1                                                             # EXEMPLO IMPORTANTE
 
 
def fun():
    global a
    a = 2
    print(a)
 
 
a = 3
fun()
print(a)      # OUTPUT 2 2

##################################################################

a = 1                                                             # EXEMPLO IMPORTANTE
 
 
def fun():
    global a
    a = 2
    print(a)
 
 
fun()
a = 3
print(a)     # OUTPUT 2 3

##################################################################