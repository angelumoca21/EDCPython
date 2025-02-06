"""
Ejercicio 1. (2 puntos) Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad
"""

class Persona:
    def __init__(self,nombre = "",edad = 0,dni = ""):
        self.__nombre = nombre.title()
        self.__edad = edad
        self.__dni = dni.upper()

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevoNombre):
        self.__nombre = nuevoNombre.title()

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,nuevaEdad):
        if nuevaEdad < 0:
            print("Edad fuera del rango.")
            self.__edad = 0
        else:
            self.__edad = nuevaEdad
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,dniNuevo):
        self.__dni = dniNuevo.upper()

    def mostrarDatos(self):
        return f"Nombre:{self.nombre}, Edad:{self.edad}, DNI:{self.dni}"

    def esMayorDeEdad(self):
        return self.edad >= 18

persona1 = Persona("AnGEL MoraLEs",28,"MOCA961021")
print(persona1.mostrarDatos())
print(persona1.esMayorDeEdad())
persona1.nombre = "Uriel CARDOSO"
persona1.edad = 30
print(persona1.mostrarDatos())

"""
Ejercicio 2. (2 puntos) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""
"""
Ejercicio 3. (2 puntos) Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase Cuenta Joven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Construye los siguientes métodos para la clase:
Un constructor.
Los setters y getters para el nuevo atributo.
En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad; por lo tanto hay que crear un método es TitularVálido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
Además la retirada de dinero sólo se podrá hacer si el titular es válido.
El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir.
"""