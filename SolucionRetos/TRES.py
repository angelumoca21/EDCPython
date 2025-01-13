# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética: $(\frac{3+2}{2*5})^2$ 

print(((3+2)/(2*5))**2)

# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente. 

n = int(input("Ingresa el valor de n:"))
m = int(input("Ingresa el valor de m:"))
c = n // m
r = n % m
print(f"{n} entre {m} da un cociente {c} y un resto {r}.")