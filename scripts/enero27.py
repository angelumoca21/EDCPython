#Sin parámetros sin retorno de datos
def saludar():
    print("Hola")

#Con parámetros sin retorno de datos
def saludarA(nombre,calificacion="NA"):
    print(f"Hola {nombre}, sacaste {calificacion}")

#Sin parámetros con retorno de datos
def suma():
    numero1 = float(input("Ingresa el primer numero:"))
    numero2 = float(input("Ingresa el segundo numero:"))
    return numero1+numero2

#Con parámetros y con retorno de datos
def resta(numero1,numero2):
    return numero1-numero2