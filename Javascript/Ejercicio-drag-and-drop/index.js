const parrafos = document.querySelectorAll(".parrafo")
const secciones = document.querySelectorAll(".section")

parrafos.forEach(parrafo => {
    parrafo.addEventListener("dragstart", event => {
        console.log("Estoy arrastrando el parrafo: " + parrafo.innerText )
        parrafo.classList.add("dragging")
        event.dataTransfer.setData("id", parrafo.id)
    })

    parrafo.addEventListener("dragend", () => {
        // console.log("He terminado de arrastrar")
        parrafo.classList.remove("dragging")
    })
})

    secciones.forEach(section => {
        section.addEventListener("dragover", event => {
            event.preventDefault()
            // console.log("Drag Over")
       //
    })
    section.addEventListener("drop", event=> {
        console.log("Drop")
        const id_parrafo = event.dataTransfer.getData("id")
        // console.log("Parrafo id: ", id_parrafo)
        const parrafo = document.getElementById(id_parrafo)
        section.appendChild(parrafo)
    })
});

const eliminar = document.querySelector(".eliminar")

//eliminar comportamiento por default
eliminar.addEventListener("dragover", event => {
    event.preventDefault()
})

//instruir la eliminacion del archivo
eliminar.addEventListener("drop", event => {
    const eliminar = event.dataTransfer.getData("id")
    document.getElementById(eliminar).remove()
})

