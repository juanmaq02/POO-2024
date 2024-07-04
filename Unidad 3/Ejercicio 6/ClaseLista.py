from ClaseNodo import Nodo
from ClaseCalefactorE import CalefactorE
from ClaseCalefactorG import CalefactorG
from ClaseInterfaz import Interfaz
from zope.interface import implementer

@implementer(Interfaz)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        self.__actual = self.__comienzo
        self.__indice = 0
        return self
    
    def __next__(self):
        if self.__actual is None:
            raise StopIteration
        elif self.__indice == self.__tope:
            raise StopIteration
        else:
            self.__indice += 1
            calefactor = self.__actual.getCalefactor()
            self.__actual = self.__actual.getSiguiente()
            return calefactor
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            calefactores = [calefactor.toJSON() for calefactor in self]
        )
        return d
    
    def agregarCalefactor(self, calefactor):
        nodo = Nodo(calefactor)
        if self.__comienzo == None:
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            while actual.getSiguiente() is not None:
                actual = actual.getSiguiente()
            actual.setSiguiente(nodo)
        self.__tope += 1

    def mostrarCalefactor(self, pos):
        cont = 0
        bandera = True
        for calefactor in self:
            if cont == pos:
                if isinstance(calefactor, CalefactorE):
                    print("\nCalefactor Electrico:\n")
                else:
                    print("Calefactor a Gas:\n")
                print(calefactor)
                bandera = False
            cont += 1
        if bandera:
            print("Posición de memoria no disponible.")

    def calefactorMenorPrecio(self):
        bandera = True
        for calefactor in self:
            if isinstance(calefactor, CalefactorG):
                if bandera:
                    min = calefactor
                    bandera = False
                else:
                    if calefactor < min:
                        min = calefactor
        print("Calefactor con menor precio:")
        print(min)

    def calefactoresEUnaMarca(self, marca):
        band = True
        for calefactor in self:
            if isinstance(calefactor, CalefactorE):
                if calefactor.getMarca() == marca:
                    print("Modelo: {}     Potencia máxima: {}\nPrecio: ${}".format(calefactor.getModelo(),
                                                                                   calefactor.getPotMax(),
                                                                                   calefactor.getPrecio()))
                    print("-----------------------------------")
                    band = False
        if band:
            print("No se han encontrado calefactores de la marca ingresada.")

    def calefactoresEnPromocion(self):
        print("Calefactores en promoción:\n")
        for calefactor in self:
            if calefactor.getPromocion() == 'Si':
                print("Marca: {}      Modelo: {}\nPaís de fabricación: {}     Importe de venta: ${}".format(calefactor.getMarca(),
                                                                                                            calefactor.getModelo(),
                                                                                                            calefactor.getPais(),
                                                                                                            calefactor.getImporteV()))
                print("------------------------------------")