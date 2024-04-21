class Moto:
    __patente: str
    __marca: str
    __nombre: str
    __apellido: str
    __km: float
    def __init__(self, patente, marca, nombre, apellido, km):
        self.__patente = patente
        self.__marca = marca
        self.__nombre = nombre
        self.__apellido = apellido
        self.__km = km
    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getKm(self):
        return self.__km
    def __lt__(self, other):
        return self.__patente < other.__patente