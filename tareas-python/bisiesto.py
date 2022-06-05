def bisiesto():
    año: int = int(input("Verificador de años bisiestos. Escribe el año aqui: "))

    if(año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        print("El año es bisiesto")

    else:
        print("El año no es bisisesto")

print({bisiesto()})



