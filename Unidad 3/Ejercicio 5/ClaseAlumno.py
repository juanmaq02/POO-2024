class Alumno(object):
    __ayn: str
    __dni: int
    __registro: str
    __carrera: str
    __ingreso: int

    def __init__(self, ayn, dni, registro, carrera, ingreso):
        self.__ayn = ayn
        self.__dni = dni
        self.__registro = registro
        self.__carrera = carrera
        self.__ingreso = ingreso
    
    def getApeYNom(self):
        return self.__ayn
    
    def getDNI(self):
        return self.__dni
    
    def getRegistro(self):
        return self.__registro

    def getCarrera(self):
        return self.__carrera

    def getIngreso(self):
        return self.__ingreso

    def __str__(self):
        return f'Apellido y Nombre: {self.__ayn}      DNI: {self.__dni}\nRegistro: {self.__registro}       Carrera: {self.__carrera}\nAño de ingreso: {self.__ingreso}'