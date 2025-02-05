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