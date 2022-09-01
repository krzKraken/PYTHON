# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

ano = int(input("Ingrese un año: "))


def esBiciesto(ano):
    div4 = ano % 4 == 0
    div100 = ano % 100 == 0
    div400 = ano % 400 == 0
    if (div4 and (not div100 or div400)):
        print(f"{ano} SI es un año Bisiesto!!!")
    else:
        print(f"{ano} NO es un año Bisiesto...")


esBiciesto(ano=ano)
