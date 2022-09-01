# Funcion es primo o no
cont = 0
miNumero = input("Ingrese un numero: ")

for i in range(1, int(miNumero)+1):
    if (int(miNumero) % i == 0):
        cont += 1

if cont == 2 or int(miNumero) == 1:
    print("Es primo")
else:
    print("No es Primo")
