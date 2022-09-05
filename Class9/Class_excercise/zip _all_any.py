# Zip agrega iterables en una tupla y los devuelve
# Combina item a imtems una lista de tuplas
cursos = ["java", "Python", "git"]
asistentes = [12, 4, 51]

demo = zip(cursos,  asistentes)
print(list(demo))

# [('java', 12), ('Python', 4), ('git', 51)]

#All and Any
# Sirven para verificar que todas las condiones en una lista se cumplan o que al menos una de las condiciones de lista se cumplan
listaA = [1 == 1, 2 == 2, 3 == 4]
res = any(listaA)
print(res)
res = all(listaA)
print(res)
