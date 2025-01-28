import enero27
from random import randint, choice

def factorial(numero):
    resultado = 1
    if numero == 0:
        resultado = 1
        return resultado
    elif numero < 0:
        resultado = "Invalido"
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado

lista = ["Geo", "Guillermo", "Elda", "Alex", "Miguel", "Cristina","Angelica"]

resultado = factorial(4) #4*3*2*1
print(resultado)

numeroAleatorio = randint(1,10)
print(numeroAleatorio)

print(choice(lista))

enero27.saludar()

enero27.saludarA("Cristina",8)
enero27.saludarA("Alex")
enero27.saludarA("Geo",8)
enero27.saludarA("Guillermo",10)
enero27.saludarA("Elda",9)
enero27.saludarA("Angelica")

resultado = enero27.suma()
print(resultado)
print(enero27.resta(900,564))