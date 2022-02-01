#practica sobre clases
class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("alumno", self.nombre)
        print("nota", self.nota)
    def resultado(self):
        if self.nota < 5:
            print("no aprobo")
        else:
            print("aprobo")
alumno1 = Alumno("diego",4)
alumno2 = Alumno("juan",10)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()
        
        
