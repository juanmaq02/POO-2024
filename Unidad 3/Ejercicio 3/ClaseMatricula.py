class Matricula:
    __fecha: str
    __empleado: object
    __programa: object

    def __init__(self, fecha, empleado, programa):
        self.__fecha = fecha
        self.__empleado = empleado
        self.__programa = programa

    def __str__(self):
        return f'Fecha: {self.__fecha}\nEmpleado:\n{self.__empleado}\nPrograma:\n{self.__programa}'
    
    def getEmpleado(self):
        return self.__empleado
    
    def getProgramaC(self):
        return self.__programa