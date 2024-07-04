class Calefactor:
    __marca: str
    __modelo: str
    __pais: str
    __precio: float
    __formaP: str
    __cantC: int
    __promocion: str
    __importeV: float

    def __init__(self, marca, modelo, pais, precio, formaP, cantC, promocion, importeV = 0):
        self.__marca = marca
        self.__modelo = modelo
        self.__pais = pais
        self.__precio = precio
        self.__formaP = formaP
        self.__cantC = cantC
        self.__promocion = promocion
        self.__importeV = importeV
    
    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getPais(self):
        return self.__pais

    def getPrecio(self):
        return self.__precio

    def getFormaP(self):
        return self.__formaP

    def getCantC(self):
        return self.__cantC

    def getPromocion(self):
        return self.__promocion
    
    def getImporteV(self):
        return self.__importeV

    def setPrecio(self, pl):
        if self.getPromocion() == 'Si':
            pl -= pl * 0.15
        self.__importeV = pl