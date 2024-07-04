class Alumno:
    __facultad = 'FCEFyN'
    __matricula: str
    __ingreso: int
    __promedio: float
    def __init__(self, m, i, p):
        self.__matricula = m
        self.__ingreso = int(i)
        self.__promedio = float(p)
    def mostrarDatos(self):
        print("Facultad: {}\nMatricula: {}\nIngreso: {}\nPromedio: {}".format(self.__facultad, self.__matricula, self.__ingreso, self.__promedio))
    def actualizarPromedio(self):
        self.__promedio = float(input("Ingrese nuevo promedio del alumno con matricula {}: ".format(self.__matricula)))
if __name__ == '__main__':
    alumno1 = Alumno('E010-50', 2022, 7.25)
    alumno2 = Alumno('E009-19', 2021, 8)
    alumno1.mostrarDatos()
    alumno2.mostrarDatos()
    alumno1.actualizarPromedio()
    alumno1.mostrarDatos()