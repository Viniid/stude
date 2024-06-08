##########################################################################

# Ex: 1

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 
words = ['gato', 'lion', 'cavalo'] 

for word in words: 
    if word in dictionary: 
        print(word, "->", dictionary[word]) 
    else: 
        print(word, "não está no dicionário")

##########################################################################

# Ex:2  recuo suspenso, dicionario muito extenso

# Exemplo 1:
dictionary = {
              "gato": "chat",
              "cachorro": "chien",
              "cavalo": "cheval"
}
# Exemplo 2:
phone_numbers = {'chefe': 5551234567,
              'Suzy': 22657854310
}

##########################################################################

# Ex: 3 Função                  Keys()

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 

for key in dictionary.keys(): 
    print(key, "->", dictionary[key])

##########################################################################

# Ex: 4  Função                 items()

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 

for english, french in dictionary.items(): 
    print(english, "->", french)

##########################################################################

# Ex: 5 substituir um valor 

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 

dictionary['gato'] = 'minou' # é só especificar qual é o dicionario e a chave que deseja substituir o value

print(dictionary)

##########################################################################

# Ex: 6 Função                   Sorted()

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 

for key in sorted(dictionary.keys()):
    print(dictionary[key])

##########################################################################

# Ex: 7                          values()

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 
for french in dictionary.values():  # similar a keys(), retorna os valores em vez da chave
    print(french)

##########################################################################

# Ex: 8  Adicionando uma chave e um valor novo

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 

dictionary['swan'] = 'cygne' # [key] = 'Value'

print(dictionary)

##########################################################################

# Ex: 9 Função                      update()

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 

dictionary.update({"pato": "canard"})  # mais legivel

print(dictionary)

##########################################################################

# Ex: 10  Função                     Del

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 

del dictionary['cachorro'] # similar a outras funções 

print(dictionary) 

##########################################################################

# Ex : 11 Função                     popitem()

# Remove o ultimo item de um dicionario

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} 

dictionary.popitem() 

print(dictionary) # saídas: {'gato': 'chat', 'cachorro': 'chien'}

##########################################################################

#Tuplas e dicionários

school_class = {}

var = 0

while var < 2:
    var += 1

    name = input("Digite o nome do aluno: ")

    if name == '':
        break
        score = int(input("Insira a pontuação do aluno (0-10): "))
    if score not in range(0, 11):
        break
 
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
 
    for name in sorted(school_class.keys()):
        adding = 0
        counter = 0
        for score in school_class[name]:
            adding += score
            counter += 1
            print(name, ":", adding / counter)
  
##########################################################################

# Ex: 12    Função                        tuple()
 
my_tuple = tuple((1, 2, "corda"))
print(my_tuple)
 
my_list = [2, 4, 6]
print(my_list)    # saídas: [2, 4, 6]
print(type(my_list))    # saídas: 
tup = tuple(my_list)
print(tup)    # saídas: (2, 4, 6)
print(type(tup))    # saídas: 
 
###########################################################################

# eX: 13 Função                             list()

tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list))    # saídas: 
 
############################################################################

# 1Ex: 14 Função                            get()

pol_eng_dictionary = {
    "kwiat": "flor",
    "woda": "água",
    "gleba": "solo"
    }
 
item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # saídas: solo
 
item_2 = pol_eng_dictionary.get("woda")    # ex. 2
print(item_2)    # saídas: água
 
############################################################################

#Ex: 15 Função                               clear()

pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
print(len(pol_eng_dictionary))    # saídas: 3

del pol_eng_dictionary["zamek"]    # remover um item

print(len(pol_eng_dictionary))    # saídas: 2
 
pol_eng_dictionary.clear()   # remove todos os itens

print(len(pol_eng_dictionary))    # saídas: 0
 
del pol_eng_dictionary    # remove o dicionário

############################################################################

# Ex: 16 Função                              copy()

pol_eng_dictionary = { "zamek": "castelo", "woda": "água", "gleba": "solo" } 

copy_dictionary = pol_eng_dictionary.copy()

 
