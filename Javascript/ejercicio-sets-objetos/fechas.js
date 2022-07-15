fecha_hoy = new Date()
console.log(fecha_hoy)

fecha_nac = new Date("December 11, 2001")

console.log(fecha_hoy > fecha_nac)

//dia nacimiento
dia_naci = (fecha_nac.getDate())
console.log(dia_naci)

//mes nacimiento
mes_naci =(fecha_nac.getMonth())
console.log(mes_naci)

//año nacimiento
año = (fecha_nac.getFullYear())
console.log(año)