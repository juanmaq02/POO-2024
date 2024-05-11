class Ladrillo:
    __alto: float
    __largo: float
    __ancho: float
    __cantidad: int
    __id: int
    __matPrimaUti: float
    __costo: float
    __materialR: list

    def __init__(self, cantidad, id, matPrimaUti, costo):
        self.__alto = 7
        self.__largo = 25
        self.__ancho = 15
        self.__cantidad = cantidad
        self.__id = id
        self.__matPrimaUti = matPrimaUti
        self.__costo = costo
        self.__materialR = []
    
    def agregarMaterialR(self, materialR):
        self.__materialR.append(materialR)