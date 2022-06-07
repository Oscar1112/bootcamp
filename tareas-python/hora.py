
import time

hora = time.strftime("%H")
minutos = time.strftime("%M")


if int(hora) > 19:
    print("No estas en el horario de trabajo")
else:
    print ("Tiempo restante  {} horas y {} minutos para llegar al tiempo de descanso".format(18- int(hora), 59-int(minutos)))
