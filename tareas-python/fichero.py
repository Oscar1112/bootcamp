#crear un archivo
archivo = open("texto.txt", "w")
archivo.write("Primer elemento \n")
archivo.close
archivo = open("texto.txt", "r+")
archivo.readline()
archivo.write("Esta es una pruba para observar si aparece el texto")
archivo.seek(0)
print(archivo.read())
archivo.close
