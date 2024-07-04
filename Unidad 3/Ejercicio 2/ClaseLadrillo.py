class Ladrillo:
    __alto = 7
    __largo = 25
    __ancho = 15
    __cantidad: int
    __id: int
    __matPrimaUti: float
    __costo: float
    __materialR: list

    def __init__(self, cantidad, id, matPrimaUti, costo):
        self.__cantidad = cantidad
        self.__id = id
        self.__matPrimaUti = matPrimaUti
        self.__costo = costo
        self.__materialR = []
    
    def agregarMaterialR(self, materialR, cantidad):
        for i in range(cantidad):
            self.__materialR.append(materialR)
    
    @classmethod
    def getAlto(cls):
        return cls.__alto
    
    @classmethod
    def getLargo(cls):
        return cls.__largo
    
    @classmethod
    def getAncho(cls):
        return cls.__ancho
    
    def getCantidad(self):
        return self.__cantidad
    
    def getID(self):
        return self.__id
    
    def getMatPrimaUti(self):
        return self.__matPrimaUti
    
    def getCosto(self):
        return self.__costo
    
    def getMaterialR(self):
        return self.__materialR

    def __str__(self):
        return f'ID: {self.__id}'
    