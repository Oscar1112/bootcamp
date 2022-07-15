let compras = ["leche", "pan", "cereal", "mantequilla", "azucar"];
(compras.push("Aceite de Girasol"));
console.log(compras)


//eliminar elementos
console.log(compras.pop("Aceite de Girasol"))
console.log(compras)

let peliculas = [
    {titulo: "soy leyenda", director: "Lawrence", año: "2007"},
    {titulo: "Dioses de Egipto", director: "Proyas", año: "2016"},
    {titulo: "El caminio", director: "Guillian", año: "2019"}

]

recientes = peliculas.filter(rec => rec.año > 2010)
console.log(recientes)

directores = peliculas.map(dir => {
return dir.director;
})
console.log(directores)

title = peliculas.map (titu => {
    return titu.titulo;
})
console.log(title)

concatenacion = title.concat(directores)
console.log(concatenacion)

let f_propagacion = [...title, ...directores]
console.log(f_propagacion)