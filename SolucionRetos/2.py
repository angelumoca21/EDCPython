"""Ejercicio 1. (1.5 puntos) Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:  ([°F] − 32) × 5 ⁄ 9."""

fahrenheit = float(input("Ingresa la cantidad de grados Fahrenheit a convertir:"))
celsius = (fahrenheit - 32)*(5/9)
print(f"{fahrenheit}º F = {celsius}º C")

"""Ejercicio 2. (1.5 puntos) Dados dos números, mostrar la suma, resta, división y multiplicación de ambos."""

numero1 = float(input("Ingresa el primer número:"))
numero2 = float(input("Ingresa el segundo número:"))
print(f"{numero1}+{numero2}={numero1+numero2}")
print(f"{numero1}-{numero2}={numero1-numero2}")
print(f"{numero1}/{numero2}={numero1/numero2}")
print(f"{numero1}*{numero2}={numero1*numero2}")

"""Ejercicio 3. (1.5 puntos) Calcular el perímetro y área de un rectángulo dada su base y su altura."""

base = float(input("Ingresa la base del rectángulo:"))
altura = float(input("Ingresa la altura del rectángulo:"))
area = base * altura
print(f"El rectángulo con base={base} y altura={altura} tiene un área de {area} cm^2")

"""Ejercicio 4. (1.5 puntos) Calcular la media de tres números pedidos por teclado."""

numero1 = float(input("Ingresa el primer número:"))
numero2 = float(input("Ingresa el segundo número:"))
numero3 = float(input("Ingresa el tercer número:"))
media = (numero1+numero2+numero3)/3
print(f"La media de los números: {numero1},{numero2} y {numero3} es {media}.")