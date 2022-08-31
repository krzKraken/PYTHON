# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
lista100 = []
for i in range(1, 101):
    lista100.append(i)
print("Lista creada --> " + str(lista100) + "\n")
# Con Metodo
listaInversa = sorted(lista100, reverse=True)
print("Lista invertida con metodo --> " + str(listaInversa) + "\n")

# Sin Metodos
listaInversa2 = []
i = len(lista100)
while i > 0:
    listaInversa2.append(i)
    i -= 1
print("Lista creada:" + str(listaInversa2) + "\n")
