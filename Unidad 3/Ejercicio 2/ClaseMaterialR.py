class MaterialR:
    __material: str
    __caracteristicas: str
    __cantUtilizada: float
    __costoAdi: float

    def __init__(self, material, caracteristicas, cantUtilizada, costoAdi):
        self.__material = material
        self.__caracteristicas = caracteristicas
        self.__cantUtilizada = cantUtilizada
        self.__costoAdi = costoAdi

    def getMaterial(self):
        return self.__material

    def getCaracteristicas(self):
        return self.__caracteristicas

    def getCantUtilizada(self):
        return self.__cantUtilizada

    def getCostoAdi(self):
        return self.__costoAdi
