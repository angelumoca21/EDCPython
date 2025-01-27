'''Ejercicio 1. (1.5 puntos) Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.'''
while True:
    opcionUsuario = input("""
    Escoge una opción del menu:
    1.Opción 1
    2.Opción 2
    3.Opción 3
    4.Salir\n""")
    if opcionUsuario == "4":
        print("Adios")
        break

"""Ejercicio 2. (1.5 puntos) Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar."""

listaPrimos = []
numeroPrimos = int(input("Ingresa la cantidad de números primos a ver:"))
inicio = 2
while len(listaPrimos) < numeroPrimos:
    while True:
        divisores = 2
        for i in range(2,inicio):
            if inicio%i==0:
                divisores = divisores + 1
                inicio = inicio + 1
                break
        if divisores == 2:
            listaPrimos.append(inicio)
            inicio = inicio + 1
            break
print(listaPrimos)

"""Ejercicio 3. (1.5 puntos) Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses."""

total = 0
for i in range(1,21):
    pago = 10*(2**(i-1))
    print(f"Pago #{i}:{pago}")
    total = total + pago
print(f"El pago total es {pago}")

"""Ejercicio 4. (1.5 puntos) Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)."""

numero = int(input("Ingresa el numero al cual le quieres calcular el factorial:"))
total = 1
for i in range(1,numero+1):
    total = total * i

print(f"{numero}! = {total}")