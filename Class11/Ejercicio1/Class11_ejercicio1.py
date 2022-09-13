# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
3

import sqlite3
import sys


def createUser(id, nombre, apellido):
    try:
        conn = sqlite3.connect('alumnos.db', isolation_level=None)
        cursor = conn.cursor()

        query = '''INSERT INTO alumnos(id, nombre, apellido) VALUES(?,?,?);'''
        rows = cursor.execute(query, (id, nombre, apellido))
        print(" \n [+] Alumno registrado... \n")
        cursor.close()
        conn.close()
    except:
        print("\n [-] Error registrando usuario, vuelva a intentarlo \n")
        return


def searchUser(nombre, apellido):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    query = f'SELECT * FROM alumnos WHERE nombre="{nombre}" and apellido="{apellido}";'
    rows = cursor.execute(query)
    data = rows.fetchone()
    cursor.close()
    conn.close()
    if data == None:
        print(f'No se encontraron coincidencias con {nombre} {apellido}')
    else:
        print(f'\n[+] Coincidencia Encontrada: {data} \n')


def main():
    menu_val = 0
    while (menu_val != 3):
        menu_val = int(
            input(''' 
        Menu:
        1.- Para crear Alumno
        2.- Realizar Consulta
        3.- Salir
         '''))
        if menu_val == 1:
            identificator = int(input("Ingrese id para alumno: "))
            nombre = input("Ingrese el Nombre: ")
            apellido = input("Ingrese el Apellido: ")
            createUser(id=identificator, nombre=nombre, apellido=apellido)
        elif menu_val == 2:
            nombre = input('Ingrese nombre: ')
            apellido = input('Ingrese apellido: ')
            searchUser(nombre=nombre, apellido=apellido)
        elif menu_val == 3:
            sys.exit(1)


if __name__ == '__main__':
    main()