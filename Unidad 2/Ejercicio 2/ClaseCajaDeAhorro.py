class CajaDeAhorro:
    __nroCuenta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float
    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self.__nroCuenta = nroCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo
    def getNroCuenta(self):
        return self.__nroCuenta
    def getCUIL(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSaldo(self):
        return self.__saldo