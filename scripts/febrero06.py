"""class Animal:
    def __init__(self,nombre,tipo):
        self.__nombre=nombre
        self._tipo=tipo

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nuevoNombre):
        self.__nombre = nuevoNombre

animal1 = Animal("Perro","terrestre")
print(animal1.getNombre())
print(animal1._tipo)
animal1.setNombre("Gato")
print(animal1.getNombre())"""

class Animal:
    def __init__(self,nombre,tipo):
        self.__nombre=nombre
        self.tipo=tipo

    #get
    @property
    def nombre(self):
        return self.__nombre
    #set
    @nombre.setter
    def nombre(self,nuevoNombre):
        if len(nuevoNombre)>2:
            self.__nombre = nuevoNombre
        else:
            print("No se realizo ningún cambio.")

animal1 = Animal("Tortuga","Acuatico")
print(animal1.nombre)
animal1.nombre = "Pulpo"
print(animal1.nombre)