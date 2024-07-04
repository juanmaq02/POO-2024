from ClaseCalefactor import Calefactor

class CalefactorE(Calefactor):
    __potMax: float

    def __init__(self, marca, modelo, pais, precio, formaP, cantC, promocion, potMax):
        super().__init__(marca, modelo, pais, precio, formaP, cantC, promocion)
        self.__potMax = potMax

    def getPotMax(self):
        return self.__potMax
    
    def setImporte(self):
        precio = self.getPrecio()
        if self.getPotMax() > 1000:
            precio += precio * 0.01
        if self.getFormaP() == 'cuotas':
            precio += precio * 0.3
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
                potMax = self.__potMax,
                importeV = self.getImporteV()
            )
        )
        return d
    
    def __str__(self):
        return f'Marca: {self.getMarca()}    Modelo: {self.getModelo()}    País: {self.getPais()}\nPrecio base: ${self.getPrecio()}      Forma de pago: {self.getFormaP()}     Cantidad de cuotas: {self.getCantC()}\nPromoción: {self.getPromocion()}      Potencia máxima: {self.__potMax} watts.'
    