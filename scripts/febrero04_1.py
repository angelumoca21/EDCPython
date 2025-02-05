class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años.")
    
    def correr(self,distancia):
        self.distancia = distancia
        print(f"Estoy corriendo {self.distancia} m.")

    def saludar(self,saludarA):
        print(f"Hola, {saludarA}")

    def cumplirAnios(self):
        self.edad = self.edad+1
        print(f"Ya tienes {self.edad} años.")