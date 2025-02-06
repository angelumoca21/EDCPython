from febrero05 import Auto, Cliente, Concesionaria

auto1 = Auto("Audi","Z3",300_000)
auto2 = Auto("Ford","Fiesta",150_000)
cliente1 = Cliente("Alex Moya","1234")

concesionaria1 = Concesionaria("Pensil")
concesionaria1.agregarAuto(auto1)
concesionaria1.agregarAuto(auto2)
concesionaria1.agregarCliente(cliente1)

cliente1.preguntarAuto(concesionaria1)
cliente1.comprarAuto(auto2)
cliente1.preguntarAuto(concesionaria1)
