from ClaseDepartamento import Departamento

class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __nombreEmpresa: str
    __cantP: int
    __cantD: int
    __departamentos: list
    
    def __init__(self, id, nombre, direccion, nombreEmpresa, cantP, cantD):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nombreEmpresa = nombreEmpresa
        self.__cantP = cantP
        self.__cantD = cantD
        self.__departamentos = []

    def setDepartamento(self, id, nya, numP, numD, cantD, cantB, superficie):
        departamento = Departamento(id, nya, numP, numD, cantD, cantB, superficie)
        self.__departamentos.append(departamento)

    def getID(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getNombreEmpresa(self):
        return self.__nombreEmpresa

    def getCantP(self):
        return self.__cantP

    def getCantD(self):
        return self.__cantD
    
    def getDepartamentos(self):
        return self.__departamentos