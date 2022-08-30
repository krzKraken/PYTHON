nombre = "Alfonsino"
apellido = "Prieto Menendez"
edad = 40
email = "alfonsino.prieto@hotmail.com"
telefono = "+593123456987"
casado = True
hijos = True
amigos = ["Carlos", "Pedro", "Maria", "Carmen"]
peliculas = {
    "terror": "Chuckie",
    "comedia": "Donde estan las rubias?",
    "suspenso": "Anaconda"
}

print("Nombre: " + nombre + "\nApellido: " + apellido + "\nEdad: "+str(edad) + "\nE-mail: " + email + "\nTelefono: " + telefono +
      "\nCasado" + str(casado) + "\nHijos: " + str(hijos) + "\nAmigos: " + ' '.join(amigos) + "\nPeliculas:  " + peliculas["terror"] + " ," + peliculas["comedia"] + " ,"+peliculas["suspenso"])
