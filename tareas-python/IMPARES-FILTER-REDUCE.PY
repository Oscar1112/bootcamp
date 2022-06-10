from functools import reduce
numeros = list(range(50))
def proyecto(lista): 
    resultado = list(filter((lambda x: x % 2), numeros)) 
    print(resultado)

    
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(resultado)
proyecto(numeros)