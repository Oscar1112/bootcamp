function verdad(){
    return true
}

setTimeout(function(){
    console.log("Hola Soy una promesa");
}, 5000);

function* generaindices(){
    let id = 0;
    while(true) {
        if(id === 10) {
       
        return
        }
        yield id= id + 2
    }
}
indice = generaindices()
console.log(indice.next())
console.log(indice.next())
console.log(indice.next())

