from turtle import color


class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color,
        self.ruedas = ruedas
        self.puertas = puertas
    def __str__(self):
        return "el color es {}, {} ruedas, y tiene {}puertas".format( self.color, self.ruedas, self.puertas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
       return " el color {}, La velocidad maxima es de {} km/h, {} ruedas, cuenta con {} puertas, {} cc".format( self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )
nuevoCoche = Coche("purpura", "4", 6, 200, 800)
print(nuevoCoche)
