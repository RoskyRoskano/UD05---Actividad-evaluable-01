# Creo una listado de listas con tamaño y peso
lista_elementos = [
    [180, 70],
    [160, 65],
    [175, 75],
    [180, 60],
    [160, 55],
]

# Defino la "key function" para ordenar la lista
# La "key function" toma un elemento de la lista y devuelve un valor utilizado para la comparación durante la clasificación.
# En este caso, la key function devuelve una tupla (altura, -peso) para ordenar por mayor altura y menor peso.
def key_func(elemento):
    altura, peso = elemento
    return (altura, -peso)

# Ordeno la lista utilizando la "key function"
lista_ordenada = sorted(lista_elementos, key=key_func)

# Muestro la lista original y la lista ordenada
print("Lista original:")
for elemento in lista_elementos:
    print(elemento)

print("\nLista ordenada por mayor altura y menor peso:")
for elemento in lista_ordenada:
    print(elemento)
