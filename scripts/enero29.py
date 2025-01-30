print("Bienvenido")
#print(5/0) #zeroDivisionError
print("Adios")
#numero = int(input("Ingresa un numero")) #ValueError

#print("Hola"   

def print_exception(exceptionClass, indent=0):
    print(' '*indent+exceptionClass.__name__)
    for subclass in exceptionClass.__subclasses__():
        print_exception(subclass,indent+4)

print_exception(Exception)