class Carro:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El carro {self.marca},{self.modelo} se vendió.")
        else:
            print(f"El carro {self.marca},{self.modelo} no está disponible.")
        
    def revisarDisponibilidad(self):
        return self.disponible
    
    def getPrecio(self):
        return self.precio
    
class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.carrosComprados = []
    
    def comprarCarro(self,carro):
        if carro.revisarDisponibilidad():
            carro.vender()
            self.carrosComprados.append(carro)
        else:
            print(f"El carro {carro.marca},{carro.modelo} no está disponible.")

    def preguntarCarro(self,carro):
        if carro.revisarDisponibilidad():
            disponibilidad = "disponible"
        else:
            disponibilidad = "no disponible"
        print(f"El coche {carro.marca},{carro.modelo} esta {disponibilidad} y cuesta ${carro.getPrecio()}")

class Concesionaria:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def agregarCarro(self,carro):
        self.inventario.append(carro)
        print(f"El coche {carro.marca},{carro.modelo} ha sido añadido al inventario.")

    def registrarCliente(self,cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} ha sido registrado.")

    def mostrarCarrosDisponibles(self):
        print("Los carros disponibles son:")
        for carro in self.inventario:
            if carro.revisarDisponibilidad():
                print(f"-{carro.marca},{carro.modelo} por {carro.getPrecio()}")