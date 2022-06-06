from contextlib import redirect_stderr


class Vehiculo:
    color = "red",
    ruedas = 4,
    puertas = 5

class Coche(Vehiculo):
    Velocidad = 200
    cilindrada = 8

C = Coche()
print(C)
