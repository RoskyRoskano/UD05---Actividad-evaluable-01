# Clonar una lista
lista_original = [1, 2, 3, 4, 5]
lista_shallow_copy = lista_original.copy()  # Shallow copy
lista_deep_copy = lista_original.copy()  # Deep copy 

# Diferencia entre shallow copy y deep copy
# En una shallow copy, los elementos de la lista son referencias a los mismos objetos que en la lista original.
# En una deep copy, se crean nuevos objetos para los elementos, lo que garantiza independencia entre las listas.

# Agregar un elemento a una lista
nuevo_elemento = "hola"
lista_original.append(nuevo_elemento)

# Quitar un elemento de una lista
elemento_a_quitar = "hola"
lista_original.remove(elemento_a_quitar)

# Crear una lista nueva con los 4 últimos elementos de una lista
lista_cuatro_elementos = lista_original[-4:]

# Convertir las palabras de una cadena a una lista
cadena = "Hola cómo estás"
lista_palabras = cadena.split(" ")

# Los comentarios simples se hacen con una almohadilla
# Este es un comentario de una línea hecho con la almohadilla

# Los comentarios multilínea se hacen con triples comillas dobles 
"""
Así se hacen los comentarios multilínea con triples comillas dobles
"""
# Pero también se pueden hacer con triples comillas simples

'''
Así se hacen los comentarios multilínea con triples comillas simples
'''
