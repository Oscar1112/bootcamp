mis_Datos = 
    {nombre: "Oscar", apellido: "Flores", edad: 20, altura: 1.69, Developer: true},
    

mi_edad = mis_Datos.edad
console.log(mi_edad)

lista_amigos = [
    {...mis_Datos},
    {nombre: "Roberto", apellido: "Villalobos", edad: 21, altura: 1.86, Developer: false},
    {nombre: "Oswaldo", apellido: "Merino", edad: 23, altua: 1.71, Developer: false},


]
lista_orden = lista_amigos.sort((a, b) => b.edad - a.edad)
console.log(lista_orden)