class Cuenta:
    __apellido: str
    __nombre: str
    __dni: int
    __telefono: str
    __saldo: float
    __cvu: int
    __porcentaje: float
    
    def __init__(self, apellido, nombre, dni, telefono, saldo, cvu, porcentaje = 68.0):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = int(dni)
        self.__telefono = telefono
        self.__saldo = float(saldo)
        self.__cvu = int(cvu)
        self.__porcentaje = porcentaje
        
    def getApellido(self):
        return self.__apellido
        
    def getNombre(self):
        return self.__nombre
        
    def getDNI(self):
        return self.__dni
        
    def getTelefono(self):
        return self.__telefono
        
    def getSaldo(self):
        return self.__saldo
        
    def getCVU(self):
        return self.__cvu
        
    def getPorcentaje(self):
        return self.__porcentaje
        
    def setSaldo(self, saldo):
        self.__saldo = saldo
        
    @classmethod
    def setPorcentaje(cls, porcentaje):
        cls.__porcentaje = float(porcentaje)