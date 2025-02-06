#Realiza un programa que simule una concesionaria de autos donde además de poder gestionar los autos y clientes, los clientes pueden comprar autos.

class Auto:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponibleComprar = True
        print(f"El auto {self.marca},{self.modelo} que tiene un precio de ${precio} se ha creado.")

    def vender(self):
        self.disponibleComprar = False
        print(f"El auto {self.marca},{self.modelo} se vendió.")

class Cliente:
    def __init__(self,nombre,telefono):
        self.nombre = nombre
        self.telefono = telefono
        print(f"El cliente {self.nombre} se ha creado.")
    
    def comprarAuto(self,auto):
        if auto.disponibleComprar:
            auto.vender()

    def preguntarAuto(self,concesionaria):
        print("Los autos disponibles son:")
        for auto in concesionaria.inventario:
            if auto.disponibleComprar:
                print(f"-{auto.marca},{auto.modelo} ${auto.precio}")

class Concesionaria:
    def __init__(self,nombre):
        self.nombre = nombre
        self.inventario = []
        self.clientes = []
        print(f"La concesionaria {self.nombre} se ha creado.")

    def agregarAuto(self,auto):
        self.inventario.append(auto) 
        print(f"El auto {auto.marca},{auto.modelo} se agrego al inventario.")

    def agregarCliente(self,cliente):
        self.clientes.append(cliente) 
        print(f"El cliente {cliente.nombre}, se agrego al directorio.")     

           