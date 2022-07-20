function tarea(num) {
    let array = [];
    array[0] = 0;
    array[1] = 1;
    for (let i = 2; i < num; i++) {
        array[i] = array[i - 2] + array[i -1];
    }
    return array;
}
let prueba = tarea(12);
console.log(prueba)


