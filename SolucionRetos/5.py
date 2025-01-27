"""Ejercicio 1. (2 puntos) Programa que imprima si el número es positivo o negativo."""

numero = float(input("Ingresa un numero:"))
if numero < 0:
    print(f"El numero: {numero} es negativo.")
else:
    print(f"El numero: {numero} es positivo.")

"""Ejercicio 2. (2 puntos) Programa que imprima si el número ingresado esta en el rango de 1 a 7."""

numero = int(input("Ingresa un numero:"))
if numero >= 1 and numero <= 7:
    print(f"El numero: {numero} esta en el rango de 1 a 7.")
else:
    print(f"El numero: {numero} no esta en el rango de 1 a 7.")

"""Ejercicio 3. (2 puntos) Programa que calcule el interés de una cantidad si es mayor al 30%, sino informa el importe total."""

monto = float(input("Ingresa el monto:"))
porcentaje = float(input("Ingresa el porcentaje de interés:"))

if porcentaje < 30:
    print(f"El monto es: {monto}")
else:
    montoConInteres = monto + monto*(porcentaje/100)
    print(f"El monto con interés es:{montoConInteres}")