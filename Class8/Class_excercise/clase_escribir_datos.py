# Escritura en ficheros
def main():
    f = open('Class8/Class_excercise/mi_fichero.txt', 'a')
    f.write('datos\n')
    f.write('Mas datos\n')
    lista = ["hola \n", "como \n", "Estas\n"]
    f.writelines(lista)

    f.close()


if __name__ == '__main__':
    main()
