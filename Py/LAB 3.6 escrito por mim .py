my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escreva seu código aqui.
#
new_list = []
my_list.sort()

for i in my_list:
    if i not in new_list:
        new_list.append(i)

new_list.sort() 
print("A lista com os elementos exclusivos aqui")
print(new_list)

