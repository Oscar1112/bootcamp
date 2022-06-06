class Alumno:
    def _datos(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
   
    def dashboard(self):
        print("Su nombre es ",  self.nombre)
        print("Su nota es ",  self.nota)

    def Aprobación(self):
        if self.nota <= 5:
            return "Usted ha reprobado"
        else:
            print("Usted aprobó")

Carlos = Alumno()
Astrid = Alumno()

Carlos._datos("carlos", 10)
Astrid._datos("Astrid",2)

Carlos.dashboard()
Carlos.Aprobación()
Astrid.dashboard()
Astrid.datos()

