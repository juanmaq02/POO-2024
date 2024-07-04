class Jugador:
    __nombre: str
    __fecha: str
    __hora: str
    __dificultad: str
    __puntaje: int

    def __init__(self, nombre, fecha, hora, dificultad, puntaje):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__hora = hora
        self.__dificultad = dificultad
        self.__puntaje = puntaje

    def getNombre(self):
        return self.__nombre

    def getFecha(self):
        return self.__fecha

    def getHora(self):
        return self.__hora
    
    def getDificultad(self):
        return self.__dificultad

    def getPuntaje(self):
        return self.__puntaje
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.getNombre(),
                fecha = self.getFecha(),
                hora = self.getHora(),
                dificultad = self.getDificultad(),
                puntaje = self.getPuntaje()
            )
        )
        return d

    def __gt__(self, otro):
        if self.__puntaje == otro.__puntaje:
            return self.__nombre > otro.__nombre
        return self.__puntaje > otro.__puntaje