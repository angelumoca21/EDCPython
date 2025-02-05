"""Ejercicio 1. (1.5 puntos) Realice un programa que pregunte aleatoriamente una multiplicación. El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta). El programa preguntará 10 multiplicaciones, y al finalizar mostrará el número de aciertos."""
import random

numeroPregunta = 0
aciertos = 0
while numeroPregunta < 10:
    numero1 = random.randint(1,10)
    numero2 = random.randint(1,10)
    respuesta = int(input(f"Cuanto es {numero1}*{numero2}?"))
    if respuesta == numero1*numero2:
        aciertos = aciertos + 1
    numeroPregunta = numeroPregunta + 1 
print(f"Fin de las preguntas, tuviste {aciertos} aciertos.")


"""Ejercicio 2. (1.5 puntos) Obtener el cuadrado de todos los elementos en la lista. Lista: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = list(map(lambda x:x**2,lista))
print(lista2)

"""Ejercicio 3. (1.5 puntos) Obtener la cantidad de elementos mayores a 5 en la tupla. tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)"""

tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)
lista3 = list(filter(lambda x:x>5 ,tupla))
print(lista3)

"""Ejercicio 4. (1.5 puntos) Obtener la suma de todos los elementos en la lista."""
from functools import reduce
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = reduce(lambda x,y:x+y,lista4)
print(resultado)