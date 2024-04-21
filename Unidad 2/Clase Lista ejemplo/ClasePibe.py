class Pibe:
    __nombre: str
    __apellido: str
    __edad: int
    __dni: int
    __altura: float
    def __init__(self, nombre, apellido, edad, dni, altura):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = int(edad)
        self.__dni = int(dni)
        self.__altura = float(altura)
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return(self.__apellido)
    def getEdad(self):
        return self.__edad
    def getDNI(self):
        return self.__dni
    def getAltura(self):
        return self.__altura