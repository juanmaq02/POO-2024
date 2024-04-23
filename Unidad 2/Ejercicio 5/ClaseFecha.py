class Fecha:
    __fecha: str
    __idEquipoL: int
    __idEquipoV: int
    __golesL: int
    __golesV: int
    def __init__(self, fecha, idEquipoL, idEquipoV, golesL, golesV):
        self.__fecha = fecha
        self.__idEquipoL = int(idEquipoL)
        self.__idEquipoV = int(idEquipoV)
        self.__golesL = int(golesL)
        self.__golesV = int(golesV)
    def getFecha(self):
        return self.__fecha
    def getIDEquipoL(self):
        return self.__idEquipoL
    def getIDEquipoV(self):
        return self.__idEquipoV
    def getGolesL(self):
        return self.__golesL
    def getGolesV(self):
        return self.__golesV