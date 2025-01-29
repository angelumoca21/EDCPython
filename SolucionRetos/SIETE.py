#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calculoIva(cantidad,iva=21):
    return (cantidad*(iva/100) + cantidad)

print(calculoIva(3000,16))
print(calculoIva(3000))
print(calculoIva(3000,21))

# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
#a=pi*r*r
#v=a*h

# Funcion de orden mayor
def areaCirculo(radio):
    pi = 3.1416
    return pi*(radio**2)

def volumenCilindro(area,altura):
    return area*altura

print(volumenCilindro(areaCirculo(8),5))