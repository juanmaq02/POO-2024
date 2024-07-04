from ClasePublicaciones import Publicacion

class CD(Publicacion):
    __duracion: int
    __nombreN: str

    def __init__(self, titulo, categoria, precio, duracion, nombreN):
        super().__init__(titulo, categoria, precio)
        self.__duracion = duracion
        self.__nombreN = nombreN