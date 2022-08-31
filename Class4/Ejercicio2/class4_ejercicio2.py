# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

valInicial = input("Valor inicial: ")
valFinal = input("valor Final: ")
listaResultados = []
for i in range(int(valInicial), int(valFinal)):
    if (i % 2 != 0):
        listaResultados.append(i)
print(listaResultados)
