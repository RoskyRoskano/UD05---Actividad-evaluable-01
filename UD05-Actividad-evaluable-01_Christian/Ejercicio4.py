"""
El operador is se utiliza para verificar si dos objetos son el mismo objeto en la memoria.
"""
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # False, porque son objetos diferentes
print(a is c)  # True, porque c apunta al mismo objeto que a

"""
El operador not se utiliza para negar una expresión booleana.
"""
x = True

print(not x)  # False, porque negamos True

"""
El operador in se utiliza para verificar la pertenencia de un elemento en una secuencia (como una lista, cadena, o conjunto).
"""
lista = [1, 2, 3, 4, 5]

print(3 in lista)  # True, porque 3 está en la lista
print(6 in lista)  # False, porque 6 no está en la lista
