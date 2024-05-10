class Pedido:
    __patente: str
    __id: int
    __comidas: str
    __tiempoE: int
    __tiempoR: int
    __precio: float
    def __init__(self, patente, ide, comidas, tiempoE, precio, tiempoR = 0):
        self.__patente = patente
        self.__id = ide
        self.__comidas = comidas
        self.__tiempoE = tiempoE
        self.__tiempoR = tiempoR
        self.__precio = precio
    def getPatente(self):
        return self.__patente
    def getID(self):
        return self.__id
    def getComidas(self):
        return self.__comidas
    def getTiempoE(self):
        return self.__tiempoE
    def getTiempoR(self):
        return self.__tiempoR
    def getPrecio(self):
        return self.__precio
    def setTiempoR(self, tiempo):
        self.__tiempoR = tiempo
    def __lt__(self, other):
        return self.__comidas < other.__comidas