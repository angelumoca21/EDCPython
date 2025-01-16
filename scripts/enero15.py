#if simple

edad = int(input("Cuantos años tienes?"))

if edad>=18:
    print("Eres mayor de edad.")

#if-else

edad = int(input("Cuantos años tienes?"))

if edad>=18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")

#if-elif-else

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