#Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

nombre = input("Cual es tu nombre?")
print("Hola " + nombre)#concatenar
print(f"Hola {nombre}")

resultado=((3+2)/(2*5))**2
print(resultado)
print("Angel"*5)


# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

fahrenheit = float(input("Ingresa la cantidad de grados Fahrenheit a convertir:"))
celsius = (fahrenheit-32)/(1.8)
print(f"{fahrenheit}ºF = {celsius}ºC")