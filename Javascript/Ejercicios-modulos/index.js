import * as funciones from"./controller.js";
import chalk from "chalk"

const sumatoria = funciones.suma(4, 5)
console.log(sumatoria)

const multiplicacion = funciones.multiplica(1, 2)
console.log(multiplicacion)

console.log(chalk.green(funciones.multiplica(funciones.suma(1, 2), funciones.suma(4, 5))));

