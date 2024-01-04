# Función para sumar dos números
def suma_numeros(a, b):
    return a + b

# Función para modificar una lista (referencia) doblando los valores de sus elementos
def modificar_lista(lista):
    for i in range(len(lista)):
        lista[i] *= 2

# Función para devolver una copia de la lista original (referencia) doblando los valores de sus elementos
def copia_y_dobla(lista):
    # Creamos una copia de la lista utilizando la función copy
    lista_copia = lista.copy() 
    
    for i in range(len(lista_copia)):
        lista_copia[i] *= 2
    
    return lista_copia

# Ejemplos
num1 = 3
num2 = 5
resultado_suma = suma_numeros(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado_suma}")

mi_lista = [1, 2, 3, 4]
modificar_lista(mi_lista)
print(f"Lista modificada (referencia): {mi_lista}")

mi_lista_original = [1, 2, 3, 4]
lista_doblada = copia_y_dobla(mi_lista_original)
print(f"Lista original: {mi_lista_original}")
print(f"Copia de la lista con valores doblados: {lista_doblada}")
