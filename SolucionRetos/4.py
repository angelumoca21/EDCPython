"""Ejercicio 1. (1.2 puntos) Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo."""

import random

listaAleatoria = []

for i in range(10):
    valorAleatorio = random.randint(1,10)
    listaAleatoria.append(valorAleatorio)

for valor in listaAleatoria:
    print(f"{valor},{valor**2},{valor**3}")

"""Ejercicio 2. (1.2 puntos) Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla."""

lista = []
listaInversa = []

for i in range(5):
    palabra = input("Ingresa una cadena de caracteres:")
    lista.append(palabra)

for i in range(4,-1,-1):
    listaInversa.append(lista[i])

print(lista)
print(listaInversa)

"""Ejercicio 3. (1.2 puntos) Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor."""

notas = []

while len(notas) < 5:
    nota = float(input("Ingresa una nota:"))
    if nota >= 1 and nota <= 10:
        notas.append(nota)
    else:
        print("Nota fuera de rango.")

media = sum(notas)/len(notas)
alta = max(notas)
baja = min(notas)

print(f"Las notas fueron: {notas}, la nota media es: {media}, la nota más alta es: {alta} y la más baja es: {baja}")

"""Ejercicio 4. (1.2 puntos) Codifica un programa en Python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listados con las notas de cada alumno.
El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error."""

diccionario = {}
listaNombres = []
listaNotas = []
notasPorAlumno = []
nota = 0
numeroAlumnos = int(input("Ingresa la cantidad de alumnos a registrar sus notas:"))

while len(listaNombres)<numeroAlumnos:
    nombre = input("Ingresa el nombre del alumno:")
    if nombre in listaNombres:
        print("Nombre repetido")
    else:
        listaNombres.append(nombre)

for nombre in listaNombres:
    while True:
        nota = int(input(f"Ingresa la nota de {nombre}:"))
        if nota < 0:
            break
        else:
            notasPorAlumno.append(nota)
    listaNotas.append(notasPorAlumno.copy())
    notasPorAlumno.clear()

for nombre,nota in zip(listaNombres,listaNotas):
    diccionario[nombre] = nota

for nombre,calificaciones in zip(diccionario.keys(),diccionario.values()):
    print(f"{nombre}:{calificaciones}:{(sum(calificaciones))/len(calificaciones)}")

"""Ejercicio 5. (1.2 puntos) Crea una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero."""

meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")

numero = int(input("Ingresa el numero de mes al que quieres acceder:"))
print(meses[numero-1])