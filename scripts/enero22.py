lista = [4,5,1,2,5,10,5,7,8,9,2,9,6,6,10]
aprobados = 0

for elemento in lista:
    if elemento >= 6:
        aprobados = aprobados + 1

print(f"La cantidad de alumnos aprobados es {aprobados}")