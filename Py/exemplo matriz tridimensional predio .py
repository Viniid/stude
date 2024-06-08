# O Python não limita a profundidade da inclusão na lista. Aqui você pode ver um exemplo de uma matriz tridimensional:

rooms = [[[() for r in range(20)] for f in range(15)] for t in range(3)]

# Agora você pode reservar um quarto para dois noivos: no segundo edifício, no décimo andar, quarto 14:
rooms [1][9][13] = True

#e liberar a segunda sala no quinto andar, localizada no primeiro edifício:
rooms [0][4][1] = False

#Verifique se há vagas no 15º andar do terceiro edifício:
vacancy = 0
 
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
 
print(vacancy)
print(rooms)