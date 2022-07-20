class Estudiante {
    nombre ="Oscar"
    asignaturas = ["Javascript", "Html", "Css"]
    obtenDatos() {
        return {
            nombre: this.nombre,
            asignaturas: this.asignaturas
        }
    }
}

const Estudiante1 = new Estudiante("Roberto", ["Css, React, Angular"])
console.log(Estudiante1.obtenDatos())