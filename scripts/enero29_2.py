try:
    numero = float(input("Ingrese el divisor:"))
    resultado = 90/numero
    print(resultado)
    assert numero != 1, "Uno es igual que uno"
except ZeroDivisionError:
    print("No es valido ingresar cero.")

except ValueError:
    print("No es valido ingresar letras.")

except AssertionError:
    print("Error personalizado")
else:
    print("El usuario no rompió mi código.")
finally : 
    print("Final")