from OCHO import Carro,Cliente,Concesionaria

carro1 = Carro("Toyota","Corolla",200_000)
carro2 = Carro("Honda","CRV",350_000) 
carro3 = Carro("Ford","Mustang",500_000) 

cliente1 = Cliente("Juan")

concesionaria1 = Concesionaria()

concesionaria1.agregarCarro(carro1)
concesionaria1.agregarCarro(carro2)
concesionaria1.agregarCarro(carro3)
concesionaria1.registrarCliente(cliente1)

concesionaria1.mostrarCarrosDisponibles()

cliente1.preguntarCarro(carro2)
cliente1.comprarCarro(carro2)
concesionaria1.mostrarCarrosDisponibles()
cliente1.comprarCarro(carro2)

#########################################################

from OCHO_3 import Carro,Moto,Camion,Cliente,Concesionaria

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