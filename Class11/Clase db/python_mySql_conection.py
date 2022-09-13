# Install pysqlite3
# pip install sqlite3

from getpass import getpass
import sqlite3


def main():
    username = input("Ingrese el nombre: ")
    password = getpass("Ingrese contrasena: ")
    if verificar_contrasena(username=username, password=password):
        print("Login Correcto")
    else:
        crear_usuario(identificator=5, username=username, password=password)


def verificar_contrasena(username, password):
    conn = sqlite3.connect('myapplication.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' and password='{password}'"
    # query = f"SELECT id FROM users WHERE username='Cristhian' and password='contrasena1k'"
    print(f'query enviada: {query}')
    rows = cursor.execute(query)
    data = rows.fetchone()

    print(data)
    cursor.close()
    conn.close()

    if data == None:
        return False
    return True


def crear_usuario(identificator, username, password):
    conn = sqlite3.connect('myapplication.db', isolation_level=None)
    cursor = conn.cursor()

    query = '''INSERT INTO users(id, username, password) VALUES(?,?,?)'''
    # query = f"SELECT id FROM users WHERE username='Cristhian' and password='contrasena1k'"
    print(f'query enviada: {query}')
    rows = cursor.execute(query, (identificator, username, password))
    data = rows.fetchone()
    # conn.commit()  #--> Es el commit a que modifique la base de datos
    cursor.close()
    conn.close()


# Comunicacion con la base de datos
# conn = sqlite3.connect('myapplication.db')

# cursor = conn.cursor()
# rows = cursor.execute('SELECT * FROM users WHERE username="Cristhian"')
# for row in rows:
#     print(row)

# cursor.close()
# conn.close()

if __name__ == '__main__':
    main()