##################################################################

# conversores

# IMC

def bmi(weight, height):
    return weight / height ** 2
 
 
print(bmi(52.5, 1.65))

##################################################################

# IMC com medidas imperiais

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
        weight < 20 or weight > 200:
        return None

        return weight / height ** 2


print(bmi(352.5, 1.65))

##############################################################

# Kilo por Libra

def lb_to_kg(lb):
    return lb * 0.45359237
 
 
print(lb_to_kg(1))
 
##############################################################

# pés e Polegada por metros

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
 
 
print(ft_and_inch_to_m(1, 1))

##############################################################

# apenas pés sem as polegadas

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
print(ft_and_inch_to_m(6))

##############################################################

#A função terá três parâmetros - um para cada lado.

#Ele retornará True se os lados puderem construir um triângulo, e False caso contrário

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
        return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

##############################################################

#

def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
 
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

##############################################################

# Compactados

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

##############################################################

# Pitagoras

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Digite o primeiro lado\'s comprimento: '))
b = float(input('Entre no segundo lado\'s comprimento: '))
c = float(input('Entre no terceiro lado\'s comprimento: '))

if is_a_triangle(a, b, c):
    print('Sim, pode ser um triângulo.')
else:
    print('Não, não pode ser um triângulo.')

###############################################################

# Descobrir a hipotenusa

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 #if a > b and a > c :
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

###############################################################

# Avaliando a área de um triangulo com a raiz quadrada

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
 
 
print(area_of_triangle(1., 1., 2. ** .5))

##############################################################

# função Fatorial

#0! = 1 (sim! É verdade)
#1! = 1
#2! = 1 * 2
#3! = 1 * 2 * 3
#4! = 1 * 2 * 3 * 4
#:
#:
#n! = 1 * 2 * 3 * 4 * ... * n-1 * n

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6): # testando
    print(n, factorial_function(n))

##############################################################


# Números de Fibonacci

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10): # testando
    print(n, "->", fib(n))

##############################################################

# Recursiva

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
 
##############################################################

# fatorial ex classico de recursão:

# Implementação recursiva da função fatorial.
 
def factorial(n):
    if n == 1: # O caso base (condição de rescisão).
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24