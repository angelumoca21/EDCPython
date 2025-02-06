#Clase padre
class vehiculo:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponibleComprar = True
        print(f"El vehículo {self.marca},{self.modelo} que tiene un precio de ${precio} se ha creado.")

    def vender(self):
        self.disponibleComprar = False
        print(f"El vehículo {self.marca},{self.modelo} se vendió.")

    def encender(self):
        pass

    def apagar(self):
        pass

#Clase hijo
class Auto(vehiculo):
    def encender(self):
        print("El auto se encendió.")

    def apagar(self):
        print("El auto se apago.")

#Clase hijo
class Moto(vehiculo):
    def encender(self):
        print("El moto se encendió.")

    def apagar(self):
        print("El moto se apago.")

#Clase hijo
class Camion(vehiculo):
    def encender(self):
        print("El camion se encendió.")

    def apagar(self):
        print("El camion se apago.")