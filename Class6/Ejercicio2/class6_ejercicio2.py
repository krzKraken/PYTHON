class Alumno():
    nombre = ""
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def ImprimirNotas(self):
        print(f"{self.nombre} tiene {self.nota}")

    def EstaAprobado(self):
        if self.nota >= 7:
            print(f"{self.nombre} está Aprobado")
        else:
            print(f"{self.nombre} está Reprobado")


miAlumno = Alumno(nombre="Cristhian", nota=10)
miAlumno.ImprimirNotas()
miAlumno.EstaAprobado()
