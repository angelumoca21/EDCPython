class Vehiculo:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca},{self.modelo} se vendió.")
        else:
            print(f"El vehículo {self.marca},{self.modelo} no está disponible.")
        
    def revisarDisponibilidad(self):
        return self.disponible
    
    def getPrecio(self):
        return self.precio
    
    def encender(self):
        pass

    def apagar(self):
        pass

class Carro(Vehiculo):
    def encender(self):
        print("El carro encendió.")

    def apagar(self):
        print("El carro se apagó.")

class Moto(Vehiculo):
    def encender(self):
        print("La moto encendió.")

    def apagar(self):
        print("La moto se apagó.")

class Camion(Vehiculo):
    def encender(self):
        print("El camión encendió.")

    def apagar(self):
        print("El camión se apagó.")

class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.vehiculosComprados = []
    
    def comprarVehiculo(self,vehiculo:Vehiculo):
        if vehiculo.revisarDisponibilidad():
            vehiculo.vender()
            self.vehiculosComprados.append(vehiculo)
        else:
            print(f"El vehiculo {vehiculo.marca},{vehiculo.modelo} no está disponible.")

    def preguntarVehiculo(self,vehiculo:Vehiculo):
        if vehiculo.revisarDisponibilidad():
            disponibilidad = "disponible"
        else:
            disponibilidad = "no disponible"
        print(f"El vehiculo {vehiculo.marca},{vehiculo.modelo} esta {disponibilidad} y cuesta ${vehiculo.getPrecio()}")

class Concesionaria:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def agregarVehiculo(self,vehiculo:Vehiculo):
        self.inventario.append(vehiculo)
        print(f"El vehiculo {vehiculo.marca},{vehiculo.modelo} ha sido añadido al inventario.")

    def registrarCliente(self,cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} ha sido registrado.")

    def mostrarVehiculosDisponibles(self):
        print("Los vehiculos disponibles son:")
        for vehiculo in self.inventario:
            if vehiculo.revisarDisponibilidad():
                print(f"-{vehiculo.marca},{vehiculo.modelo} por {vehiculo.getPrecio()}")


carro1 = Carro("Toyota","Corolla",200_000)
moto1 = Moto("Yamaha","100H",150_000)
camion1 = Camion("Volvo","XR3",800_000)

cliente1 = Cliente("Juan")

concesionaria1 = Concesionaria()

concesionaria1.agregarVehiculo(carro1)
concesionaria1.agregarVehiculo(moto1)
concesionaria1.agregarVehiculo(camion1)
concesionaria1.registrarCliente(cliente1)

concesionaria1.mostrarVehiculosDisponibles()

cliente1.preguntarVehiculo(camion1)
cliente1.comprarVehiculo(camion1)

concesionaria1.mostrarVehiculosDisponibles()

cliente1.preguntarVehiculo(camion1)