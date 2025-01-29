#Solución1####################
numbers = [1, 2, 3, 4, 5]
cuadrados = []

for number in numbers:
    cuadrado = number**2
    cuadrados.append(cuadrado)
print(cuadrados)
####################

def square(x):
    return x ** 2

squared = list(map(square, numbers))

print(squared)
####################
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
evens = list(filter(is_even, numbers))
print(evens)
####################
from functools import reduce

def times(x,y):
    return x * y

total = reduce(times, numbers)

print(total)
print(sum(numbers))

#######################
#definición
square = lambda x: x ** 2

#llamado
result = square(4)
result = square(20)
print(result)