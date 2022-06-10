pedirPaises = input("Escriba una lista de paises")
#.split se utiliza para trabajar una lista de elementos y separarlos en este caso por comas
guardar = [Paises for Paises in pedirPaises.split(",")]

print(",".join(sorted(list(set(guardar)))))