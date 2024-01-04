import sys

"""
Pasar varios parametros por consola
"""
# Cojo los argumentos de la línea de comandos
argumentos = sys.argv[1:]

# Muestro los argumentos
print("Argumentos desde la consola:", argumentos)

"""
Sobrecarga de funciones
"""
def suma(*args):
    total = 0
    for num in args:
        total += num
    return total

# Ejemplos
resultado1 = suma(1, 2, 3)
resultado2 = suma(4, 5, 6, 7, 8)

# Muestro los resultados
print("Resultado 1:", resultado1)
print("Resultado 2:", resultado2)
