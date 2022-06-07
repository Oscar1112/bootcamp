# Importamos el módulo time para poder coger la hora.
import time

hora = time.strftime("%H")
minutos = time.strftime("%M")

if int(hora) > 19:
    print("Estas en tiempo de descanso")
else:
    print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))