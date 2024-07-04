class Nodo:
    __calefactor: object
    __siguiente: object

    def __init__(self, calefactor):
        self.__calefactor = calefactor
        self.__siguiente = None

    def setSiguiente(self, calefactor):
        self.__siguiente = calefactor

    def getCalefactor(self):
        return self.__calefactor
    
    def getSiguiente(self):
        return self.__siguiente