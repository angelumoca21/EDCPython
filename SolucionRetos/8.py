"""Ejercicio 1. (2 puntos) Escribe un programa Python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves."""

diccionario = {}

numero = int(input("Ingresa el numero generador:"))

for i in range(1,numero+1):
    diccionario[i]=i**2

print(diccionario)

"""Ejercicio 2. (2 puntos) Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena."""

diccionario = {}
palabra = input("Ingresa la palabra generadora:")
for caracter in palabra:
    if caracter not in diccionario:
        diccionario[caracter] = palabra.count(caracter)

print(diccionario)

"""Ejercicio 3. (2 puntos) Vamos a crear un programa en Python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta."""

diccionarioFrutas = {
    "Naranja":10,
    "Manzana":35,
    "Uva":20,
    "Platano":15,
    "Fresa":50
}

while True:
    fruta = input("Ingresa la fruta que quieres comprar:")
    if fruta in diccionarioFrutas:
        cantidad = float(input("Ingresa la cantidad:"))
        total = diccionarioFrutas[fruta] * cantidad
        print(f"El total por {cantidad} de {fruta} es {total}")
    else:
        print("Fruta no disponible")
    repetir = input("¿Quieres intentarlo de nuevo?[0 o 1]:")
    if repetir == "0":
        break