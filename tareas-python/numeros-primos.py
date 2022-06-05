

##------------------------------------

def Primo():
    numero: int = int(input("Introduzca cualquier numero entero: "))

    if numero > 1:
     for i in range(2,int(numero)):
        if(int(numero) % i) == 0:
            print(f"El numero {numero} no es primo")

            break
        else:
                print(f"El numero {numero} si es primo")

print({Primo()})
