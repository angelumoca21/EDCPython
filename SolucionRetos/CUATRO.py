"""
1.Color de alien: Imagina un videojuego donde de manera aleatoria van apareciendo aliens en la pantalla de diferentes colores (verdes, amarillos y rojos), pide por teclado al usuario que ingrese el color de alien, si el color escogido es verde el usuario ganara 5 puntos y es diferente a verde no habrá salida de datos.

2. Modifica el código realizado para se muestre lo siguiente:
Si el color ingresado es verde el usuario gane 5 puntos.
Si el color es diferente a verde el usuario gana 10 puntos.

3.Modifica el código para que:
Si el color ingresado es verde el usuario gane 5 puntos.
Si el color ingresado es amarillo el usuario gana 10 puntos.
Si el color ingresado es rojo el usuario gana 15 puntos.
"""

color = input("Ingresa el color de tu alien:")
if color == "verde":
    print("Ganaste 5 puntos")
elif color == "amarillo":
    print("Ganaste 10 puntos")
elif color == "rojo":
    print("Ganaste 15 puntos")
"""
Etapas de la vida
Escribe un código para determinar la etapa de vida de una persona, a partir de la edad ingresada por teclado:
Si la edad es menor a 2 años, imprime: "Es un bebé".
Si la edad es mínimo 2 y menor a 4, imprime: "Es un niño pequeño".
Si la edad está entre 4 y menos de 13, imprime: "Es un niño".
Si la edad es mínimo 13 y menor a 20, imprime: "Es un adolescente".
Si la edad va desde 20 y es menor a 65, imprime: "Es un adulto".
Si la edad es mayor o igual 65, imprime: "Es un adulto mayor".
"""

edad = int(input("Cuantos años tienes?"))

if edad<2 and edad>0:
    print("Bebé")
elif edad<4 and edad>=2:
    print("Niño pequeño.")
elif edad<13 and edad>=4:
    print("Niño.")
elif edad<=19 and edad>12:
    print("Adolescente")
elif edad<=64 and edad>19:
    print("Adulto")
elif edad>=65:
    print("Adulto mayor")
else:
    print("Edad invalida")