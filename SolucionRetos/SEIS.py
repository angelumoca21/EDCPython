#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre = input("Ingresa tu nombre:")

print(nombre.lower())
print(nombre.upper())
print(nombre.title())

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

nombre = input("Ingresa tu nombre:")
nombreSinEspacios = nombre.replace(" ","")
numeroCaracteres = len(nombreSinEspacios)
print(f"{nombre} tiene {numeroCaracteres} letras")

#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

palabra = input("Ingresa una palabra:")
print(palabra[::-1])

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignaturas = ("Mate","Fisica","Quimica","Historia","Progra")
notas = []

for asignatura in asignaturas:
    notas.append(float(input(f"Ingresa la nota de {asignatura}:")))

#Sol.1
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")

#Sol.2
for asignatura, nota in zip(asignaturas,notas):
    print(f"En {asignatura} has sacado {nota}")

#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

diccionario = {}

palabras = input("Ingresa el par de la siguiente forma: [español:ingles] y separados por coma:")

for par in palabras.split(","):
     clave, valor = par.split(":")
     diccionario[clave]=valor

frase = input("Ingresa la frase a traducir:")

for palabra in frase.split(" "):
    if palabra in diccionario:
        print(diccionario[palabra], end=" ")
    else:
        print(palabra, end=" ")