class Transaccion:
    __cvu: int
    __nroTransaccion: int
    __importe: float
    __tipoTransaccion: str
    
    def __init__(self, cvu, nroTransaccion, importe, tipoTransaccion):
        self.__cvu = int(cvu)
        self.__nroTransaccion = int(nroTransaccion)
        self.__importe = float(importe)
        self.__tipoTransaccion = tipoTransaccion
        
    def getCVU(self):
        return self.__cvu
        
    def getNroTransaccion(self):
        return self.__nroTransaccion
        
    def getImporte(self):
        return self.__importe
        
    def getTipoTransaccion(self):
        return self.__tipoTransaccion