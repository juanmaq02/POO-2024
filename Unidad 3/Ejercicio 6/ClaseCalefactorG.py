from ClaseCalefactor import Calefactor

class CalefactorG(Calefactor):
    __matricula: str
    __calorias: float

    def __init__(self, marca, modelo, pais, precio, formaP, cantC, promocion, matricula, calorias):
        super().__init__(marca, modelo, pais, precio, formaP, cantC, promocion)
        self.__matricula = matricula
        self.__calorias = calorias

    def getMatricula(self):
        return self.__matricula
    
    def getCalorias(self):
        return self.__calorias
    
    def setImporte(self):
        precio = self.getPrecio()
        if self.getCalorias() > 3000:
            precio += precio * 0.01
        if self.getFormaP() == 'cuotas':
            precio += precio * 0.4
        self.setPrecio(precio)
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                pais = self.getPais(),
                precio = self.getPrecio(),
                formaP = self.getFormaP(),
                cantC = self.getCantC(),
                promocion = self.getPromocion(),
                matricula = self.__matricula,
                calorias = self.__calorias,
                importeV = self.getImporteV()
            )
        )
        return d
    
    def __str__(self):
        return f'Marca: {self.getMarca()}    Modelo: {self.getModelo()}    País: {self.getPais()}\nPrecio base: ${self.getPrecio()}      Forma de pago: {self.getFormaP()}     Cantidad de cuotas: {self.getCantC()}\nPromoción: {self.getPromocion()}      Matricula: {self.__matricula}     Calorías: {self.__calorias} kilocalorias/m3'
    
    def __lt__(self, otro):
        return self.getImporteV() < otro.getImporteV()