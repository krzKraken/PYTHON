# Crea una lista de Paises separados por comas, estos se deben almacenar en una lista. No deberia haber paises repetidos.Finalmente muestra por  consola la lista de los Países ordenadas alfabeticamente y separados por coma.
from getpass import getpass
listaPaises = []
print("::::::::::::::: INICIODE PROGRAMA ::::::::::::")
menu = 0
while (menu != 3):
    menu = int(input("""
    Menu: 
    1) Agregar pais
    2) Ordenar Lista
    3) Salir \n

    """))
    if menu == 1:
        pais = input("Escriba un Pais: ")
        listaPaises.append(pais.title())

    elif menu == 2:
        listaPaises = sorted(list(set(listaPaises)))
        print(list(listaPaises))
    elif menu == 3:
        print("Saliendo de programa")
