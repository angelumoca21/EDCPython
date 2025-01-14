print("Hola a todos en","PILARES Pensil")

print("Hola a todos en","PILARES Pensil",sep="           ")

print("Hola a todos en", end="*")
print("PILARES Pensil", end="*")

print('Hola a todos en PILARES Pensil')

print("I'm")
print('I\'m')

print('"Hola"')
print("\"Hola\"")

print("\\")


edad = 28 #Entero
precio = 9.99 #Flotante
nombre = "Angel" #String o cadena de texto
estado_envio = True #Booleano


print(edad)
print(type(edad))
print(precio)
print(type(precio))
print(nombre)
print(type(nombre))
print(estado_envio)
print(type(estado_envio))

nombre = input("Cual es tu nombre?")
print("Bienvenido " + nombre)

edad = int(input("Cual es tu edad?"))
print(type(edad))
edad = edad + 30
print("Tu edad en 30 años sera de " + str(edad) + " años.")
print(f"Tu edad en 30 años sera de {edad} años.") #fstrings