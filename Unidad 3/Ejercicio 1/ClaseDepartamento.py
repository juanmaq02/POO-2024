class Departamento:
    __id = int
    __nya: str
    __numP: int
    __numD: int
    __cantD: int
    __cantB: int
    __superficie: float

    def __init__(self, id, nya, numP, numD, cantD, cantB, superficie):
        self.__id = id
        self.__nya = nya
        self.__numP = numP
        self.__numD = numD
        self.__cantD = cantD
        self.__cantB = cantB
        self.__superficie = superficie

    def getID(self):
        return self.__id

    def getNomYApe(self):
        return self.__nya

    def getNumPiso(self):
        return self.__numP

    def getNumDepa(self):
        return self.__numD

    def getCantDorm(self):
        return self.__cantD

    def getCantBanios(self):
        return self.__cantB

    def getSuperficie(self):
        return self.__superficie