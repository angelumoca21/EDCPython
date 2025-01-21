# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

"""palabra = input("Ingresa una palabra:")
for i in range(10):
    print(palabra)

# Escribe un programa que pida por teclado un numero y se muestre la tabla (1-10) de dicho numero.

numero = int(input("Ingresa un numero:"))
for i in range(1,11):
    print(f"{i}*{numero}={numero*i}")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

#Sol. 1
contraseña = "pilares"
password = input("Ingresa la contraseña:")

while password != "pilares":
    print("Contraseña erronea.")
    password = input("Ingresa la contraseña:")
    if password == "pilares":
        print("Bienvenido, inicio exitoso")

#Sol. 2
contraseña = "pilares"

while True:
    password = input("Ingresa la contraseña:")
    if password == contraseña:
        print("Bienvenido, inicio exitoso")
        break
    else:
        print("Contraseña errónea.")"""

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
# 5 -> primo, 6->no primo, 29->primo
numero = int(input("Ingresa un numero:"))
divisores = 2
for i in range(2,numero):
    if numero%i==0:
        divisores = divisores + 1
        break
if divisores == 2:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")