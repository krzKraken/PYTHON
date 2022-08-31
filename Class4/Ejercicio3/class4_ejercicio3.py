# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
print("Lista del 1 al 100")
lista = [1, 2, 3, 4, 5, 6]
print(lista)
lista.reverse()
print(lista)

lista100 = []
for i in range(1, 101):
    lista100.append(i)
print(lista100)

poss = 0
for i in range(len(lista100)):
    if (i == 0):
        lista100.append(lista100[lista100[0]])
print(lista100)
