from pickle import *

class Vehiculo:
    def __init__(self, ruedas, ventanas):
        self.ruedas = ruedas
        self.ventanas = ventanas

    def __str__(self):
        return (f"El carro cuenta con {self.ruedas} ruedas y {self.ventanas} ventanas")

mazda = Vehiculo(5, 4)
print(mazda)

datos = open("Vehiculo_objeto", "w+b")
dump(mazda, datos)
datos.seek(0)

unMazda = load(datos)
print(unMazda)

datos.close