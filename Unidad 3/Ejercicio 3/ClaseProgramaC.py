from ClaseMatricula import Matricula

class ProgramaC:
    __nombre: str
    __codigo: str
    __duracion: int
    __matriculas: list
    __idActual = 0

    def __init__(self, nombre, codigo, duracion):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__duracion = duracion
        self.__matriculas = []

    @classmethod
    def getID(cls):
        cls.__idActual += 1
        return cls.__idActual

    def matricularEmpleado(self, empleado, fecha, c):
        mat = Matricula(fecha, empleado, self)
        self.__matriculas.append(mat)
        c.agregarMatricula(mat)

    def __str__(self):
        return f'{self.__nombre}     Codigo: {self.__codigo}\n   Duracion: {self.__duracion} horas'
    
    def getMatriculas(self):
        return self.__matriculas
    
    def getNombre(self):
        return self.__nombre
    
    def getDuracion(self):
        return self.__duracion
    
    def __eq__(self, otro):
        return self.__nombre == otro