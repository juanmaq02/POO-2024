class Equipo:
    __idEquipo: int
    __nombre: str
    __golesAF: int
    __golesEC: int
    __difGoles: int
    __pts: int
    def __init__(self, idEquipo, nombre, golesAF, golesEC, difGoles, pts):
        self.__idEquipo = int(idEquipo)
        self.__nombre = nombre
        self.__golesAF = int(golesAF)
        self.__golesEC = int(golesEC)
        self.__difGoles = int(difGoles)
        self.__pts = int(pts)
    def getIDEquipo(self):
        return self.__idEquipo
    def getNombre(self):
        return self.__nombre
    def getGolesAF(self):
        return self.__golesAF
    def getGolesEC(self):
        return self.__golesEC
    def getDifGoles(self):
        return self.__difGoles
    def getPuntos(self):
        return self.__pts
    def setGolesAF(self, goles):
        self.__golesAF = goles
    def setGolesEC(self, goles):
        self.__golesEC = goles
    def setDifGoles(self):
        self.__difGoles = int(self.__golesAF) - int(self.__golesEC)
    def setPuntos(self, pts):
        self.__pts = pts
    def __gt__(self, other):
        if self.__pts == other.__pts:
            if self.__difGoles == other.__difGoles:
                return self.__golesAF > other.__golesAF
            return self.__difGoles > other.__difGoles
        return self.__pts > other.__pts