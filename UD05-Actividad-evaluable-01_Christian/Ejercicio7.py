import random

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def mostrar(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")

    # Creo dos métrodos mas que muestran los atributos por separado
    def mostrar_color(self):
        print(f"Color: {self.color}")
    
    def mostrar_matricula(self):
        print(f"Matrícula: {self.matricula}")

# Pido al usuario el número "n"
n = int(input("Dame el número de instancias a crear: "))

# Valido que "n" sea al menos 1
if n < 1:
    print("Dame un número")
else:
    # Creo "n" instancias de la clase Car
    lista_coches = []
    for i in range(1, n + 1):
        matricula = i
        color = random.choice(["red", "white", "black", "pink", "blue"])
        coche = Car(matricula, color)
        lista_coches.append(coche)

    # Imprimo los valores de las 10 primeras instancias (o las "n" instancias si son menos de 10)
    for coche in lista_coches[:10]:
        coche.mostrar()
        coche.mostrar_matricula()
        coche.mostrar_color()
        
