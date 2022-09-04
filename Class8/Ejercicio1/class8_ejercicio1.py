# Crear un Fichero y escribir en el


def main():
    crearFichero()
    escribirFicher()


def crearFichero():
    f = open('fichero.txt', 'w')
    f.close()


def escribirFicher():
    texto = input("Escriba en el fichero: ")
    f = open("fichero.txt", 'a')
    f.write(texto)
    f.close()


if __name__ == '__main__':
    main()
